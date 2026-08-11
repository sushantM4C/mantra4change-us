/* Mantra4Change US — site behaviour.
   No framework, no build step. Everything degrades gracefully without JS. */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------- mobile nav */
  function initNav() {
    var toggle = $(".nav__toggle");
    var links  = $(".nav__links");
    if (!toggle || !links) return;

    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      links.setAttribute("data-open", String(!open));
    });

    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        toggle.setAttribute("aria-expanded", "false");
        links.setAttribute("data-open", "false");
      }
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        toggle.setAttribute("aria-expanded", "false");
        links.setAttribute("data-open", "false");
      }
    });
  }

  /* ------------------------------------------------------- scroll reveal */
  function initReveal() {
    var els = $$("[data-reveal]");
    if (!els.length) return;
    if (reduced || !("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseInt(el.getAttribute("data-reveal-delay") || "0", 10);
        setTimeout(function () { el.classList.add("is-in"); }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------------ counters */
  function formatNum(v, decimals) {
    return v.toLocaleString("en-US", {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    });
  }

  function runCount(el) {
    var target   = parseFloat(el.getAttribute("data-count"));
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
    var prefix   = el.getAttribute("data-prefix") || "";
    var suffix   = el.getAttribute("data-suffix") || "";
    if (isNaN(target)) return;

    if (reduced) { el.textContent = prefix + formatNum(target, decimals) + suffix; return; }

    var duration = 1500;
    var start = null;
    function frame(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);           // easeOutCubic
      el.textContent = prefix + formatNum(target * eased, decimals) + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  function initCounters() {
    var els = $$("[data-count]");
    if (!els.length) return;
    if (!("IntersectionObserver" in window)) { els.forEach(runCount); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        runCount(entry.target);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.4 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ----------------------------------------------------------- accordion */
  function initFaq() {
    $$(".faq__q").forEach(function (btn) {
      var panel = document.getElementById(btn.getAttribute("aria-controls"));
      if (!panel) return;

      btn.addEventListener("click", function () {
        var open = btn.getAttribute("aria-expanded") === "true";

        // close siblings within the same .faq group
        var group = btn.closest(".faq");
        if (group && !open) {
          $$(".faq__q[aria-expanded='true']", group).forEach(function (other) {
            var op = document.getElementById(other.getAttribute("aria-controls"));
            other.setAttribute("aria-expanded", "false");
            if (op) op.style.height = "0px";
          });
        }

        btn.setAttribute("aria-expanded", String(!open));
        panel.style.height = open ? "0px" : panel.scrollHeight + "px";
      });

      // keep an open panel correctly sized on resize
      window.addEventListener("resize", function () {
        if (btn.getAttribute("aria-expanded") === "true") {
          panel.style.height = panel.scrollHeight + "px";
        }
      });
    });
  }

  /* ---------------------------------------------------------------- tabs */
  function initTabs() {
    $$("[data-tabs]").forEach(function (group) {
      var tabs = $$(".tab", group);

      function select(tab) {
        tabs.forEach(function (t) {
          var on = t === tab;
          t.setAttribute("aria-selected", String(on));
          t.setAttribute("tabindex", on ? "0" : "-1");
          var panel = document.getElementById(t.getAttribute("aria-controls"));
          if (panel) panel.hidden = !on;
        });
      }

      tabs.forEach(function (tab, i) {
        tab.addEventListener("click", function () { select(tab); });
        tab.addEventListener("keydown", function (e) {
          var next = null;
          if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
          if (e.key === "ArrowLeft")  next = tabs[(i - 1 + tabs.length) % tabs.length];
          if (next) { e.preventDefault(); next.focus(); select(next); }
        });
      });
    });
  }

  /* ---------------------------------------------------------- india map */
  var ACCENTS = {
    navy: "#273f7d", sky: "#00b1ff", green: "#38c68b",
    amber: "#ffcb37", orange: "#f59a3d", steel: "#95b3d7"
  };

  function stateInfo(name) {
    if (typeof STATE_DATA === "undefined") return null;
    for (var i = 0; i < STATE_DATA.length; i++) {
      if (STATE_DATA[i].name === name) return STATE_DATA[i];
    }
    return null;
  }

  function buildMap(host) {
    if (typeof INDIA_MAP === "undefined") return null;
    var NS = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", INDIA_MAP.viewBox);
    svg.setAttribute("class", "map");
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", "Map of India showing the six states where Mantra4Change works");

    var order = 0;
    INDIA_MAP.states.forEach(function (s) {
      var path = document.createElementNS(NS, "path");
      path.setAttribute("d", s.d);
      path.setAttribute("class", "map__state" + (s.on ? " map__state--active" : ""));
      path.setAttribute("data-state", s.name);

      if (s.on) {
        var info = stateInfo(s.name);
        if (info && ACCENTS[info.accent]) path.style.fill = ACCENTS[info.accent];
        path.style.animationDelay = (order * 90) + "ms";
        order++;
      }
      svg.appendChild(path);
    });

    host.appendChild(svg);

    if (!reduced && host.hasAttribute("data-animate")) {
      svg.classList.add("map--animate");
      // A `forwards` animation outranks normal declarations in the cascade, which
      // would pin opacity at 1 and break the selection dimming. Drop the class
      // once the stagger has finished playing.
      setTimeout(function () { svg.classList.remove("map--animate"); }, order * 90 + 700);
    }
    return svg;
  }

  function renderInfo(panel, info) {
    if (!info) return;
    var rows = [
      ["schools",  "Schools reached"],
      ["leaders",  "Education leaders"],
      ["children", "Children reached"]
    ].map(function (r) {
      return '<div class="mapinfo__num"><b class="tnum">' + info[r[0]] + "</b><span>" + r[1] + "</span></div>";
    }).join("");

    panel.innerHTML =
      '<div class="mapinfo__name">' + info.name + "</div>" +
      '<div class="mapinfo__nums">' + rows + "</div>" +
      '<p class="mapinfo__note">' + info.note + "</p>" +
      (info.budget ? '<p class="small" style="margin-top:1rem;color:var(--muted)"><strong>' + info.budget + "</strong></p>" : "");
  }

  function initMaps() {
    $$("[data-map]").forEach(function (host) {
      var svg = buildMap(host);
      if (!svg || !host.hasAttribute("data-interactive")) return;

      var panel = $("[data-mapinfo]");
      var pills = $$("[data-statepill]");
      var paths = $$(".map__state--active", svg);

      function select(name) {
        svg.classList.add("map--haspick");
        paths.forEach(function (p) {
          p.setAttribute("data-selected", String(p.getAttribute("data-state") === name));
        });
        pills.forEach(function (b) {
          b.setAttribute("aria-pressed", String(b.getAttribute("data-statepill") === name));
        });
        if (panel) renderInfo(panel, stateInfo(name));
      }

      paths.forEach(function (p) {
        var name = p.getAttribute("data-state");
        p.setAttribute("tabindex", "0");
        p.setAttribute("role", "button");
        p.setAttribute("aria-label", name + " — view impact figures");
        p.addEventListener("click", function () { select(name); });
        p.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(name); }
        });
      });

      pills.forEach(function (b) {
        b.addEventListener("click", function () { select(b.getAttribute("data-statepill")); });
      });

      select(host.getAttribute("data-default") || "Bihar");
    });
  }

  /* ------------------------------------------------ photos with fallback */
  /* Photos are optional. Each slot renders a designed placeholder and swaps in
     the real image only once it has actually loaded, so a missing file never
     shows a broken-image icon. */
  function tryPhoto(src, onload, onfail) {
    var img = new Image();
    img.onload = function () { onload(img); };
    img.onerror = onfail || function () {};
    img.src = src;
  }

  function initFigures() {
    $$("[data-photo]").forEach(function (fig) {
      var src = fig.getAttribute("data-photo");
      var slot = $(".figure__slot", fig);
      tryPhoto(src, function () {
        var el = document.createElement("img");
        el.className = "figure__img";
        el.src = src;
        el.alt = fig.getAttribute("data-alt") || "";
        if (slot) slot.replaceWith(el); else fig.appendChild(el);
      });
    });
  }

  /* --------------------------------------------------------- board + bio */
  function initials(name) {
    return name.split(/\s+/).filter(Boolean).map(function (w) { return w[0]; })
               .slice(0, 2).join("").toUpperCase();
  }

  var LI_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05C20.4 8.65 21 11.1 21 14.3V21h-4v-6c0-1.43-.03-3.27-2-3.27-2 0-2.3 1.56-2.3 3.17V21H9z"/></svg>';

  var ACCENT_CYCLE = ["a-navy", "a-sky", "a-green", "a-amber", "a-orange", "a-steel"];

  function photoPath(slug) { return "assets/img/board/" + slug + ".jpg"; }

  function personCard(person, i) {
    var hasBio = Array.isArray(person.bio) && person.bio.length;
    var card = document.createElement("div");
    card.className = "pcard " + ACCENT_CYCLE[i % ACCENT_CYCLE.length];

    card.innerHTML =
      '<div class="pcard__frame">' +
        '<div class="pcard__initials">' + initials(person.name) + "</div>" +
      "</div>" +
      '<div class="pcard__body">' +
        '<div class="pcard__name">' + person.name + "</div>" +
        '<div class="pcard__role">' + person.role + "</div>" +
        '<div class="pcard__foot">' +
          (person.li
            ? '<a class="pcard__li" href="' + person.li + '" target="_blank" rel="noopener" aria-label="' +
              person.name + ' on LinkedIn">' + LI_ICON + "</a>"
            : "") +

        "</div>" +
      "</div>";

    // swap in the photo if the file exists
    var frame = $(".pcard__frame", card);
    tryPhoto(photoPath(person.slug), function () {
      var el = document.createElement("img");
      el.className = "pcard__photo";
      el.src = photoPath(person.slug);
      el.alt = person.name;
      el.loading = "lazy";
      frame.insertBefore(el, frame.firstChild);
      $(".pcard__initials", frame).style.display = "none";
    });

    // A whole-card hit area for the bio, sitting under the LinkedIn link so both
    // stay clickable and we avoid nesting a button inside a button.
    if (hasBio) {
      card.classList.add("pcard--clickable");
      var hit = document.createElement("button");
      hit.type = "button";
      hit.className = "pcard__hit";
      hit.setAttribute("aria-label", "Read the full bio of " + person.name);
      hit.addEventListener("click", function () { openBio(person); });
      card.appendChild(hit);
    }
    return card;
  }

  var lastFocused = null;

  function openBio(person) {
    var modal = $("#bio-modal");
    if (!modal) return;
    lastFocused = document.activeElement;

    $("#bio-name").textContent = person.name;
    $("#bio-role").textContent = person.role;
    $("#bio-text").innerHTML = person.bio.map(function (t) { return "<p>" + t + "</p>"; }).join("");

    var frame = $("#bio-frame");
    frame.innerHTML = '<div class="biohead__initials">' + initials(person.name) + "</div>";
    tryPhoto(photoPath(person.slug), function () {
      frame.innerHTML = '<img src="' + photoPath(person.slug) + '" alt="' + person.name + '">';
    });

    var link = $("#bio-link");
    if (person.li) { link.href = person.li; link.hidden = false; } else { link.hidden = true; }

    modal.hidden = false;
    document.body.style.overflow = "hidden";
    $(".modal__close", modal).focus();
  }

  function closeBio() {
    var modal = $("#bio-modal");
    if (!modal || modal.hidden) return;
    modal.hidden = true;
    document.body.style.overflow = "";
    if (lastFocused) lastFocused.focus();
  }

  function initBoard() {
    var host = $("[data-board]");
    if (!host || typeof BOARD === "undefined") return;

    var n = 0;
    BOARD.forEach(function (group) {
      var head = document.createElement("div");
      head.className = "grouphead";
      head.innerHTML = '<h2 class="t-h3" style="margin:0">' + group.title + "</h2>";
      host.appendChild(head);

      var grid = document.createElement("div");
      grid.className = "people";
      grid.style.marginBottom = "3.5rem";
      group.people.forEach(function (person) { grid.appendChild(personCard(person, n++)); });
      host.appendChild(grid);
    });

    var modal = $("#bio-modal");
    if (!modal) return;
    $(".modal__close", modal).addEventListener("click", closeBio);
    modal.addEventListener("click", function (e) { if (e.target === modal) closeBio(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeBio(); });
  }

  /* ----------------------------------------------------------- carousel */
  /* Crossfades through the hero photographs. Pauses on hover and on focus so
     it never yanks the image out from under someone reading a caption, and
     holds on the first frame when reduced motion is requested. */
  function initCarousel() {
    $$("[data-carousel]").forEach(function (root) {
      var slides = $$(".carousel__slide", root);
      if (slides.length < 2) return;

      var gap = parseInt(root.getAttribute("data-interval") || "3000", 10);
      var dotWrap = $(".carousel__dots", root);
      var i = 0, timer = null;

      var dots = slides.map(function (_, n) {
        var d = document.createElement("button");
        d.type = "button";
        d.className = "carousel__dot";
        d.setAttribute("aria-label", "Show photograph " + (n + 1) + " of " + slides.length);
        d.addEventListener("click", function () { go(n); restart(); });
        if (dotWrap) dotWrap.appendChild(d);
        return d;
      });

      function go(n) {
        i = (n + slides.length) % slides.length;
        slides.forEach(function (s, k) { s.classList.toggle("is-on", k === i); });
        dots.forEach(function (d, k) { d.setAttribute("aria-current", String(k === i)); });
      }
      function start() { if (!reduced && !timer) timer = setInterval(function () { go(i + 1); }, gap); }
      function stop()  { clearInterval(timer); timer = null; }
      function restart() { stop(); start(); }

      go(0);
      start();
      root.addEventListener("mouseenter", stop);
      root.addEventListener("mouseleave", start);
      root.addEventListener("focusin", stop);
      root.addEventListener("focusout", start);
      document.addEventListener("visibilitychange", function () {
        if (document.hidden) stop(); else start();
      });
    });
  }

  /* -------------------------------------------------------------- video */
  /* Click-to-play facade: no YouTube script loads until the visitor asks for
     it, which keeps the page light and avoids third-party cookies on arrival. */
  function initVideo() {
    $$("[data-yt]").forEach(function (fig) {
      var id = fig.getAttribute("data-yt");
      var hit = $(".video__hit", fig);
      if (!id || !hit) return;

      // Poster frame. maxresdefault only exists for videos uploaded in HD, and
      // YouTube answers some missing sizes with a 120x90 grey placeholder rather
      // than a 404 — so walk down the sizes and reject anything suspiciously small.
      (function poster(sizes, n) {
        if (n >= sizes.length) return;                     // no poster: the CSS gradient stands in
        var url = "https://i.ytimg.com/vi/" + id + "/" + sizes[n] + ".jpg";
        var img = new Image();
        img.onload = function () {
          if (img.naturalWidth < 200) { poster(sizes, n + 1); return; }
          fig.style.backgroundImage = 'url("' + url + '")';
          fig.classList.add("video--hasposter");
        };
        img.onerror = function () { poster(sizes, n + 1); };
        img.src = url;
      })(["maxresdefault", "sddefault", "hqdefault"], 0);

      hit.addEventListener("click", function () {
        var frame = document.createElement("iframe");
        frame.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&modestbranding=1";
        frame.title = fig.getAttribute("data-title") || "Video";
        frame.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture";
        frame.allowFullscreen = true;
        frame.setAttribute("frameborder", "0");
        frame.className = "video__frame";
        fig.classList.add("video--playing");
        hit.replaceWith(frame);
      });
    });
  }

  /* ---------------------------------------------------------------- misc */
  function initYear() {
    $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  /* ---------------------------------------------------------------- boot */
  function boot() {
    initNav();
    initFigures();
    initBoard();     // build cards before reveal/observers attach
    initMaps();
    initReveal();
    initCounters();
    initFaq();
    initTabs();
    initCarousel();
    initVideo();
    initYear();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
