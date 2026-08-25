/* =====================================================================
   HumansOfCoding — i18n.js (core)
   ---------------------------------------------------------------------
   English is the AUTHENTIC version of this site. Every other language is
   translated by AI, and a notice under the header says so — including an
   apology for any mistakes — whenever a translation is active.

   Only this small file loads up front. A language dictionary is fetched
   from assets/i18n/<code>.js the first time that language is chosen, so
   an English visitor never downloads any translation data.

   To edit wording, open assets/i18n/<code>.js — see README section 2b.
   ===================================================================== */
window.HOC_I18N = window.HOC_I18N || {};

/* Languages offered in the switcher, grouped by region and alphabetical inside
   each group. English is the source; `rtl: true` flips page direction. */
window.HOC_I18N.languages = [
  { code: "zh",   label: "Chinese",             native: "简体中文",              region: "East Asia" },
  { code: "ja",   label: "Japanese",            native: "日本語",               region: "East Asia" },
  { code: "ko",   label: "Korean",              native: "한국어",               region: "East Asia" },
  { code: "bg",   label: "Bulgarian",           native: "Български",         region: "Europe" },
  { code: "en",   label: "English",             native: "English",           region: "Europe" },
  { code: "fr",   label: "French",              native: "Français",          region: "Europe" },
  { code: "de",   label: "German",              native: "Deutsch",           region: "Europe" },
  { code: "el",   label: "Greek",               native: "Ελληνικά",          region: "Europe" },
  { code: "it",   label: "Italian",             native: "Italiano",          region: "Europe" },
  { code: "nb",   label: "Norwegian",           native: "Norsk",             region: "Europe" },
  { code: "pl",   label: "Polish",              native: "Polski",            region: "Europe" },
  { code: "pt",   label: "Portuguese",          native: "Português",         region: "Europe" },
  { code: "ru",   label: "Russian",             native: "Русский",           region: "Europe" },
  { code: "es",   label: "Spanish",             native: "Español",           region: "Europe" },
  { code: "sv",   label: "Swedish",             native: "Svenska",           region: "Europe" },
  { code: "uk",   label: "Ukrainian",           native: "Українська",        region: "Europe" },
  { code: "ar",   label: "Arabic",              native: "العربية",           region: "Middle East & Central Asia", rtl: true },
  { code: "kk",   label: "Kazakh",              native: "Қазақша",           region: "Middle East & Central Asia" },
  { code: "fa",   label: "Persian",             native: "فارسی",             region: "Middle East & Central Asia", rtl: true },
  { code: "tr",   label: "Turkish",             native: "Türkçe",            region: "Middle East & Central Asia" },
  { code: "bn",   label: "Bengali",             native: "বাংলা",             region: "South Asia" },
  { code: "gu",   label: "Gujarati",            native: "ગુજરાતી",           region: "South Asia" },
  { code: "hi",   label: "Hindi",               native: "हिन्दी",            region: "South Asia" },
  { code: "mr",   label: "Marathi",             native: "मराठी",             region: "South Asia" },
  { code: "pa",   label: "Punjabi",             native: "ਪੰਜਾਬੀ",            region: "South Asia" },
  { code: "ta",   label: "Tamil",               native: "தமிழ்",             region: "South Asia" },
  { code: "te",   label: "Telugu",              native: "తెలుగు",            region: "South Asia" },
  { code: "ur",   label: "Urdu",                native: "اردو",              region: "South Asia", rtl: true },
  { code: "tl",   label: "Filipino",            native: "Filipino",          region: "Southeast Asia" },
  { code: "id",   label: "Indonesian",          native: "Bahasa Indonesia",  region: "Southeast Asia" },
  { code: "ms",   label: "Malay",               native: "Bahasa Melayu",     region: "Southeast Asia" },
  { code: "th",   label: "Thai",                native: "ไทย",               region: "Southeast Asia" },
  { code: "vi",   label: "Vietnamese",          native: "Tiếng Việt",        region: "Southeast Asia" }
];

/* Shown as a bar under the header while a translation is active. */
window.HOC_I18N.disclaimer = {
  ar: { text: "تُرجمت هذه الصفحة بواسطة الذكاء الاصطناعي وقد تحتوي على أخطاء — نعتذر عن أي خطأ. يُرجى الرجوع إلى النسخة الإنجليزية باعتبارها النسخة الموثوقة.", link: "عرض بالإنجليزية", ok: "حسنًا" },
  bg: { text: "Тази страница е преведена от изкуствен интелект и може да съдържа грешки — извиняваме се за тях. Моля, приемайте английската версия за меродавна.", link: "Вижте на английски", ok: "Разбрах" },
  de: { text: "Diese Seite wurde von einer KI übersetzt und kann Fehler enthalten — wir bitten um Entschuldigung. Verbindlich ist ausschließlich die englische Fassung.", link: "Auf Englisch ansehen", ok: "Verstanden" },
  el: { text: "Αυτή η σελίδα μεταφράστηκε από τεχνητή νοημοσύνη και μπορεί να περιέχει λάθη — ζητούμε συγγνώμη. Παρακαλούμε ανατρέξτε στην αγγλική έκδοση ως την αυθεντική.", link: "Προβολή στα αγγλικά", ok: "Εντάξει" },
  es: { text: "Esta página ha sido traducida por IA y puede contener errores — pedimos disculpas por ello. Consulta la versión en inglés como la auténtica.", link: "Ver en inglés", ok: "Entendido" },
  fr: { text: "Cette page a été traduite par une IA et peut contenir des erreurs — veuillez nous en excuser. Seule la version anglaise fait foi.", link: "Voir en anglais", ok: "J'ai compris" },
  hi: { text: "इस पेज का अनुवाद AI ने किया है और इसमें ग़लतियाँ हो सकती हैं — किसी भी भूल के लिए क्षमा करें। कृपया अंग्रेज़ी संस्करण को ही प्रामाणिक मानें।", link: "अंग्रेज़ी में देखें", ok: "ठीक है" },
  id: { text: "Halaman ini diterjemahkan oleh AI dan mungkin mengandung kesalahan — mohon maaf atas kekeliruan yang ada. Silakan merujuk ke versi bahasa Inggris sebagai versi yang paling sahih.", link: "Lihat dalam bahasa Inggris", ok: "Oke" },
  it: { text: "Questa pagina è stata tradotta da un'IA e potrebbe contenere errori — ce ne scusiamo. Fai riferimento alla versione inglese come quella autentica.", link: "Vedi in inglese", ok: "Ho capito" },
  ja: { text: "このページはAIによって翻訳されており、誤りが含まれている可能性があります。ご不便をおかけして申し訳ありません。正式な内容は英語版をご参照ください。", link: "英語版を見る", ok: "了解" },
  kk: { text: "Бұл бет жасанды интеллект арқылы аударылған және қателер болуы мүмкін — кешірім сұраймыз. Ағылшын тіліндегі нұсқаны түпнұсқа ретінде қараңыз.", link: "Ағылшынша қарау", ok: "Түсінікті" },
  ko: { text: "이 페이지는 AI가 번역했으며 오류가 있을 수 있습니다. 불편을 드려 죄송합니다. 정확한 내용은 영어 원문을 참고해 주세요.", link: "영어로 보기", ok: "확인" },
  ms: { text: "Halaman ini diterjemahkan oleh AI dan mungkin mengandungi kesilapan — kami memohon maaf. Sila rujuk versi bahasa Inggeris sebagai versi yang sahih.", link: "Lihat dalam bahasa Inggeris", ok: "Faham" },
  nb: { text: "Denne siden er oversatt av KI og kan inneholde feil — vi beklager eventuelle feil. Se den engelske versjonen som den autentiske.", link: "Se på engelsk", ok: "Greit" },
  pt: { text: "Esta página foi traduzida por IA e pode conter erros — pedimos desculpa por qualquer falha. Consulte a versão em inglês como a autêntica.", link: "Ver em inglês", ok: "Entendido" },
  ru: { text: "Эта страница переведена искусственным интеллектом и может содержать ошибки — приносим извинения. Пожалуйста, считайте английскую версию достоверной.", link: "Посмотреть на английском", ok: "Понятно" },
  sv: { text: "Den här sidan är översatt av AI och kan innehålla fel — vi ber om ursäkt för eventuella misstag. Se den engelska versionen som den autentiska.", link: "Visa på engelska", ok: "Okej" },
  ta: { text: "இந்தப் பக்கம் AI மூலம் மொழிபெயர்க்கப்பட்டது, பிழைகள் இருக்கக்கூடும் — தவறுகளுக்கு மன்னிக்கவும். ஆங்கிலப் பதிப்பையே சரியான பதிப்பாகக் கருதவும்.", link: "ஆங்கிலத்தில் பார்க்க", ok: "சரி" },
  th: { text: "หน้านี้แปลโดย AI และอาจมีข้อผิดพลาด ขออภัยในความคลาดเคลื่อน โปรดยึดฉบับภาษาอังกฤษเป็นฉบับที่ถูกต้อง", link: "ดูฉบับภาษาอังกฤษ", ok: "รับทราบ" },
  vi: { text: "Trang này được dịch bằng AI và có thể có sai sót — chúng tôi xin lỗi vì bất kỳ lỗi nào. Vui lòng xem bản tiếng Anh là bản chuẩn xác nhất.", link: "Xem bản tiếng Anh", ok: "Đã hiểu" },
  bn: { text: "এই পৃষ্ঠাটি AI দিয়ে অনুবাদ করা হয়েছে এবং এতে ভুল থাকতে পারে — এর জন্য আমরা দুঃখিত। অনুগ্রহ করে ইংরেজি সংস্করণটিকেই প্রামাণিক ধরুন।", link: "ইংরেজিতে দেখুন", ok: "ঠিক আছে" },
  fa: { text: "این صفحه توسط هوش مصنوعی ترجمه شده است و ممکن است خطا داشته باشد — بابت هر اشتباهی پوزش می‌خواهیم. لطفاً نسخهٔ انگلیسی را معتبر بدانید.", link: "مشاهده به انگلیسی", ok: "باشه" },
  gu: { text: "આ પાનું AI દ્વારા અનુવાદિત છે અને તેમાં ભૂલો હોઈ શકે છે — તે માટે અમે માફી માગીએ છીએ. કૃપા કરીને અંગ્રેજી સંસ્કરણને જ પ્રામાણિક ગણો.", link: "અંગ્રેજીમાં જુઓ", ok: "બરાબર" },
  mr: { text: "हे पान AI ने भाषांतरित केले आहे आणि त्यात चुका असू शकतात — त्याबद्दल क्षमस्व. कृपया इंग्रजी आवृत्तीच प्रमाण माना.", link: "इंग्रजीत पाहा", ok: "ठीक आहे" },
  pa: { text: "ਇਹ ਪੰਨਾ AI ਨੇ ਅਨੁਵਾਦ ਕੀਤਾ ਹੈ ਅਤੇ ਇਸ ਵਿੱਚ ਗਲਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ — ਇਸ ਲਈ ਮੁਆਫ਼ੀ। ਕਿਰਪਾ ਕਰਕੇ ਅੰਗਰੇਜ਼ੀ ਸੰਸਕਰਣ ਨੂੰ ਹੀ ਪ੍ਰਮਾਣਿਕ ਮੰਨੋ।", link: "ਅੰਗਰੇਜ਼ੀ ਵਿੱਚ ਵੇਖੋ", ok: "ਠੀਕ ਹੈ" },
  pl: { text: "Ta strona została przetłumaczona przez AI i może zawierać błędy — przepraszamy za nie. Wersją wiążącą jest wersja angielska.", link: "Zobacz po angielsku", ok: "Rozumiem" },
  te: { text: "ఈ పేజీని AI అనువదించింది, ఇందులో పొరపాట్లు ఉండవచ్చు — అందుకు క్షమించండి. దయచేసి ఇంగ్లీష్ వెర్షన్‌ను మాత్రమే ప్రామాణికంగా భావించండి.", link: "ఇంగ్లీష్‌లో చూడండి", ok: "సరే" },
  tl: { text: "Isinalin ang pahinang ito ng AI at maaaring may mga mali — paumanhin po. Pakitingnan ang bersyong Ingles bilang siyang tunay.", link: "Tingnan sa Ingles", ok: "Sige" },
  tr: { text: "Bu sayfa yapay zekâ tarafından çevrildi ve hatalar içerebilir — bunun için özür dileriz. Lütfen İngilizce sürümü esas alın.", link: "İngilizce görüntüle", ok: "Tamam" },
  uk: { text: "Цю сторінку переклав штучний інтелект, тож у ній можуть бути помилки — перепрошуємо за них. Автентичною вважайте англійську версію.", link: "Переглянути англійською", ok: "Зрозуміло" },
  ur: { text: "اس صفحے کا ترجمہ AI نے کیا ہے اور اس میں غلطیاں ہو سکتی ہیں — اس کے لیے معذرت۔ براہِ کرم انگریزی نسخے کو ہی مستند سمجھیں۔", link: "انگریزی میں دیکھیں", ok: "ٹھیک ہے" },
  zh: { text: "本页面由 AI 翻译，可能存在错误——对此我们深表歉意。请以英文版本为准。", link: "查看英文版", ok: "知道了" },
};

window.HOC_I18N.selectorLabel = {
  en: "Language", ar: "اللغة", bg: "Език", de: "Sprache", el: "Γλώσσα",
  es: "Idioma", fr: "Langue", hi: "भाषा", id: "Bahasa", it: "Lingua",
  ja: "言語", kk: "Тіл", ko: "언어", ms: "Bahasa", nb: "Språk",
  pt: "Idioma", ru: "Язык", sv: "Språk", ta: "மொழி", th: "ภาษา", vi: "Ngôn ngữ",
  bn: "ভাষা",
  fa: "زبان",
  gu: "ભાષા",
  mr: "भाषा",
  pa: "ਭਾਸ਼ਾ",
  pl: "Język",
  te: "భాష",
  tl: "Wika",
  tr: "Dil",
  uk: "Мова",
  ur: "زبان",
  zh: "语言",
};

/* Where the on-demand dictionaries live, relative to index.html. */
window.HOC_I18N.path = "assets/i18n/";
