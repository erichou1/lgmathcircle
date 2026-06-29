/* ==========================================================================
   Los Gatos Math Circle: shared behavior
   - Mobile nav
   - Footer year
   - Newsletter signup (front-end only confirmation)
   - Newsletter archive + recent issues
   - Single issue rendering (reads ?slug= ; math typeset by MathJax)
   ========================================================================== */

(function () {
  "use strict";

  function initNav() {
    var toggle = document.querySelector(".nav__toggle");
    var links = document.querySelector(".nav__links");
    if (!toggle || !links) return;
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  function initYear() {
    document.querySelectorAll("[data-year]").forEach(function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }

  /* Forms that confirm in place, no backend. Replace each form's `action`
     with your provider (newsletter service, form endpoint, etc.) to go live.
     Works for newsletter signups (.signup) and the team application (.form). */
  function initForms() {
    document.querySelectorAll("form[data-confirm]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!form.checkValidity()) {
          form.reportValidity();
          return;
        }
        var box = form.closest(".signup, .form") || form.parentElement;
        if (box) box.classList.add("is-done");
        try { form.reset(); } catch (_) {}
      });
    });
  }

  function formatDate(iso) {
    var d = new Date(iso + "T00:00:00");
    if (isNaN(d)) return iso;
    return d.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });
  }

  function fmtCount(n) {
    if (n == null) return "";
    if (n >= 1000) return (n / 1000).toFixed(1).replace(/\.0$/, "") + "k";
    return String(n);
  }

  var ICON_EYE =
    '<svg class="stat-ic" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="M1.5 12S5.5 5 12 5s10.5 7 10.5 7-4 7-10.5 7S1.5 12 1.5 12z" fill="none" stroke="currentColor" stroke-width="1.7"/>' +
    '<circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>';
  var ICON_HEART =
    '<svg class="stat-ic" viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="M12 20.6l-1.6-1.45C5.1 14.36 2 11.6 2 8.25 2 5.5 4.2 3.3 7 3.3c1.6 0 3.13.74 4.13 1.92.13.16.37.16.5 0C12.63 4.04 14.17 3.3 15.77 3.3c2.8 0 5 2.2 5 4.95 0 3.35-3.1 6.11-8.4 10.9L12 20.6z" ' +
    'fill="var(--heart-fill, none)" stroke="currentColor" stroke-width="1.7"/></svg>';

  function likeKey(slug) { return "lgmc-like-" + slug; }
  function isLiked(slug) {
    try { return localStorage.getItem(likeKey(slug)) === "1"; } catch (e) { return false; }
  }

  function statsHtml(it, interactive) {
    if (it.views == null) return "";
    var liked = isLiked(it.slug);
    var likeN = (it.likes || 0) + (liked ? 1 : 0);
    var views =
      '<span class="stat" title="' + it.views + ' views">' + ICON_EYE +
      "<span>" + fmtCount(it.views) + "</span></span>";
    var likes;
    if (interactive) {
      likes =
        '<button type="button" class="stat stat--like' + (liked ? " is-liked" : "") +
        '" data-like="' + escapeHtml(it.slug) + '" aria-pressed="' + (liked ? "true" : "false") +
        '" aria-label="Like this issue">' + ICON_HEART +
        '<span data-like-count>' + fmtCount(likeN) + "</span></button>";
    } else {
      likes =
        '<span class="stat' + (liked ? " is-liked" : "") + '" title="' + likeN + ' likes">' +
        ICON_HEART + "<span>" + fmtCount(likeN) + "</span></span>";
    }
    return '<span class="issue-stats">' + views + likes + "</span>";
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function sortedIssues() {
    var list = (window.ISSUES || []).slice();
    list.sort(function (a, b) { return new Date(b.date) - new Date(a.date); });
    return list;
  }

  function issueCard(it) {
    var href = "issue.html?slug=" + encodeURIComponent(it.slug);
    var num = it.number != null ? "Issue " + String(it.number).padStart(2, "0") + " · " : "";
    return (
      '<article class="issue">' +
      '<a class="issue__media" href="' + href + '">' +
      '<img src="' + escapeHtml(it.image) + '" alt="' + escapeHtml(it.alt || "") + '" loading="lazy">' +
      "</a>" +
      '<div class="issue__meta">' + num + formatDate(it.date) + "</div>" +
      (it.views != null ? '<div class="issue__stats">' + statsHtml(it, false) + "</div>" : "") +
      '<h3><a href="' + href + '">' + escapeHtml(it.title) + "</a></h3>" +
      "<p>" + escapeHtml(it.excerpt) + "</p>" +
      '<a class="arrow-link" href="' + href + '">Read issue &rarr;</a>' +
      "</article>"
    );
  }

  function initArchive() {
    var grid = document.querySelector("[data-issue-grid]");
    if (!grid) return;
    grid.innerHTML = sortedIssues().map(issueCard).join("");
  }

  function initRecent() {
    var grid = document.querySelector("[data-recent-issues]");
    if (!grid) return;
    var n = parseInt(grid.getAttribute("data-recent-issues"), 10) || 3;
    grid.innerHTML = sortedIssues().slice(0, n).map(issueCard).join("");
  }

  function getParam(name) {
    return new URLSearchParams(window.location.search).get(name);
  }

  function initIssue() {
    var root = document.querySelector("[data-issue]");
    if (!root) return;

    var issues = sortedIssues();
    var slug = getParam("slug");
    var it = issues.find(function (p) { return p.slug === slug; });

    var kicker = document.querySelector("[data-issue-kicker]");
    var titleEl = document.querySelector("[data-issue-title]");
    var byline = document.querySelector("[data-issue-byline]");
    var coverEl = document.querySelector("[data-issue-cover]");
    var bodyEl = document.querySelector("[data-issue-body]");
    var navEl = document.querySelector("[data-issue-nav]");

    if (!it) {
      if (titleEl) titleEl.textContent = "Issue not found";
      if (bodyEl) bodyEl.innerHTML = '<p>Sorry, that issue does not exist. <a href="newsletter.html">Back to the newsletter</a>.</p>';
      return;
    }

    document.title = it.title + " · Los Gatos Math Circle";
    if (kicker) kicker.textContent = (it.number != null ? "Issue " + String(it.number).padStart(2, "0") + " · " : "") + formatDate(it.date);
    if (titleEl) titleEl.textContent = it.title;
    if (byline) {
      byline.innerHTML = statsHtml(it, true);
      var likeBtn = byline.querySelector("[data-like]");
      if (likeBtn) {
        likeBtn.addEventListener("click", function () {
          var liked = isLiked(it.slug);
          try { localStorage.setItem(likeKey(it.slug), liked ? "0" : "1"); } catch (e) {}
          var now = !liked;
          likeBtn.classList.toggle("is-liked", now);
          likeBtn.setAttribute("aria-pressed", now ? "true" : "false");
          var cnt = likeBtn.querySelector("[data-like-count]");
          if (cnt) cnt.textContent = fmtCount((it.likes || 0) + (now ? 1 : 0));
        });
      }
    }
    if (coverEl && it.image) {
      coverEl.innerHTML = '<div class="frame"><img src="' + escapeHtml(it.image) + '" alt="' + escapeHtml(it.alt || "") + '"></div>';
    }
    if (bodyEl) bodyEl.innerHTML = it.body;

    if (navEl) {
      var idx = issues.indexOf(it);
      var older = issues[idx + 1];
      var newer = issues[idx - 1];
      var html = older
        ? '<a class="arrow-link" href="issue.html?slug=' + encodeURIComponent(older.slug) + '">&larr; ' + escapeHtml(older.title) + "</a>"
        : "<span></span>";
      html += newer
        ? '<a class="arrow-link" href="issue.html?slug=' + encodeURIComponent(newer.slug) + '">' + escapeHtml(newer.title) + " &rarr;</a>"
        : "<span></span>";
      navEl.innerHTML = html;
    }

    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise();
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNav();
    initYear();
    initForms();
    initArchive();
    initRecent();
    initIssue();
  });
})();
