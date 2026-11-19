/* =====================================================================
   Tavzuran — i18n.js (core)
   ---------------------------------------------------------------------
   The site is English only. The translations, and the notice shown while
   a translation is active, are kept in the private lazyschool/tzr-translations
   repository; its README explains how to switch a language back on.

   With one language listed, script.js hides the language picker and never
   fetches a dictionary.
   ===================================================================== */
window.TAVZ_I18N = window.TAVZ_I18N || {};

/* Languages offered in the switcher. English is the source and the only one. */
window.TAVZ_I18N.languages = [
  { code: "en", label: "English", native: "English", region: "" },
];

/* Shown as a bar under the header while a translation is active: never, now. */
window.TAVZ_I18N.disclaimer = {};

window.TAVZ_I18N.selectorLabel = {
  en: "Language",
};

/* Where on-demand dictionaries would live, resolved against this file's URL. */
window.TAVZ_I18N.path = (function () {
  var self = document.currentScript;
  var base = self && self.src ? self.src.replace(/[^/]*$/, "") : "";
  return base + "assets/i18n/";
})();
