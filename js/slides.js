/* ==========================================================================
   Los Gatos Math Circle. Presentations: schedule index + slide-deck viewer.
   Reads window.SCHEDULE and window.MODULES from js/meetings.js.
   ========================================================================== */
(function () {
  "use strict";

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function shortDate(label) {
    // "Sat, Sep 9, 2023" -> "Sep 9, 2023"
    var i = label.indexOf(", ");
    return i >= 0 ? label.slice(i + 2) : label;
  }
  function typeset() {
    if (window.MathJax && window.MathJax.typesetPromise) window.MathJax.typesetPromise();
  }

  /* ---------- Schedule index (presentations.html) ---------- */
  function initSchedule() {
    var root = document.querySelector("[data-schedule]");
    if (!root || !window.SCHEDULE) return;
    var html = "";
    window.SCHEDULE.forEach(function (yr) {
      var meetings = yr.meetings.filter(function (m) { return m.type === "meeting"; });
      var first = meetings[0], last = meetings[meetings.length - 1];
      html += '<section class="year-block">';
      html += '<div class="year-head"><h2>' + esc(yr.year) + " school year</h2>" +
        '<span class="yr-meta">' + meetings.length + " meetings · " +
        esc(shortDate(first.label)) + " to " + esc(shortDate(last.label)) + "</span></div>";
      yr.meetings.forEach(function (m) {
        if (m.type === "break") {
          html += '<div class="sched-row sched-row--break">' +
            '<span class="sr-n"></span>' +
            '<span class="sr-date">' + esc(shortDate(m.label)) + "</span>" +
            '<span class="sr-break">' + esc(m.brk) + ", no meeting</span></div>";
        } else if (m.type === "cancelled") {
          html += '<div class="sched-row sched-row--break sched-row--cancelled">' +
            '<span class="sr-n"></span>' +
            '<span class="sr-date">' + esc(shortDate(m.label)) + "</span>" +
            '<span class="sr-break">' + esc(m.brk) + "</span></div>";
        } else {
          html += '<div class="sched-row">' +
            '<span class="sr-n">' + m.n + "</span>" +
            '<span class="sr-date">' + esc(shortDate(m.label)) + "</span>" +
            '<span class="sr-title">' + esc(m.title) +
            '<span class="sr-topic">' + esc(m.topic) + "</span></span>" +
            '<a class="sr-link" href="slides.html?d=' + encodeURIComponent(m.date) +
            '">View slides &rarr;</a></div>';
        }
      });
      html += "</section>";
    });
    root.innerHTML = html;
  }

  /* ---------- Slide deck viewer (slides.html) ---------- */
  function findMeeting(date) {
    var res = null;
    (window.SCHEDULE || []).forEach(function (yr) {
      yr.meetings.forEach(function (m) {
        if (m.type === "meeting" && m.date === date) res = { m: m, year: yr.year };
      });
    });
    return res;
  }

  function initDeck() {
    var root = document.querySelector("[data-deck]");
    if (!root) return;

    var date = new URLSearchParams(window.location.search).get("d");
    var hit = findMeeting(date);
    var stage = document.querySelector("[data-stage]");
    var metaEl = document.querySelector("[data-deck-meta]");

    if (!hit || !window.MODULES[hit.m.module]) {
      if (stage) stage.innerHTML = '<div class="slide is-active"><div class="slide__body">' +
        "<p>Sorry, that meeting could not be found. " +
        '<a href="presentations.html">Back to the schedule</a>.</p></div></div>';
      return;
    }

    var m = hit.m, mod = window.MODULES[m.module];
    document.title = mod.t + " · Slides · Los Gatos Math Circle";
    if (metaEl) metaEl.textContent = hit.year + " · Meeting " + m.n + " · " + shortDate(m.label);

    // Build slides: a title slide, then the module's slides.
    var slides = [];
    slides.push(
      '<section class="slide slide--title">' +
      '<div class="slide__kicker">Los Gatos Math Circle</div>' +
      "<h1>" + esc(mod.t) + "</h1>" +
      '<div><span class="st-topic">' + esc(mod.topic) + "</span></div>" +
      '<div class="st-date">' + esc(m.label) + " · Meeting " + m.n + "</div>" +
      "</section>"
    );
    mod.s.forEach(function (slide, i) {
      var head = slide[0], body = slide[1], img = slide[2], cap = slide[3];
      var cls = "slide";
      var inner = '<div class="slide__kicker">' + (i + 1) + " / " + mod.s.length + "</div>";
      if (img && body) {
        // Text + image side by side.
        cls += " slide--split";
        inner +=
          '<div class="slide__cols">' +
          '<div class="slide__text">' +
          (head ? "<h2>" + esc(head) + "</h2>" : "") +
          '<div class="slide__body">' + body + "</div></div>" +
          '<figure class="slide__media"><img src="' + esc(img) + '" alt="' + esc(cap || head || "") + '" />' +
          (cap ? '<figcaption>' + esc(cap) + "</figcaption>" : "") +
          "</figure></div>";
      } else if (img) {
        // Full image slide with a caption heading.
        cls += " slide--photo";
        inner +=
          (head ? "<h2>" + esc(head) + "</h2>" : "") +
          '<figure class="slide__media slide__media--wide"><img src="' + esc(img) + '" alt="' + esc(cap || head || "") + '" />' +
          (cap ? '<figcaption>' + esc(cap) + "</figcaption>" : "") +
          "</figure>";
      } else {
        inner += "<h2>" + esc(head) + "</h2>" + '<div class="slide__body">' + body + "</div>";
      }
      slides.push('<section class="' + cls + '">' + inner + "</section>");
    });

    stage.innerHTML = slides.join("");

    var slideEls = Array.prototype.slice.call(stage.querySelectorAll(".slide"));
    var dotsEl = document.querySelector("[data-dots]");
    var countEl = document.querySelector("[data-count]");
    var prevBtn = document.querySelector("[data-prev]");
    var nextBtn = document.querySelector("[data-next]");
    var idx = 0;

    if (dotsEl) {
      dotsEl.innerHTML = slideEls.map(function (_, i) {
        return '<button class="deck-dot" data-go="' + i + '" aria-label="Slide ' + (i + 1) + '"></button>';
      }).join("");
    }

    function show(n) {
      idx = Math.max(0, Math.min(slideEls.length - 1, n));
      slideEls.forEach(function (el, i) { el.classList.toggle("is-active", i === idx); });
      if (dotsEl) {
        Array.prototype.forEach.call(dotsEl.children, function (d, i) {
          d.classList.toggle("is-on", i === idx);
        });
      }
      if (countEl) countEl.textContent = (idx + 1) + " / " + slideEls.length;
      if (prevBtn) prevBtn.disabled = idx === 0;
      if (nextBtn) nextBtn.disabled = idx === slideEls.length - 1;
    }

    if (prevBtn) prevBtn.addEventListener("click", function () { show(idx - 1); });
    if (nextBtn) nextBtn.addEventListener("click", function () { show(idx + 1); });
    if (dotsEl) dotsEl.addEventListener("click", function (e) {
      var b = e.target.closest("[data-go]");
      if (b) show(parseInt(b.getAttribute("data-go"), 10));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight" || e.key === "PageDown" || e.key === " ") { e.preventDefault(); show(idx + 1); }
      else if (e.key === "ArrowLeft" || e.key === "PageUp") { e.preventDefault(); show(idx - 1); }
      else if (e.key === "Home") { show(0); }
      else if (e.key === "End") { show(slideEls.length - 1); }
    });

    show(0);
    typeset();

    // Prev / next meeting links across the whole schedule.
    var flat = [];
    (window.SCHEDULE || []).forEach(function (yr) {
      yr.meetings.forEach(function (mm) { if (mm.type === "meeting") flat.push(mm); });
    });
    var pos = flat.findIndex(function (mm) { return mm.date === date; });
    var navEl = document.querySelector("[data-deck-nav]");
    if (navEl && pos >= 0) {
      var older = flat[pos - 1], newer = flat[pos + 1];
      var h = older
        ? '<a class="arrow-link" href="slides.html?d=' + encodeURIComponent(older.date) + '">&larr; ' + esc(older.title) + "</a>"
        : "<span></span>";
      h += newer
        ? '<a class="arrow-link" href="slides.html?d=' + encodeURIComponent(newer.date) + '">' + esc(newer.title) + " &rarr;</a>"
        : "<span></span>";
      navEl.innerHTML = h;
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initSchedule();
    initDeck();
  });
})();
