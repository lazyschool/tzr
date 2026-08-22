/* =====================================================================
   HumansOfCoding — i18n.js (core)
   ---------------------------------------------------------------------
   English is the AUTHENTIC version of this site. The other languages are
   machine-assisted translations, and a notice under the header says so
   whenever one is active.

   Only this small file loads up front. A language dictionary is fetched
   from assets/i18n/<code>.js the first time that language is chosen, so
   an English visitor never downloads any translation data.

   To edit wording, open assets/i18n/<code>.js — see README section 2b.
   ===================================================================== */
window.HOC_I18N = window.HOC_I18N || {};

/* Languages offered in the switcher. `en` first — it is the source. */
window.HOC_I18N.languages = [
  {
    "code": "en",
    "label": "English",
    "native": "English"
  },
  {
    "code": "hi",
    "label": "Hindi",
    "native": "हिन्दी"
  },
  {
    "code": "de",
    "label": "German",
    "native": "Deutsch"
  },
  {
    "code": "fr",
    "label": "French",
    "native": "Français"
  },
  {
    "code": "es",
    "label": "Spanish",
    "native": "Español"
  }
];

/* Shown as a bar under the header while a translation is active. */
window.HOC_I18N.disclaimer = {
  "hi": {
    "text": "यह पेज इलेक्ट्रॉनिक रूप से अनुवादित है और इसमें ग़लतियाँ हो सकती हैं। अंग्रेज़ी संस्करण ही प्रामाणिक माना जाएगा।",
    "link": "अंग्रेज़ी में देखें"
  },
  "de": {
    "text": "Diese Seite wurde elektronisch übersetzt und kann Fehler enthalten. Verbindlich ist ausschließlich die englische Fassung.",
    "link": "Auf Englisch ansehen"
  },
  "fr": {
    "text": "Cette page a été traduite électroniquement et peut contenir des erreurs. Seule la version anglaise fait foi.",
    "link": "Voir en anglais"
  },
  "es": {
    "text": "Esta página se ha traducido electrónicamente y puede contener errores. La versión en inglés es la auténtica.",
    "link": "Ver en inglés"
  }
};

window.HOC_I18N.selectorLabel = {
  "en": "Language",
  "hi": "भाषा",
  "de": "Sprache",
  "fr": "Langue",
  "es": "Idioma"
};

/* Where the on-demand dictionaries live, relative to index.html. */
window.HOC_I18N.path = "assets/i18n/";
