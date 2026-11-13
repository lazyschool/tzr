/* Design switcher: a small drop-down that opens the same page in another
   version of the site. No requests, nothing stored. */
(function () {
  "use strict";
  var VERSIONS = [
    { id: "", name: "First Light (space)" },
    { id: "blueprint", name: "Blueprint" },
    { id: "honest-quote", name: "The Honest Quote" },
    { id: "original", name: "Original" }
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

  function css(text) {
    var el = document.createElement("style");
    el.textContent = text;
    document.head.appendChild(el);
  }

  var panel = document.getElementById("appearPanel");
  if (panel) {
    /* Inside the theme dialogue, as its own row. */
    css(".vsw-row{display:grid!important;gap:6px;min-width:12rem}" +
        ".vsw-row label{font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;opacity:.75}" +
        ".vsw-row select{width:100%;padding:9px 10px;font:inherit;font-size:.9rem;color:inherit;" +
        "background:transparent;border:1px solid var(--line-2,currentColor);border-radius:10px;cursor:pointer}" +
        ".vsw-row select:focus-visible{outline:2px solid var(--hue,currentColor);outline-offset:2px}" +
        ".vsw-row option{color:#111;background:#fff}");
    var row = document.createElement("div");
    row.className = "appear__row vsw-row";
    var label = document.createElement("label");
    label.setAttribute("for", "vsw-select");
    label.textContent = "Design";
    var sel = pick();
    sel.id = "vsw-select";
    row.appendChild(label);
    row.appendChild(sel);
    panel.insertBefore(row, panel.firstChild);
    return;
  }

  /* No navbar on this page: fall back to a small floating control. */
  css(
    ".vsw{position:fixed;left:12px;bottom:12px;z-index:2147483000;padding:6px 10px;border-radius:999px;" +
    "background:rgba(12,16,14,.88);color:#eef3f0;border:1px solid rgba(255,255,255,.28);font:500 12px/1 system-ui,sans-serif}" +
    ".vsw select{font:inherit;color:inherit;background:#0c100e;border:1px solid rgba(255,255,255,.28);border-radius:6px;padding:4px 6px}");
  var box = document.createElement("div");
  box.className = "vsw";
  box.appendChild(pick());
  document.body.appendChild(box);
})();
