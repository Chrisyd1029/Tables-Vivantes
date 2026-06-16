// ════════════════════════════════════════════════════════════
//  TABLES SAUVAGES — script partagé
//  · apparition au scroll (IntersectionObserver)
//  · narrateur (synthèse vocale, dans la langue de la page)
// ════════════════════════════════════════════════════════════

// Narrateur : lit le contenu principal dans la langue du document
function speakPage() {
  const synth = window.speechSynthesis;
  if (!synth) return;
  if (synth.speaking) { synth.cancel(); return; }
  const main = document.querySelector('main') || document.body;
  const text = main.innerText.replace(/\s+/g, ' ').slice(0, 3800);
  const u = new SpeechSynthesisUtterance(text);
  const lang = document.documentElement.lang || 'fr';
  u.lang = { fr: 'fr-FR', en: 'en-GB', de: 'de-DE' }[lang] || 'fr-FR';
  u.rate = 0.9; u.pitch = 0.85;
  synth.speak(u);
}
document.querySelectorAll('[data-narrator]').forEach(b => b.addEventListener('click', speakPage));
window.addEventListener('beforeunload', () => window.speechSynthesis && window.speechSynthesis.cancel());
