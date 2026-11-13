/* Design switcher: a small drop-down that opens the same page in another
   version of the site. No requests, nothing stored. */
(function () {
  "use strict";
  var VERSIONS = [
    { id: "", name: "First Light (space)" },
    { id: "blueprint", name: "Blueprint" },
    { id: "honest-quote", name: "The Honest Quote" }
  ];
  var m = location.pathname.match(/^\/v\/([a-z-]+)(\/.*)?$/);
  var current = m ? m[1] : "";
  var rest = m ? (m[2] || "/") : location.pathname;

  var css = document.createElement("style");
  css.textContent =
    ".vsw{position:fixed;left:12px;bottom:12px;z-index:2147483000;display:flex;align-items:center;gap:8px;" +
    "padding:6px 10px;border-radius:999px;background:rgba(12,16,14,.88);color:#eef3f0;" +
    "border:1px solid rgba(255,255,255,.28);font:500 12px/1 ui-monospace,Menlo,Consolas,monospace;" +
    "-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}" +
    ".vsw select{font:inherit;color:inherit;background:#0c100e;border:1px solid rgba(255,255,255,.28);" +
    "border-radius:6px;padding:4px 6px;max-width:48vw}" +
    ".vsw select:focus-visible{outline:2px solid #5fe0a6;outline-offset:2px}" +
    "@media (max-width:760px){.vsw{bottom:84px}}@media print{.vsw{display:none}}";
  document.head.appendChild(css);

  var box = document.createElement("div");
  box.className = "vsw";
  var label = document.createElement("label");
  label.setAttribute("for", "vsw-select");
  label.textContent = "Design";
  var sel = document.createElement("select");
  sel.id = "vsw-select";
  VERSIONS.forEach(function (v) {
    var o = document.createElement("option");
    o.value = v.id;
    o.textContent = v.name;
    if (v.id === current) o.selected = true;
    sel.appendChild(o);
  });
  sel.addEventListener("change", function () {
    var id = sel.value;
    location.href = (id ? "/v/" + id : "") + rest + location.hash;
  });
  box.appendChild(label);
  box.appendChild(sel);
  document.body.appendChild(box);
})();
