# Supported elements

## Details

| Type               | Amount | Meaning                                        |
| ------------------ | ------ | ---------------------------------------------- |
| All                | 97     |  |
| ⛔ Not Possible     | 3     | Not possible to implement in a console context |
| ✅ Implemented      | 63    | Supported                                      |
| 📰 No Documentation | 22    | Not enough available information to implement  |
| ❌ Not Implemented  | 12    | Not implemented                                |

## Element List

| Index | Item                                                                                                     |       Supported?       |
| :---: | :------------------------------------------------------------------------------------------------------- | :--------------------: |
|   1   | [abbreviation](https://docutils.sourceforge.io/docs/ref/doctree.html#abbreviation)                       |   ⛔ Not Possible[^1]   |
|   2   | [acronym](https://docutils.sourceforge.io/docs/ref/doctree.html#acronym)                                 |   ⛔ Not Possible[^1]   |
|   3   | [address](https://docutils.sourceforge.io/docs/ref/doctree.html#address)                                 |         ✅ Yes          |
|   4   | [admonition](https://docutils.sourceforge.io/docs/ref/doctree.html#admonition)                           |         ✅ Yes          |
|   5   | [attention](https://docutils.sourceforge.io/docs/ref/doctree.html#attention)                             |         ✅ Yes          |
|   6   | [attribution](https://docutils.sourceforge.io/docs/ref/doctree.html#attribution)                         |   📰 No Documentation   |
|   7   | [author](https://docutils.sourceforge.io/docs/ref/doctree.html#author)                                   |         ✅ Yes          |
|   8   | [authors](https://docutils.sourceforge.io/docs/ref/doctree.html#authors)                                 |         ✅ Yes          |
|   9   | [block-quote](https://docutils.sourceforge.io/docs/ref/doctree.html#block-quote)                         |         ✅ Yes          |
|  10   | [bullet-list](https://docutils.sourceforge.io/docs/ref/doctree.html#bullet-list)                         |       ✅ Yes[^2]        |
|  11   | [caption](https://docutils.sourceforge.io/docs/ref/doctree.html#caption)                                 |   📰 No Documentation   |
|  12   | [caution](https://docutils.sourceforge.io/docs/ref/doctree.html#caution)                                 |         ✅ Yes          |
|  13   | [citation](https://docutils.sourceforge.io/docs/ref/doctree.html#citation)                               |   📰 No Documentation   |
|  14   | [citation-reference](https://docutils.sourceforge.io/docs/ref/doctree.html#citation-reference)           |   📰 No Documentation   |
|  15   | [classifier](https://docutils.sourceforge.io/docs/ref/doctree.html#classifier)                           |         ✅ Yes          |
|  16   | [colspec](https://docutils.sourceforge.io/docs/ref/doctree.html#colspec)                                 |   📰 No Documentation   |
|  17   | [comment](https://docutils.sourceforge.io/docs/ref/doctree.html#comment)                                 |         ✅ Yes          |
|  18   | [compound](https://docutils.sourceforge.io/docs/ref/doctree.html#compound)                               |          ❌ No          |
|  19   | [contact](https://docutils.sourceforge.io/docs/ref/doctree.html#contact)                                 |         ✅ Yes          |
|  20   | [container](https://docutils.sourceforge.io/docs/ref/doctree.html#container)                             |   📰 No Documentation   |
|  21   | [copyright](https://docutils.sourceforge.io/docs/ref/doctree.html#copyright)                             |         ✅ Yes          |
|  22   | [danger](https://docutils.sourceforge.io/docs/ref/doctree.html#danger)                                   |         ✅ Yes          |
|  23   | [date](https://docutils.sourceforge.io/docs/ref/doctree.html#date)                                       |         ✅ Yes          |
|  24   | [decoration](https://docutils.sourceforge.io/docs/ref/doctree.html#decoration)                           |   📰 No Documentation   |
|  25   | [definition](https://docutils.sourceforge.io/docs/ref/doctree.html#definition)                           |         ✅ Yes          |
|  26   | [definition-list](https://docutils.sourceforge.io/docs/ref/doctree.html#definition-list)                 |         ✅ Yes          |
|  27   | [definition-list-item](https://docutils.sourceforge.io/docs/ref/doctree.html#definition-list-item)       |         ✅ Yes          |
|  28   | [description](https://docutils.sourceforge.io/docs/ref/doctree.html#description)                         |         ✅ Yes          |
|  29   | [docinfo](https://docutils.sourceforge.io/docs/ref/doctree.html#docinfo)                                 |         ✅ Yes          |
|  30   | [doctest-block](https://docutils.sourceforge.io/docs/ref/doctree.html#doctest-block)                     |         ✅ Yes          |
|  31   | [document](https://docutils.sourceforge.io/docs/ref/doctree.html#document)                               |         ✅ Yes          |
|  32   | [emphasis](https://docutils.sourceforge.io/docs/ref/doctree.html#emphasis)                               |         ✅ Yes          |
|  33   | [entry](https://docutils.sourceforge.io/docs/ref/doctree.html#entry)                                     |   📰 No Documentation   |
|  34   | [enumerated-list](https://docutils.sourceforge.io/docs/ref/doctree.html#enumerated-list)                 |       ✅ Yes[^3]        |
|  35   | [error](https://docutils.sourceforge.io/docs/ref/doctree.html#error)                                     |         ✅ Yes          |
|  36   | [field](https://docutils.sourceforge.io/docs/ref/doctree.html#field)                                     |         ✅ Yes          |
|  37   | [field-body](https://docutils.sourceforge.io/docs/ref/doctree.html#field-body)                           |         ✅ Yes          |
|  38   | [field-list](https://docutils.sourceforge.io/docs/ref/doctree.html#field-list)                           |         ✅ Yes          |
|  39   | [field-name](https://docutils.sourceforge.io/docs/ref/doctree.html#field-name)                           |         ✅ Yes          |
|  40   | [figure](https://docutils.sourceforge.io/docs/ref/doctree.html#figure)                                   |   📰 No Documentation   |
|  41   | [footer](https://docutils.sourceforge.io/docs/ref/doctree.html#footer)                                   | ❌ No (help needed[^4]) |
|  42   | [footnote](https://docutils.sourceforge.io/docs/ref/doctree.html#footnote)                               | ❌ No (help needed[^4]) |
|  43   | [footnote-reference](https://docutils.sourceforge.io/docs/ref/doctree.html#footnote-reference)           | ❌ No (help needed[^4]) |
|  44   | [generated](https://docutils.sourceforge.io/docs/ref/doctree.html#generated)                             |   📰 No Documentation   |
|  45   | [header](https://docutils.sourceforge.io/docs/ref/doctree.html#header)                                   | ❌ No (help needed[^4]) |
|  46   | [hint](https://docutils.sourceforge.io/docs/ref/doctree.html#hint)                                       |         ✅ Yes          |
|  47   | [image](https://docutils.sourceforge.io/docs/ref/doctree.html#image)                                     |       ✅ Yes[^5]        |
|  48   | [important](https://docutils.sourceforge.io/docs/ref/doctree.html#important)                             |         ✅ Yes          |
|  49   | [inline](https://docutils.sourceforge.io/docs/ref/doctree.html#inline)                                   |          ❌ No          |
|  50   | [label](https://docutils.sourceforge.io/docs/ref/doctree.html#label)                                     |   📰 No Documentation   |
|  51   | [legend](https://docutils.sourceforge.io/docs/ref/doctree.html#legend)                                   |   📰 No Documentation   |
|  52   | [line](https://docutils.sourceforge.io/docs/ref/doctree.html#line)                                       |         ✅ Yes          |
|  53   | [line-block](https://docutils.sourceforge.io/docs/ref/doctree.html#line-block)                           |         ✅ Yes          |
|  54   | [list-item](https://docutils.sourceforge.io/docs/ref/doctree.html#list-item)                             |         ✅ Yes          |
|  55   | [literal](https://docutils.sourceforge.io/docs/ref/doctree.html#literal)                                 |         ✅ Yes          |
|  56   | [literal-block](https://docutils.sourceforge.io/docs/ref/doctree.html#literal-block)                     |         ✅ Yes          |
|  57   | [math](https://docutils.sourceforge.io/docs/ref/doctree.html#math)                                       |        ❌ No[^6]        |
|  58   | [math-block](https://docutils.sourceforge.io/docs/ref/doctree.html#math-block)                           |        ❌ No[^6]        |
|  59   | [meta](https://docutils.sourceforge.io/docs/ref/doctree.html#meta)                                       |         ✅ Yes          |
|  60   | [note](https://docutils.sourceforge.io/docs/ref/doctree.html#note)                                       |         ✅ Yes          |
|  61   | [option](https://docutils.sourceforge.io/docs/ref/doctree.html#option)                                   |         ✅ Yes          |
|  62   | [option-argument](https://docutils.sourceforge.io/docs/ref/doctree.html#option-argument)                 |         ✅ Yes          |
|  63   | [option-group](https://docutils.sourceforge.io/docs/ref/doctree.html#option-group)                       |         ✅ Yes          |
|  64   | [option-list](https://docutils.sourceforge.io/docs/ref/doctree.html#option-list)                         |         ✅ Yes          |
|  65   | [option-list-item](https://docutils.sourceforge.io/docs/ref/doctree.html#option-list-item)               |         ✅ Yes          |
|  66   | [option-string](https://docutils.sourceforge.io/docs/ref/doctree.html#option-string)                     |         ✅ Yes          |
|  67   | [organization](https://docutils.sourceforge.io/docs/ref/doctree.html#organization)                       |         ✅ Yes          |
|  68   | [paragraph](https://docutils.sourceforge.io/docs/ref/doctree.html#paragraph)                             |         ✅ Yes          |
|  69   | [pending](https://docutils.sourceforge.io/docs/ref/doctree.html#pending)                                 |   📰 No Documentation   |
|  70   | [problematic](https://docutils.sourceforge.io/docs/ref/doctree.html#problematic)                         |   📰 No Documentation   |
|  71   | [raw](https://docutils.sourceforge.io/docs/ref/doctree.html#raw)                                         |   📰 No Documentation   |
|  72   | [reference](https://docutils.sourceforge.io/docs/ref/doctree.html#reference)                             |   📰 No Documentation   |
|  73   | [revision](https://docutils.sourceforge.io/docs/ref/doctree.html#revision)                               |         ✅ Yes          |
|  74   | [row](https://docutils.sourceforge.io/docs/ref/doctree.html#row)                                         |   📰 No Documentation   |
|  75   | [rubric](https://docutils.sourceforge.io/docs/ref/doctree.html#rubric)                                   |   📰 No Documentation   |
|  76   | [section](https://docutils.sourceforge.io/docs/ref/doctree.html#section)                                 |         ✅ Yes          |
|  77   | [sidebar](https://docutils.sourceforge.io/docs/ref/doctree.html#sidebar)                                 |         ✅ Yes          |
|  78   | [status](https://docutils.sourceforge.io/docs/ref/doctree.html#status)                                   |         ✅ Yes          |
|  79   | [strong](https://docutils.sourceforge.io/docs/ref/doctree.html#strong)                                   |         ✅ Yes          |
|  80   | [subscript](https://docutils.sourceforge.io/docs/ref/doctree.html#subscript)                             |         ✅ Yes          |
|  81   | [substitution-definition](https://docutils.sourceforge.io/docs/ref/doctree.html#substitution-definition) |   📰 No Documentation   |
|  82   | [substitution-reference](https://docutils.sourceforge.io/docs/ref/doctree.html#substitution-reference)   |   📰 No Documentation   |
|  83   | [subtitle](https://docutils.sourceforge.io/docs/ref/doctree.html#subtitle)                               |         ✅ Yes          |
|  84   | [superscript](https://docutils.sourceforge.io/docs/ref/doctree.html#superscript)                         |         ✅ Yes          |
|  85   | [system-message](https://docutils.sourceforge.io/docs/ref/doctree.html#system-message)                   |         ✅ Yes          |
|  86   | [table](https://docutils.sourceforge.io/docs/ref/doctree.html#table)                                     |          ❌ No          |
|  87   | [target](https://docutils.sourceforge.io/docs/ref/doctree.html#target)                                   |   📰 No Documentation   |
|  88   | [tbody](https://docutils.sourceforge.io/docs/ref/doctree.html#tbody)                                     |          ❌ No          |
|  89   | [term](https://docutils.sourceforge.io/docs/ref/doctree.html#term)                                       |         ✅ Yes          |
|  90   | [tgroup](https://docutils.sourceforge.io/docs/ref/doctree.html#tgroup)                                   |          ❌ No          |
|  91   | [thead](https://docutils.sourceforge.io/docs/ref/doctree.html#thead)                                     |          ❌ No          |
|  92   | [tip](https://docutils.sourceforge.io/docs/ref/doctree.html#tip)                                         |         ✅ Yes          |
|  93   | [title](https://docutils.sourceforge.io/docs/ref/doctree.html#title)                                     |         ✅ Yes          |
|  94   | [title-reference](https://docutils.sourceforge.io/docs/ref/doctree.html#title-reference)                 |   📰 No Documentation   |
|  95   | [topic](https://docutils.sourceforge.io/docs/ref/doctree.html#topic)                                     |         ✅ Yes          |
|  96   | [transition](https://docutils.sourceforge.io/docs/ref/doctree.html#transition)                           |         ✅ Yes          |
|  97   | [version](https://docutils.sourceforge.io/docs/ref/doctree.html#version)                                 |         ✅ Yes          |
|  98   | [warning](https://docutils.sourceforge.io/docs/ref/doctree.html#warning)                                 |         ✅ Yes          |

[^1]: Abbreviation and acronym elements work when hovering over some text, since in a terminal we can't change the hover text (as far as I know), those are not supported
[^2]: Bullet lists are supported for up to 3 levels of nesting
[^3]: Enumerated lists are supported without nesting
[^4]: Currently the document is rendered top to bottom and I don't really know any method of adding a element at the end or at the beginning and keeping that order, any suggestions appreciated
[^5]: Images show an emoji and the alt text or title text (aka hover text) and they are clickable, if the image has a target link then it opens that target link when clicked, otherwise it opens the image url
[^6]: Math elements are really hard to implement since they require a lot of logic and code. And with restructuredtext math isn't really used that much so I don't want to implement them
