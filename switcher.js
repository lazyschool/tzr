/* Design switcher: a small drop-down that opens the same page in another
   version of the site. No requests, nothing stored. */
(function () {
  "use strict";
  var VERSIONS = [
    { id: "", name: "First Light (space)" },
    { id: "blueprint", name: "Blueprint" },
    { id: "honest-quote", name: "The Honest Quote" }
  ];
  /* Work out where this version's root is from the script's own address, so
     it also works when a page is opened straight from disk. */
  var me = document.currentScript && document.currentScript.src;
  var base = me ? me.slice(0, me.lastIndexOf("/") + 1) : location.href.slice(0, location.href.lastIndexOf("/") + 1);
  var m = base.match(/^(.*\/)v\/([a-z-]+)\/$/);
  var current = m ? m[2] : "";
  var siteRoot = m ? m[1] : base;
  var rest = location.href.slice(base.length).split("#")[0];

  function go(id) {
    var url = siteRoot + (id ? "v/" + id + "/" : "") + rest;
    if (location.protocol === "file:" && (rest === "" || /\/$/.test(rest))) url += "index.html";
    location.href = url + location.hash;
  }

  function pick() {
    var sel = document.createElement("select");
    sel.setAttribute("aria-label", "Design");
    VERSIONS.forEach(function (v) {
      var o = document.createElement("option");
      o.value = v.id;
      o.textContent = v.name;
      if (v.id === current) o.selected = true;
      sel.appendChild(o);
    });
    sel.addEventListener("change", function () {
      go(sel.value);
    });
    return sel;
  }

  function icon() {
    var NS = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("class", "lang__globe");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2");
    svg.setAttribute("stroke-linejoin", "round");
    svg.setAttribute("aria-hidden", "true");
    var path = document.createElementNS(NS, "path");
    path.setAttribute("d", "m12 3 9 5-9 5-9-5 9-5Zm-9 9 9 5 9-5m-18 4 9 5 9-5");
    svg.appendChild(path);
    return svg;
  }

  function caret() {
    var NS = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("class", "lang__caret");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2.4");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.setAttribute("aria-hidden", "true");
    var path = document.createElementNS(NS, "path");
    path.setAttribute("d", "m6 9 6 6 6-6");
    svg.appendChild(path);
    return svg;
  }

  var actions = document.querySelector(".nav__actions");
  if (actions) {
    /* In the navbar, wearing the language control's own styling. */
    var wrap = document.createElement("div");
    wrap.className = "lang";
    var sel = pick();
    sel.className = "lang__select";
    wrap.appendChild(icon());
    wrap.appendChild(sel);
    wrap.appendChild(caret());
    actions.insertBefore(wrap, actions.firstChild);
    return;
  }

  /* No navbar on this page: fall back to a small floating control. */
  var css = document.createElement("style");
  css.textContent =
    ".vsw{position:fixed;left:12px;bottom:12px;z-index:2147483000;padding:6px 10px;border-radius:999px;" +
    "background:rgba(12,16,14,.88);color:#eef3f0;border:1px solid rgba(255,255,255,.28);font:500 12px/1 system-ui,sans-serif}" +
    ".vsw select{font:inherit;color:inherit;background:#0c100e;border:1px solid rgba(255,255,255,.28);border-radius:6px;padding:4px 6px}";
  document.head.appendChild(css);
  var box = document.createElement("div");
  box.className = "vsw";
  box.appendChild(pick());
  document.body.appendChild(box);
})();
