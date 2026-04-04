/**
 * rich-rst docs — custom interactivity
 *
 * Features:
 *  - Animate sections into view as the user scrolls (IntersectionObserver)
 *  - Smooth scroll for same-page anchor links
 *  - Add language label badges to code blocks
 *  - "Scroll to top" button
 */

(function () {
  "use strict";

  /* ------------------------------------------------------------------
     Intersection Observer — fade-in sections on scroll
  ------------------------------------------------------------------ */
  function initScrollAnimations() {
    const targets = document.querySelectorAll(
      "section, dl.py, table.docutils, .admonition, div.highlight"
    );

    if (!("IntersectionObserver" in window)) return;

    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("rr-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
    );

    targets.forEach(function (el) {
      el.classList.add("rr-animate");
      observer.observe(el);
    });
  }

  /* ------------------------------------------------------------------
     Code block language badges
  ------------------------------------------------------------------ */
  function addLanguageBadges() {
    var blocks = document.querySelectorAll("div[class*='highlight-']");
    blocks.forEach(function (block) {
      // Extract language from class like "highlight-python"
      var match = block.className.match(/highlight-(\w+)/);
      if (!match) return;
      var lang = match[1];
      if (lang === "default" || lang === "none") return;

      // Don't add duplicate badges
      if (block.querySelector(".rr-lang-badge")) return;

      var badge = document.createElement("span");
      badge.className = "rr-lang-badge";
      badge.textContent = lang;
      block.appendChild(badge);
    });
  }

  /* ------------------------------------------------------------------
     Scroll-to-top button
  ------------------------------------------------------------------ */
  function initScrollToTop() {
    var btn = document.createElement("button");
    btn.id = "rr-scroll-top";
    btn.setAttribute("aria-label", "Scroll to top");
    btn.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"' +
      ' stroke-linecap="round" stroke-linejoin="round" width="18" height="18">' +
      "<polyline points='18 15 12 9 6 15'></polyline></svg>";
    document.body.appendChild(btn);

    window.addEventListener(
      "scroll",
      function () {
        btn.classList.toggle("rr-scroll-top--visible", window.scrollY > 300);
      },
      { passive: true }
    );

    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ------------------------------------------------------------------
     Inject dynamic CSS for scroll-animation classes & scroll-to-top btn
  ------------------------------------------------------------------ */
  function injectDynamicStyles() {
    var style = document.createElement("style");
    style.textContent = [
      /* Scroll-in animation base state */
      ".rr-animate {",
      "  opacity: 0;",
      "  transform: translateY(16px);",
      "  transition: opacity 0.45s cubic-bezier(0.22,1,0.36,1),",
      "              transform 0.45s cubic-bezier(0.22,1,0.36,1);",
      "}",
      ".rr-animate.rr-visible {",
      "  opacity: 1;",
      "  transform: none;",
      "}",
      /* Language badge */
      ".rr-lang-badge {",
      "  position: absolute;",
      "  top: 10px;",
      "  right: 46px;",
      "  font-family: 'Google Sans', 'Inter', sans-serif;",
      "  font-size: 0.68rem;",
      "  font-weight: 600;",
      "  letter-spacing: 0.06em;",
      "  text-transform: uppercase;",
      "  color: var(--color-foreground-muted, #888);",
      "  pointer-events: none;",
      "  user-select: none;",
      "  z-index: 2;",
      "}",
      /* Scroll-to-top button */
      "#rr-scroll-top {",
      "  position: fixed;",
      "  bottom: 1.8rem;",
      "  right: 1.8rem;",
      "  width: 40px;",
      "  height: 40px;",
      "  border-radius: 50%;",
      "  border: none;",
      "  background: var(--color-brand-primary, #5B4FE9);",
      "  color: #fff;",
      "  cursor: pointer;",
      "  display: flex;",
      "  align-items: center;",
      "  justify-content: center;",
      "  box-shadow: 0 3px 12px rgba(91,79,233,0.35);",
      "  opacity: 0;",
      "  transform: translateY(10px) scale(0.9);",
      "  transition: opacity 0.25s ease, transform 0.25s ease, background-color 0.2s ease;",
      "  pointer-events: none;",
      "  z-index: 999;",
      "}",
      "#rr-scroll-top.rr-scroll-top--visible {",
      "  opacity: 1;",
      "  transform: none;",
      "  pointer-events: auto;",
      "}",
      "#rr-scroll-top:hover {",
      "  background: var(--color-brand-content, #8B5CF6);",
      "  transform: translateY(-2px) scale(1.05);",
      "}",
    ].join("\n");
    document.head.appendChild(style);
  }

  /* ------------------------------------------------------------------
     Initialise everything after DOM is ready
  ------------------------------------------------------------------ */
  function init() {
    injectDynamicStyles();
    initScrollAnimations();
    addLanguageBadges();
    initScrollToTop();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
