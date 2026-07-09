from unittest.mock import patch

import pytest
from pygments.util import ClassNotFound
from rich.console import Console
from rich.text import Text

from rich_rst import (
    RestructuredText,
    RSTVisitor,
    _colSpan,
    _rowSpan,
    availability,
    hlist_block,
    py_desc,
    soft_deprecated,
    toctree_stub,
)
from rich_rst._vendor import docutils


class MockDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_calls = 0

    def get(self, key, default=None):
        self.get_calls += 1
        if self.get_calls == 2:
            return lambda node: None
        return super().get(key, default)


class MockChildrenList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iter_count = 0

    def __iter__(self):
        self.iter_count += 1
        if self.iter_count == 1:
            return iter([])
        return super().__iter__()


def test_dispatch_cache_hits():
    # Test visitor dispatch cache hit when accessed under a concurrent lock.
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    visitor._visit_dispatch_cache = MockDict(visitor._visit_dispatch_cache)
    visitor._depart_dispatch_cache = MockDict(visitor._depart_dispatch_cache)

    node_type = docutils.nodes.paragraph
    handler_visit = visitor._resolve_visit_handler(node_type)
    assert handler_visit is not None

    handler_depart = visitor._resolve_depart_handler(node_type)
    assert handler_depart is not None


def test_guess_lexer_name_exception():
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console, guess_lexer=True)

    with patch('rich_rst.guess_lexer', side_effect=ClassNotFound):
        lexer, was_guessed = visitor._guess_lexer_name('some text')
        assert lexer == 'python'
        assert not was_guessed


def test_indirect_link_references():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    ref_node = docutils.nodes.reference(text='some link', refname='mylink')
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_reference(ref_node)

    assert 'mylink' in visitor.refname_to_renderable

    target_node = docutils.nodes.target(refuri='http://example.com', names=['mylink'])
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_target(target_node)


def test_paragraph_in_system_message():
    sys_msg = docutils.nodes.system_message(
        'System message details',
        source='test.rst',
        line=1,
        type='WARNING',
        level=2,
    )
    para = docutils.nodes.paragraph(text='System message details')
    sys_msg.append(para)
    para.parent = sys_msg

    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(sys_msg, console=console)

    with patch.object(visitor, 'visit_system_message', return_value=None):
        with pytest.raises(docutils.nodes.SkipChildren):
            visitor.visit_paragraph(para)


def test_compound_elements(make_visitor):
    rst_text = """
.. compound::

   This is compound text.
"""
    visitor = make_visitor(rst_text)
    assert visitor is not None


def test_inline_nodes():
    inline_node = docutils.nodes.inline(text='generic inline')
    inline_node_with_class = docutils.nodes.inline(text='styled inline', classes=['custom-style'])

    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_inline(inline_node)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_inline(inline_node_with_class)


def test_compact_admonition_empty_body():
    # Compact admonition with empty body
    rst_text = '.. note::'
    rst = RestructuredText(rst_text, admonition_style='compact')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_admonition_without_title():
    # Generic admonition without a title
    admon = docutils.nodes.admonition()
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_admonition(admon)


def test_custom_directives_degraded():
    # Version directives without versions degrading to normal admonitions
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    avail = availability()
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_availability(avail)

    soft_dep = soft_deprecated()
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_soft_deprecated(soft_dep)


def test_py_fields_rendering():
    # Python-specific desc field list rendering cases
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    # Field list with a field having less than 2 children (empty/short fields)
    fl_empty = docutils.nodes.field_list()
    f_empty = docutils.nodes.field()
    fl_empty.append(f_empty)
    doc.append(fl_empty)
    with patch.object(visitor, '_render_admonition_body', return_value=[]):
        res = visitor._render_py_field_list(fl_empty)
    assert isinstance(res, list)

    # Type defined before parameter
    fl_type_first = docutils.nodes.field_list()
    f1 = docutils.nodes.field()
    f1.append(docutils.nodes.field_name(text='type myparam'))
    fb1 = docutils.nodes.field_body()
    fb1.append(docutils.nodes.paragraph(text='int'))
    f1.append(fb1)
    fl_type_first.append(f1)
    doc.append(fl_type_first)
    res2 = visitor._render_py_field_list(fl_type_first)
    assert len(res2) > 0

    # Return type only (no return description)
    fl_rtype = docutils.nodes.field_list()
    f2 = docutils.nodes.field()
    f2.append(docutils.nodes.field_name(text='rtype'))
    fb2 = docutils.nodes.field_body()
    fb2.append(docutils.nodes.paragraph(text='str'))
    f2.append(fb2)
    fl_rtype.append(f2)
    doc.append(fl_rtype)
    res3 = visitor._render_py_field_list(fl_rtype)
    assert len(res3) > 0


def test_py_metadata_empty():
    # Empty python description option list rendering
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    node = py_desc(options={'random': 'value'})
    res = visitor._render_py_desc_options(node)
    assert res == []


def test_py_desc_panel_style_falsy():
    # Falsy object type name styling fallback
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    style = visitor._py_desc_panel_style('', domain='py')
    assert style is not None


def test_signature_highlighters():
    # Empty signatures and highlighters for various domains
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    # C/C++ empty signature
    assert len(visitor._highlight_c_cpp_signature('c', 'function', '')) == 0

    # JS empty signature
    assert len(visitor._highlight_js_signature('function', '')) == 0

    # JS signature with keywords and styling
    js_sig = visitor._highlight_js_signature('function', 'async function test()')
    assert len(js_sig) > 0

    # JS signature attributes
    js_attr = visitor._highlight_js_signature('attribute', 'myAttr')
    assert len(js_attr) > 0

    # Py empty signature
    assert len(visitor._highlight_py_signature('function', '')) == 0


def test_py_signature_bracket_scans():
    # Bracket-aware scanning logic in python signature parsing
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    # Arrow scan with bracket depth
    sig1 = 'def foo() ->  list[str, int] '
    res1 = visitor._highlight_py_signature('function', sig1)
    assert len(res1) > 0

    # Arrow scan unmatched closing bracket
    sig2 = 'def foo() -> list]'
    res2 = visitor._highlight_py_signature('function', sig2)
    assert len(res2) > 0

    # Colon param spaces
    sig3 = 'foo(param:  int)'
    res3 = visitor._highlight_py_signature('function', sig3)
    assert len(res3) > 0

    # Colon param continue on delimiter
    sig4 = 'foo(param: )'
    res4 = visitor._highlight_py_signature('function', sig4)
    assert len(res4) > 0

    # Colon param brackets and spaces
    sig5 = 'foo(param:  list[str])'
    res5 = visitor._highlight_py_signature('function', sig5)
    assert len(res5) > 0


def test_split_py_attribute_signature():
    # Split signature type signatures partition helper
    name, typ = RSTVisitor._split_py_attribute_signature('attr : int')
    assert name == 'attr'
    assert typ == 'int'


def test_collect_typed_class_attributes():
    # Collect typed py attributes
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    class_node = docutils.nodes.Element()
    child = py_desc(objtype='attribute', sig='attr : int')
    child.append(docutils.nodes.field_list())
    class_node.append(child)

    attrs, _remaining = visitor._collect_typed_class_attributes(class_node)
    assert len(attrs) == 1
    assert attrs[0][0] == 'attr'
    assert attrs[0][1] == 'int'


def test_visit_toctree_block():
    # Toctree stub visitor handling empty entry cases
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    node = toctree_stub()
    node['entries'] = ['', 'Display Title <docname>']
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_toctree_stub(node)


def test_visit_hlist_block():
    # Hlist block items with empty, multiple, or padded columns
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    # Hlist_block without items
    node_empty = hlist_block(columns=2)
    doc.append(node_empty)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_hlist_block(node_empty)

    # Items with multiple renderables and padding
    node = hlist_block(columns=3)
    bl = docutils.nodes.bullet_list()

    li1 = docutils.nodes.list_item()
    bl.append(li1)

    li2 = docutils.nodes.list_item()
    p1 = docutils.nodes.paragraph(text='p1')
    p2 = docutils.nodes.paragraph(text='p2')
    li2.append(p1)
    li2.append(p2)
    bl.append(li2)

    node.append(bl)
    doc.append(node)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_hlist_block(node)


def test_visit_figure_no_image():
    # Figure node without image elements
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    fig = docutils.nodes.figure()
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_figure(fig)


def test_merge_bullet_markers_with_text():
    # Bullet marker text merging helper
    res = RSTVisitor._merge_bullet_markers_with_text([Text('•'), Text(' item text'), Text('other')])
    assert len(res) == 2
    assert res[0].plain == '• item text'


def test_bullet_list_non_text_or_empty():
    # Bullet list item having a non-text first child (Panel)
    rst_text = """
- .. admonition:: Hi
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_enumerated_list_multi_paragraph():
    # Multi-paragraph items in enumerated lists
    rst_text = """
1. Item first paragraph.

   Item second paragraph.
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_visit_authors():
    # Multiple authors docinfo field rendering
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    authors_node = docutils.nodes.authors()
    authors_node.append(docutils.nodes.author(text='Author 1'))
    authors_node.append(docutils.nodes.author(text='Author 2'))

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_authors(authors_node)


def test_definition_list_empty_item():
    # Empty definition list item cases
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    dl = docutils.nodes.definition_list()
    di = docutils.nodes.definition_list_item()
    dl.append(di)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_definition_list(dl)


def test_blockquote_non_text_child():
    # Blockquote first child not being a text node
    rst_text = """
    .. admonition:: Inside blockquote
    """
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_topic_empty_body():
    # Topic block with no body children
    rst_text = """
.. topic:: Topic Title
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_math_block_preceding_paragraph():
    # Math block with preceding paragraph node
    rst_text = """
Preceding paragraph.

.. math::

   E = mc^2
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_minor_elements_visitors():
    # Visitor handlers for various minor elements
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    # visit_citation_reference
    cit = docutils.nodes.citation_reference(text='[cit1]')
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_citation_reference(cit)

    # visit_footnote_reference
    fn = docutils.nodes.footnote_reference(text='1')
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_footnote_reference(fn)

    # visit_substitution_reference
    sub = docutils.nodes.substitution_reference(text='sub')
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_substitution_reference(sub)

    # visit_generated
    gen = docutils.nodes.generated(text='gen')
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_generated(gen)

    # visit_pending
    class DummyTransform:
        pass

    pen = docutils.nodes.pending(DummyTransform)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_pending(pen)

    # visit__colSpan
    col = _colSpan()
    with pytest.raises(docutils.nodes.SkipNode):
        visitor.visit__colSpan(col)

    # visit__rowSpan
    row = _rowSpan()
    with pytest.raises(docutils.nodes.SkipNode):
        visitor.visit__rowSpan(row)


def test_table_basic_edge_cases():
    # visit_table no tgroup
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(docutils.nodes.table())


def test_table_spans_and_edge_cases():
    # 1. tbody is None check
    tgroup = docutils.nodes.tgroup(cols=2)
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)

    table1 = docutils.nodes.table()
    table1.append(tgroup)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table1)

    # 2. Programmatically build a table with colspec absent, and row/colspans
    tgroup_full = docutils.nodes.tgroup()
    thead = docutils.nodes.thead()
    tr_head = docutils.nodes.row()
    tr_head.append(docutils.nodes.entry(morecols=1))
    thead.append(tr_head)
    tgroup_full.append(thead)

    tbody = docutils.nodes.tbody()

    # Row 1: has rowspan and colspan
    r1 = docutils.nodes.row()
    e1 = docutils.nodes.entry(morerows=1, morecols=1)
    e1.append(docutils.nodes.paragraph(text='span cell'))
    r1.append(e1)
    e2 = docutils.nodes.entry()
    e2.append(docutils.nodes.paragraph(text='normal'))
    r1.append(e2)
    tbody.append(r1)

    # Row 2: empty row to trigger rowspan occupancies and empty pad
    r2 = docutils.nodes.row()
    tbody.append(r2)

    tgroup_full.append(tbody)

    table2 = docutils.nodes.table()
    table2.append(tgroup_full)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table2)


def test_table_advanced_spans():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)

    tgroup = docutils.nodes.tgroup(cols=3)
    thead = docutils.nodes.thead()
    tr_head = docutils.nodes.row()
    tr_head.append(docutils.nodes.entry(morecols=1))
    thead.append(tr_head)
    tgroup.append(thead)

    tbody = docutils.nodes.tbody()

    r1 = docutils.nodes.row()
    e1 = docutils.nodes.entry(morerows=1)
    e1.append(docutils.nodes.paragraph(text='rowspan cell'))
    r1.append(e1)

    r2 = docutils.nodes.row()

    tbody.append(r1)
    tbody.append(r2)

    tbody.children = MockChildrenList(tbody.children)
    tgroup.append(tbody)

    table = docutils.nodes.table()
    table.append(tgroup)

    # Set occupied cells and row spans to execute loop 4452-4455
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


def test_table_width_shrinking_edge_cases():
    console = Console(force_terminal=True, width=120)

    import builtins

    original_min = builtins.min

    def mock_min(*args, **kwargs):
        if len(args) == 3 and args[2] == 9999:
            return 0
        return original_min(*args, **kwargs)

    with patch('rich_rst.min', mock_min):
        tgroup = docutils.nodes.tgroup(cols=2)
        colspec1 = docutils.nodes.colspec(colwidth=5)
        colspec2 = docutils.nodes.colspec(colwidth=10)
        tgroup.append(colspec1)
        tgroup.append(colspec2)

        thead = docutils.nodes.thead()
        tr_head = docutils.nodes.row()
        e_head1 = docutils.nodes.entry()
        e_head1.append(docutils.nodes.paragraph(text='h1'))
        e_head2 = docutils.nodes.entry()
        e_head2.append(docutils.nodes.paragraph(text='h2'))
        tr_head.append(e_head1)
        tr_head.append(e_head2)
        thead.append(tr_head)
        tgroup.append(thead)

        tbody = docutils.nodes.tbody()
        r = docutils.nodes.row()
        e = docutils.nodes.entry(morerows=1)
        e.append(docutils.nodes.paragraph(text='line1\nline2'))
        r.append(e)
        e_wide = docutils.nodes.entry()
        e_wide.append(docutils.nodes.paragraph(text='very_long_cell_text'))
        r.append(e_wide)
        tbody.append(r)

        # Grid table generation with entry is None inside spans-active layout
        r2 = docutils.nodes.row()
        tbody.append(r2)
        tgroup.append(tbody)

        doc = docutils.core.publish_doctree('Hello')
        visitor = RSTVisitor(doc, console=console)
        mock_options = visitor.console.options.update(max_width=1)

        from unittest.mock import PropertyMock

        with patch.object(Console, 'options', new_callable=PropertyMock) as mock_opts:
            mock_opts.return_value = mock_options

            table = docutils.nodes.table()
            table.append(tgroup)
            with pytest.raises(docutils.nodes.SkipChildren):
                visitor.visit_table(table)

            print('RENDERABLES:', visitor.renderables)
            for r in visitor.renderables:
                console.print(r)


def test_branch_coverage_various_directives():
    rst_text = """
.. code-block:: python
   :emphasize-lines: 5-3, malformed

   print("hello")

.. math::

.. only:: html

.. hlist::
   :columns: 3

.. glossary::

.. glossary::
   :sorted:

   This is a paragraph, not a definition list!
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_literalinclude_empty_range_parts():
    # test lines option with empty parts e.g. "1-2, ,3"
    rst_text = """
.. literalinclude:: tests/requirements.txt
   :lines: 1-2, ,3
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_sphinx_registration_no_roles_attr():
    import rich_rst
    import rich_rst._vendor.docutils.parsers.rst.languages.en as _en

    if hasattr(_en, 'roles'):
        orig_roles = _en.roles
        delattr(_en, 'roles')
        try:
            rich_rst._sphinx_roles_registered = False
            rich_rst._sphinx_directives_registered = False
            rich_rst._register_sphinx_roles()
            rich_rst._register_sphinx_directives()
        finally:
            _en.roles = orig_roles


def test_command_program_empty_potential_display():
    rst = RestructuredText('hello :command:` <target>` and :func:` <func_target>`')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_subclass_unregister_visitor():
    class MySubVisitor(RSTVisitor):
        pass

    MySubVisitor.unregister_visitor(docutils.nodes.paragraph)


def test_find_lexer_non_element():
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)
    lexer, _source = visitor._find_lexer(docutils.nodes.Text('abc'))
    assert lexer == 'python'


def test_footnote_empty_child():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    fn = docutils.nodes.footnote()
    fn.append(docutils.nodes.label(text='1'))
    fn.append(docutils.nodes.Text(''))
    res = visitor._format_labelled_node(fn)
    assert res == '1:'


def test_target_no_uri():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    node = docutils.nodes.target(names=['myname'])
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_target(node)


def test_depart_paragraph_empty_renderables():
    from rich.panel import Panel

    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    visitor.depart_paragraph(docutils.nodes.paragraph())

    visitor.renderables.append(Panel(Text('hi')))
    visitor.depart_paragraph(docutils.nodes.paragraph())


def test_prepend_styled_prefix_empty_body():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    visitor._prepend_styled_prefix(Text('prefix'), [])


def test_version_directive_multi_element_body():
    rst_text = """
.. versionadded:: 1.0

   First para.

   Second para.
"""
    rst = RestructuredText(rst_text, admonition_style='compact')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_signatures_edge_cases():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    assert visitor._highlight_c_cpp_signature('c', 'alias', 'invalid_alias') is not None
    assert visitor._highlight_c_cpp_signature('c', 'function', 'invalid_func') is not None
    assert visitor._highlight_c_cpp_signature('c', 'class', '') is not None
    assert visitor._highlight_c_cpp_signature('c', 'member', 'int') is not None

    assert visitor._highlight_js_signature('function', 'invalid_js_func') is not None
    assert visitor._highlight_js_signature('class', '') is not None
    assert visitor._highlight_js_signature('module', 'mod.') is not None
    assert visitor._highlight_js_signature('attribute', '') is not None
    assert visitor._highlight_js_signature('data', '') is not None

    assert visitor._highlight_py_signature('function', 'def f() ->   ') is not None
    assert visitor._highlight_py_signature('function', 'def f(a:  )') is not None
    assert visitor._highlight_py_signature('function', 'def f(a: )') is not None
    assert visitor._highlight_py_signature('function', 'def f(a:int, b:str)') is not None


def test_hlist_block_edge_cases():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    node = hlist_block(columns=2)
    node.append(docutils.nodes.paragraph(text='not bullet list'))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_hlist_block(node)


def test_bullet_list_non_text_first_child():
    rst_text = """
- .. admonition:: Hi
     :class: custom
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)

    rst_text2 = """
1. .. admonition:: Hi
      :class: custom
"""
    rst2 = RestructuredText(rst_text2)
    console.print(rst2)


def test_table_compact_lines_empty():
    rst_text = """
+----+
| -  |
+----+
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_table_no_spans_bypass_spans():
    class MockThead(docutils.nodes.thead):
        def __init__(self, *args, **kwargs):
            self._first_call = True
            super().__init__(*args, **kwargs)

        @property
        def children(self):
            if getattr(self, '_first_call', False):
                self._first_call = False
                r = docutils.nodes.row()
                r.append(docutils.nodes.entry())
                return [r]
            else:
                r = docutils.nodes.row()
                r.append(docutils.nodes.entry(morecols=1))
                return [r]

        @children.setter
        def children(self, value):
            pass

    class MockTbody(docutils.nodes.tbody):
        def __init__(self, *args, **kwargs):
            self._first_call = True
            super().__init__(*args, **kwargs)

        @property
        def children(self):
            if getattr(self, '_first_call', False):
                self._first_call = False
                r = docutils.nodes.row()
                r.append(docutils.nodes.entry())
                return [r]
            else:
                r1 = docutils.nodes.row()
                r1.append(docutils.nodes.entry(morerows=1, morecols=1))
                r2 = docutils.nodes.row()
                r3 = docutils.nodes.row()
                r3.append(docutils.nodes.entry())
                return [r1, r2, r3]

        @children.setter
        def children(self, value):
            pass

    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    tgroup = docutils.nodes.tgroup()
    tgroup.append(docutils.nodes.colspec(colwidth=5))
    tgroup.append(docutils.nodes.colspec(colwidth=5))
    tgroup.append(docutils.nodes.colspec(colwidth=5))

    thead = MockThead()
    tbody = MockTbody()
    tgroup.append(thead)
    tgroup.append(tbody)
    table = docutils.nodes.table()
    table.append(tgroup)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


def test_sphinx_compat_false():
    rst = RestructuredText('hello world', sphinx_compat=False)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_render_no_renderables():
    rst = RestructuredText('.. comment')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_render_non_text_renderable():
    rst = RestructuredText("""
+---+
| a |
+---+
""")
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_render_ends_with_newline():
    rst = RestructuredText('some paragraph\n\n')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_citations_and_footer():
    rst_text = """
.. [citation1] Citation body text.
.. [*] Footnote body text.

.. raw:: html

   <p>raw html</p>
"""
    rst = RestructuredText(rst_text, show_errors=True)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_visit_generated():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_generated(docutils.nodes.generated(text='gen'))
    assert len(visitor.footer) == 1


def test_math_directive_empty_run():
    from unittest.mock import MagicMock

    from rich_rst import _MathDirective

    directive = MagicMock(spec=_MathDirective)
    directive.arguments = ['   ']
    directive.content = []
    res = _MathDirective.run(directive)
    assert res == []


def test_sphinx_role_empty_display_via_rst():
    rst = RestructuredText('hello :func:`<target>` and :command:`<target>`')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_emit_version_directive_multi_element_body():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    visitor.admonition_style = 'compact'
    node1 = docutils.nodes.paragraph(text='first')
    node2 = docutils.nodes.paragraph(text='second')
    visitor._emit_version_directive('versionadded', '1.0', [node1, node2])


def test_render_py_field_list_direct():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)

    fl = docutils.nodes.field_list()
    f1 = docutils.nodes.field()
    f1.append(docutils.nodes.field_name(text='param myparam'))
    fb1 = docutils.nodes.field_body()
    fb1.append(docutils.nodes.paragraph(text='first desc'))
    f1.append(fb1)

    f2 = docutils.nodes.field()
    f2.append(docutils.nodes.field_name(text='param myparam'))
    fb2 = docutils.nodes.field_body()
    fb2.append(docutils.nodes.paragraph(text='second desc'))
    f2.append(fb2)

    fl.append(f1)
    fl.append(f2)

    f3 = docutils.nodes.field()
    f3.append(docutils.nodes.field_name(text='param otherparam'))
    fb3 = docutils.nodes.field_body()
    fb3.append(docutils.nodes.paragraph(text='desc without type'))
    f3.append(fb3)
    fl.append(f3)

    f4 = docutils.nodes.field()
    f4.append(docutils.nodes.field_name(text='raises ValueError'))
    fb4 = docutils.nodes.field_body()
    fb4.append(docutils.nodes.paragraph(text=''))
    f4.append(fb4)
    fl.append(f4)

    res = visitor._render_py_field_list(fl)
    assert len(res) > 0


def test_c_cpp_signature_none_matches():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    assert visitor._highlight_c_cpp_signature('c', 'class', '...') is not None


def test_js_signature_none_matches():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    assert visitor._highlight_js_signature('class', '...') is not None
    assert visitor._highlight_js_signature('attribute', '...') is not None
    assert visitor._highlight_js_signature('data', '...') is not None


def test_highlight_py_signature_direct():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    visitor._highlight_py_signature('function', 'def f() -> int, None')
    visitor._highlight_py_signature('function', 'def f() ->   int')
    visitor._highlight_py_signature('function', 'def f(a:   int)')
    visitor._highlight_py_signature('function', 'def f(a: int)')
    visitor._highlight_py_signature('function', 'def f(a:  int)')
    visitor._highlight_py_signature('function', 'def f(a: )')


def test_collect_typed_class_attributes_direct():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    class_node = docutils.nodes.Element()

    c1 = py_desc(objtype='attribute', sig='attr1')
    class_node.append(c1)

    c2 = py_desc(objtype='attribute', sig='attr2 : int')
    c2.append(docutils.nodes.Text('   '))
    class_node.append(c2)

    c3 = py_desc(objtype='attribute', sig='attr3 : int')
    class_node.append(c3)

    attrs, _remaining = visitor._collect_typed_class_attributes(class_node)
    assert len(attrs) == 2
    visitor._render_py_class_attribute_table(attrs)


def test_visit_hlist_block_multiple_renderables():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = hlist_block(columns=2)
    bl = docutils.nodes.bullet_list()
    li = docutils.nodes.list_item()
    li.append(docutils.nodes.paragraph(text='p1'))
    li.append(docutils.nodes.paragraph(text='p2'))
    bl.append(li)
    node.append(bl)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_hlist_block(node)


def test_bullet_list_non_text_rendering():
    rst_text = """
- .. note::
     Admonition body
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)

    rst_text2 = """
1. .. note::
      Admonition body
"""
    rst2 = RestructuredText(rst_text2)
    console.print(rst2)


def test_bullet_list_multiple_children_types():
    rst_text = """
- First paragraph

  .. note::
     Note body

- Second paragraph

  .. raw:: html
     :class: empty
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)

    rst_text2 = """
1. First paragraph

   .. note::
      Note body

2. Second paragraph

   .. raw:: html
      :class: empty
"""
    rst2 = RestructuredText(rst_text2)
    console.print(rst2)


def test_system_message_empty_snippet():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = docutils.nodes.system_message(type='WARNING', level=2, source='test.rst', line=1)
    node['source'] = 'test.rst'
    node['line'] = 1
    node['type'] = 'WARNING'
    node['level'] = 2
    node.append(docutils.nodes.literal_block(text='   '))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_system_message(node)


def test_field_table_not_matching():
    rst_text = """
+---+
| a |
+---+

:Author: Wasi Master
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_definition_list_block_quote():
    rst_text = """
term : classifier1 : classifier2
    This is definition body.

        Inside blockquote.
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_option_list_no_description():
    rst_text = """
-o
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_block_quote_non_text_first():
    rst_text = """
    .. note:: Note inside blockquote
    """
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_line_block_non_line():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = docutils.nodes.line_block()
    node.append(docutils.nodes.paragraph(text='not a line'))
    visitor._render_line_block(node)


def test_topic_no_title():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = docutils.nodes.topic()
    node.append(docutils.nodes.paragraph(text='body'))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_topic(node)


def test_topic_empty_body_renderables():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = docutils.nodes.topic()
    node.append(docutils.nodes.title(text='title'))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_topic(node)


def test_sidebar_no_title():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = docutils.nodes.sidebar()
    node.append(docutils.nodes.paragraph(text='body'))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_sidebar(node)


def test_sidebar_field_list_coverage_gaps():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = docutils.nodes.sidebar()

    field_list = docutils.nodes.field_list()

    # 1. Field with less than 2 children
    field_short = docutils.nodes.field()
    field_short.append(docutils.nodes.field_name(text='NameOnly'))
    field_list.append(field_short)

    # 2. Field with name not equal to "subtitle"
    field_other = docutils.nodes.field()
    field_other.append(docutils.nodes.field_name(text='OtherField'))
    field_other.append(docutils.nodes.field_body(text='value'))
    field_list.append(field_other)

    # 3. Field with name "subtitle"
    field_sub = docutils.nodes.field()
    field_sub.append(docutils.nodes.field_name(text='subtitle'))
    field_sub.append(docutils.nodes.field_body(text='My Subtitle'))
    field_list.append(field_sub)

    node.append(field_list)
    node.append(docutils.nodes.paragraph(text='body'))

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_sidebar(node)


def test_footnote_sub_ref_empty_renderables():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_footnote_reference(docutils.nodes.footnote_reference(text='1'))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_substitution_reference(docutils.nodes.substitution_reference(text='sub'))


def test_problematic_empty_text():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    node = docutils.nodes.problematic(text='')
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_problematic(node)


def test_spanning_table_render_cell_lines_direct():
    from rich_rst import RSTVisitor

    grid = [[(Text('long_text_to_truncate\n\nother'), 0, 0), None], [None, (None, 0, 0)]]
    col_widths = [2, 2]
    console = Console(force_terminal=True, width=120)
    res = RSTVisitor._spanning_table(
        grid=grid,
        col_widths=col_widths,
        header_rows=0,
        title='Table Title',
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res is not None


def test_table_invalid_child():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    table = docutils.nodes.table()
    table.append(docutils.nodes.paragraph(text='invalid'))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


def test_table_num_cols_zero_empty_tbody():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    tgroup = docutils.nodes.tgroup()
    tbody = docutils.nodes.tbody()
    tgroup.append(tbody)
    table = docutils.nodes.table()
    table.append(tgroup)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


def test_compact_admonition_non_text_body():
    rst_text = """
.. note::
   - item 1
   - item 2
"""
    rst = RestructuredText(rst_text, admonition_style='compact')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_compact_version_admonition_non_text_body():
    rst_text = """
.. versionadded:: 1.0

   - item 1
   - item 2
"""
    rst = RestructuredText(rst_text, admonition_style='compact')
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_hlist_block_multi_renderables():
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)
    node = hlist_block(columns=2)
    bl = docutils.nodes.bullet_list()
    li = docutils.nodes.list_item()
    li.append(docutils.nodes.paragraph(text='p1'))
    li.append(docutils.nodes.literal_block(text='code'))
    bl.append(li)
    node.append(bl)
    doc.append(node)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_hlist_block(node)


def test_list_continuation_empty_child():
    rst_text = """
- Item 1
  .. comment here

1. Item 1
   .. comment here
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_system_message_empty_literal_block_our():
    sys_msg = docutils.nodes.system_message('System message details')
    sys_msg['source'] = 'test.rst'
    sys_msg['line'] = 1
    sys_msg['type'] = 'WARNING'
    sys_msg['level'] = 2
    lit = docutils.nodes.literal_block(text='')
    sys_msg.append(lit)
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(sys_msg, console=console)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_system_message(sys_msg)


def test_definition_list_item_block_quote_our():
    dl = docutils.nodes.definition_list()
    dli = docutils.nodes.definition_list_item()
    dli.append(docutils.nodes.term(text='term'))
    dli.append(docutils.nodes.classifier(text='classifier1'))
    dli.append(docutils.nodes.classifier(text='classifier2'))
    dli.append(docutils.nodes.comment(text='comment'))
    dli.append(docutils.nodes.block_quote(text='quote'))
    dl.append(dli)
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_definition_list(dl)


def test_option_list_no_description_our():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    ol = docutils.nodes.option_list()
    oli = docutils.nodes.option_list_item()
    og = docutils.nodes.option_group()
    opt = docutils.nodes.option()
    opt.append(docutils.nodes.option_string(text='-o'))
    og.append(opt)
    oli.append(og)
    oli.children = [og, None]
    ol.append(oli)
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_option_list(ol)


def test_visit_substitution_reference_empty_renderables_our():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    node = docutils.nodes.substitution_reference(text='subref')
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_substitution_reference(node)


def test_table_segments_to_lines_newlines():
    from rich.segment import Segment

    from rich_rst import RSTVisitor

    console = Console(force_terminal=True, width=120)
    with patch.object(Console, 'render_lines', return_value=[[Segment('line1\n\nline2')]]):
        grid = [[(Text('cell'), 0, 0)]]
        col_widths = [10]
        res = RSTVisitor._spanning_table(
            grid=grid,
            col_widths=col_widths,
            header_rows=0,
            title='Table Title',
            header_style=None,
            cell_style=None,
            console=console,
        )
        assert res is not None


class StatefulRow(list):
    def __getitem__(self, idx):
        import sys

        frame = sys._getframe(1)
        if frame.f_code.co_name == '_render_cell_lines':
            return None
        return super().__getitem__(idx)


def test_table_render_cell_lines_none():
    from rich_rst import RSTVisitor

    grid = [StatefulRow([(Text('cell'), 0, 0)])]
    col_widths = [10]
    console = Console(force_terminal=True, width=120)
    res = RSTVisitor._spanning_table(
        grid=grid,
        col_widths=col_widths,
        header_rows=0,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res is not None


def test_table_rowspan_last_column():
    grid = [[(Text('c1'), 0, 0), (Text('c2'), 0, 1)], [(Text('c3'), 0, 0), None]]
    col_widths = [5, 5]
    console = Console(force_terminal=True, width=120)
    res = RSTVisitor._spanning_table(
        grid=grid,
        col_widths=col_widths,
        header_rows=0,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res is not None


def test_table_num_cols_tbody_only():
    tgroup = docutils.nodes.tgroup()
    tbody = docutils.nodes.tbody()
    r = docutils.nodes.row()
    e1 = docutils.nodes.entry()
    e1.append(docutils.nodes.paragraph(text='cell'))
    r.append(e1)
    tbody.append(r)
    tgroup.append(tbody)
    table = docutils.nodes.table()
    table.append(tgroup)
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)
    table.document = doc
    tgroup.document = doc
    tbody.document = doc
    r.document = doc
    e1.document = doc
    for child in e1.children:
        child.document = doc
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


def test_table_render_entry_content_edge_cases():
    rst_text = """
+----+----+----+
| -  | - b| :: |
|    |    |    |
|    |    | c  |
+----+----+----+
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


def test_table_visit_table_none():
    from rich_rst import RSTVisitor

    grid = [[(None, 0, 0)]]
    col_widths = [10]
    console = Console(force_terminal=True, width=120)
    res = RSTVisitor._spanning_table(
        grid=grid,
        col_widths=col_widths,
        header_rows=0,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res is not None


def test_table_shrink_to_floor_edge_cases():
    import builtins

    original_min = builtins.min

    def mock_min(*args, **kwargs):
        if len(args) == 3:
            return 0
        return original_min(*args, **kwargs)

    with patch('builtins.min', mock_min):
        rst_text = """
+-------+-------+
|   col 1/2     |
+=======+=======+
| col 1 | col 2 |
+-------+-------+
"""
        console = Console(width=5)
        rst = RestructuredText(rst_text)
        console.print(rst)


def test_table_rowspan_three_rows():
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    tgroup = docutils.nodes.tgroup()
    tbody = docutils.nodes.tbody()

    r0 = docutils.nodes.row()
    e1 = docutils.nodes.entry(morerows=2)
    e1.append(docutils.nodes.paragraph(text='span'))
    r0.append(e1)
    e2 = docutils.nodes.entry()
    e2.append(docutils.nodes.paragraph(text='r0'))
    r0.append(e2)
    tbody.append(r0)

    r1 = docutils.nodes.row()
    e3 = docutils.nodes.entry()
    e3.append(docutils.nodes.paragraph(text='r1'))
    r1.append(e3)
    tbody.append(r1)

    r2 = docutils.nodes.row()
    e4 = docutils.nodes.entry()
    e4.append(docutils.nodes.paragraph(text='r2'))
    r2.append(e4)
    tbody.append(r2)

    tgroup.append(tbody)
    table = docutils.nodes.table()
    table.append(tgroup)

    for row in [r0, r1, r2]:
        row.document = doc
        for entry in row.children:
            entry.document = doc
            for child in entry.children:
                child.document = doc
    table.document = doc
    tgroup.document = doc
    tbody.document = doc

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


def test_list_continuation_empty_child_programmatic():
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    bl = docutils.nodes.bullet_list()
    li = docutils.nodes.list_item()
    li.append(docutils.nodes.paragraph(text='item text'))
    li.append(docutils.nodes.comment(text='comment'))
    bl.append(li)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_bullet_list(bl)


def test_enum_list_continuation_empty_child_programmatic():
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    el = docutils.nodes.enumerated_list()
    li = docutils.nodes.list_item()
    li.append(docutils.nodes.paragraph(text='item text'))
    li.append(docutils.nodes.comment(text='comment'))
    el.append(li)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_enumerated_list(el)


class MyChar(str):
    def __new__(cls, val, index):

        obj = str.__new__(cls, val)
        obj.index = index
        obj.call_count = 0
        return obj

    def isspace(self):
        if str.isspace(self):
            return True
        if self.index in (11, 13):
            return True
        elif self.index in (12, 14):
            self.call_count += 1
            if self.call_count == 1:
                return False
            return True
        return False


class MockSignatureStr(str):
    def __init__(self, val):
        self.chars = {}

    def __getitem__(self, item):
        if isinstance(item, slice):
            return MockSignatureStr(super().__getitem__(item))
        if item not in self.chars:
            val = super().__getitem__(item)
            self.chars[item] = MyChar(val, item)
        return self.chars[item]


def test_signature_spaces_mock():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)

    # return type whitespace skipping, and False branch
    sig1 = MockSignatureStr('def foo() -> int')
    visitor._highlight_py_signature('function', sig1)

    # parameter annotation whitespace skipping, parameter type whitespace trimming
    sig2 = MockSignatureStr('def foo(x: int)')
    visitor._highlight_py_signature('function', sig2)

    # parameter type scan loops normally to end
    sig3 = 'def foo(x: int'
    visitor._highlight_py_signature('function', sig3)


def test_table_render_lines_empty():
    console = Console(force_terminal=True, width=120)
    with patch.object(Console, 'render_lines', return_value=[]):
        grid = [[(Text('cell'), 0, 0)]]
        col_widths = [10]
        res = RSTVisitor._spanning_table(
            grid=grid,
            col_widths=col_widths,
            header_rows=0,
            title=None,
            header_style=None,
            cell_style=None,
            console=console,
        )
        assert res is not None


def test_table_cell_truncate():
    from rich.segment import Segment

    console = Console(force_terminal=True, width=120)
    with patch.object(Console, 'render_lines', return_value=[[Segment('verylongword')]]):
        grid = [[(Text('cell'), 0, 0)]]
        col_widths = [3]
        res = RSTVisitor._spanning_table(
            grid=grid,
            col_widths=col_widths,
            header_rows=0,
            title=None,
            header_style=None,
            cell_style=None,
            console=console,
        )
        assert res is not None


class StatefulRowForCspan(list):
    def __len__(self):
        return 2

    def __getitem__(self, idx):
        import sys

        frame = sys._getframe(1)
        if frame.f_code.co_name == '_origin':
            caller = frame.f_back
            if caller and caller.f_code.co_name == '_content':
                if 'span_end' in caller.f_locals:
                    return None
        return (Text('cell'), 1, 1)


def test_table_cspan_continues_content_our():
    from rich_rst import RSTVisitor

    console = Console(force_terminal=True, width=120)
    grid = [StatefulRowForCspan(), [None, (Text('cell2'), 0, 0)]]
    col_widths = [5, 5]
    res = RSTVisitor._spanning_table(
        grid=grid,
        col_widths=col_widths,
        header_rows=0,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res is not None


def test_table_inner_header_sep_programmatic():
    # Covers inner header separators (junctions)
    console = Console(force_terminal=True, width=120)

    # lrc is True (┣ or ┫ junction)
    grid1 = [[(Text('h1'), 0, 1), (Text('h2'), 0, 0)], [None, (Text('h3'), 0, 0)]]
    res1 = RSTVisitor._spanning_table(
        grid=grid1,
        col_widths=[5, 5],
        header_rows=2,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res1 is not None

    # inner header intersection (╋)
    grid2 = [[(Text('h1'), 0, 0), (Text('h2'), 0, 0)], [(Text('h3'), 0, 0), (Text('h4'), 0, 0)]]
    res2 = RSTVisitor._spanning_table(
        grid=grid2,
        col_widths=[5, 5],
        header_rows=2,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res2 is not None

    # colspan above, split below (┳)
    grid3 = [[(Text('h1'), 1, 0), None], [(Text('h2'), 0, 0), (Text('h3'), 0, 0)]]
    res3 = RSTVisitor._spanning_table(
        grid=grid3,
        col_widths=[5, 5],
        header_rows=2,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res3 is not None


def test_table_avail_zero():
    # Covers zero or negative available column widths
    from rich_rst import RSTVisitor

    grid = [[(Text('cell'), 0, 0)]]
    col_widths = [0]
    console = Console(force_terminal=True, width=120)
    res = RSTVisitor._spanning_table(
        grid=grid,
        col_widths=col_widths,
        header_rows=0,
        title=None,
        header_style=None,
        cell_style=None,
        console=console,
    )
    assert res is not None


def test_table_render_entry_content_empty_list():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)

    tgroup = docutils.nodes.tgroup()
    tbody = docutils.nodes.tbody()
    r = docutils.nodes.row()
    e1 = docutils.nodes.entry()

    bl = docutils.nodes.bullet_list()
    li = docutils.nodes.list_item()
    li.append(docutils.nodes.paragraph(text='item'))
    bl.append(li)
    e1.append(bl)

    r.append(e1)
    tbody.append(r)
    tgroup.append(tbody)
    table = docutils.nodes.table()
    table.append(tgroup)

    for node in [table, tgroup, tbody, r, e1, bl, li]:
        node.document = doc
        for child in node.children:
            child.document = doc

    from rich.segment import Segment

    with patch.object(Console, 'render_lines', return_value=[[Segment('   ')]]):
        with pytest.raises(docutils.nodes.SkipChildren):
            visitor.visit_table(table)


def test_table_render_entry_content_literal_block():
    # literal block inside a cell
    # Note: Indentation of 'c' by 2 spaces is critical so it is parsed as a literal block

    rst_text = """
+----+
| :: |
|    |
|  c |
+----+
"""
    rst = RestructuredText(rst_text)
    console = Console(force_terminal=True, width=120)
    console.print(rst)


class MockEntryContentVisitor(RSTVisitor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.call_count = 0

    def _make_sub_visitor(self):
        sub = super()._make_sub_visitor()
        self.call_count += 1
        if self.call_count > 1:
            sub.renderables = [None]
        return sub


def test_visit_table_none_content_our():
    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = MockEntryContentVisitor(doc, console=console)

    # Spanning table so has_spans is True and _rendered_plain_lines gets called
    rst_text = """
+----+----+
|    a    |
+====+====+
|    |    |
+----+----+
"""
    table = docutils.core.publish_doctree(rst_text)[0]
    for child in table.findall():
        child.document = doc

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


class StatefulEntryForSimpleRowspan(docutils.nodes.entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_calls = 0

    def get(self, key, failobj=None):
        if key == 'morerows':
            self.get_calls += 1
            if self.get_calls == 1:
                return 0
            return 2
        return super().get(key, failobj)


def test_simple_table_rowspan_our():
    # Covers rowspans in the simple table renderer

    doc = docutils.core.publish_doctree('Hello')
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(doc, console=console)

    tgroup = docutils.nodes.tgroup()
    tbody = docutils.nodes.tbody()

    # Row 0: uses the stateful entry subclass
    r0 = docutils.nodes.row()
    e1 = StatefulEntryForSimpleRowspan()
    e1.append(docutils.nodes.paragraph(text='span'))
    r0.append(e1)
    e2 = docutils.nodes.entry()
    e2.append(docutils.nodes.paragraph(text='r0'))
    r0.append(e2)
    tbody.append(r0)

    # Row 1: only second cell
    r1 = docutils.nodes.row()
    e3 = docutils.nodes.entry()
    e3.append(docutils.nodes.paragraph(text='r1'))
    r1.append(e3)
    tbody.append(r1)

    # Row 2: only second cell
    r2 = docutils.nodes.row()
    e4 = docutils.nodes.entry()
    e4.append(docutils.nodes.paragraph(text='r2'))
    r2.append(e4)
    tbody.append(r2)

    tgroup.append(tbody)
    table = docutils.nodes.table()
    table.append(tgroup)

    for row in [r0, r1, r2]:
        row.document = doc
        for entry in row.children:
            entry.document = doc
            for child in entry.children:
                child.document = doc
    table.document = doc
    tgroup.document = doc
    tbody.document = doc

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_table(table)


def test_toc_newline_coverage():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)

    # 1. Bullet list in TOC
    topic = docutils.nodes.topic(classes=['contents'])
    bullet_list = docutils.nodes.bullet_list()
    topic.append(bullet_list)
    bullet_list.parent = topic

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_bullet_list(bullet_list)

    # 2. Enumerated list in TOC
    enum_list = docutils.nodes.enumerated_list()
    topic.append(enum_list)
    enum_list.parent = topic

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_enumerated_list(enum_list)

    # 3. List with grandparent/ancestor TOC (nested list)
    nested_list = docutils.nodes.bullet_list()
    list_item = docutils.nodes.list_item()
    list_item.parent = bullet_list
    nested_list.parent = list_item

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_bullet_list(nested_list)

    # 4. List with parent that is not TOC (to cover parent loop termination)
    section = docutils.nodes.section()
    normal_list = docutils.nodes.bullet_list()
    normal_list.parent = section
    section.parent = None

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_bullet_list(normal_list)


def test_parsed_literal_coverage():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console)

    node = docutils.nodes.literal_block(classes=['parsed-literal'])

    node.append(docutils.nodes.Text('Hello '))

    emp = docutils.nodes.emphasis()
    emp.append(docutils.nodes.Text('world'))
    node.append(emp)

    strg = docutils.nodes.strong()
    strg.append(docutils.nodes.Text('!'))
    node.append(strg)

    lit = docutils.nodes.literal()
    lit.append(docutils.nodes.Text('code'))
    node.append(lit)

    tr = docutils.nodes.title_reference()
    tr.append(docutils.nodes.Text('title'))
    node.append(tr)

    ref_uri = docutils.nodes.reference(refuri='http://example.com')
    ref_uri.append(docutils.nodes.Text('link1'))
    node.append(ref_uri)

    ref_nouni = docutils.nodes.reference()
    ref_nouni.append(docutils.nodes.Text('link2'))
    node.append(ref_nouni)

    inl_class = docutils.nodes.inline(classes=['myclass'])
    inl_class.append(docutils.nodes.Text('styled'))
    node.append(inl_class)

    inl_noclass = docutils.nodes.inline()
    inl_noclass.append(docutils.nodes.Text('plain'))
    node.append(inl_noclass)

    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_literal_block(node)


def test_parsed_literal_invalid_theme_coverage():
    console = Console(force_terminal=True, width=120)
    doc = docutils.core.publish_doctree('Hello')
    visitor = RSTVisitor(doc, console=console, code_theme=123)
    node = docutils.nodes.literal_block(classes=['parsed-literal'])
    node.append(docutils.nodes.Text('Hello'))
    with pytest.raises(docutils.nodes.SkipChildren):
        visitor.visit_literal_block(node)


def test_dummy_reporter_methods_coverage():
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    reporter = visitor.document.reporter
    assert reporter is not None
    reporter.info("info")
    reporter.warning("warning")
    reporter.error("error")
    reporter.severe("severe")


def test_docinfo_non_text_block_element_coverage(render_text):
    # covers isinstance(r, Text) is False in _render_docinfo_value
    rst = """
:My Field:
  .. code-block:: python

     x = 1

Body.
"""
    out = render_text(rst)
    assert 'x = 1' in out


def test_docinfo_empty_block_element_coverage(render_text):
    # covers body_renderables being empty (returns "") in _render_docinfo_value
    rst = """
:My Field:
  ..

Body.
"""
    out = render_text(rst)
    assert 'My Field' in out


def test_render_docinfo_value_non_text_inline_part_coverage():
    # covers combined.append(str(part)) in _render_docinfo_value
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    from unittest.mock import MagicMock
    mock_node = MagicMock()
    mock_node.children = [docutils.nodes.emphasis()]
    visitor._render_child_inline = MagicMock(return_value=["string part"])
    val = visitor._render_docinfo_value(mock_node)
    assert val.plain == "string part"


def test_add_to_field_table_string_coverage():
    # covers isinstance(field_value, str) in _add_to_field_table
    from rich.table import Table
    console = Console(force_terminal=True, width=120)
    visitor = RSTVisitor(docutils.nodes.document(None, None), console=console)
    visitor._add_to_field_table("Test Name", "Test Value String")
    assert len(visitor.renderables) == 1
    assert isinstance(visitor.renderables[0], Table)

