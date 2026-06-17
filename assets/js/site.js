// ════════════════════════════════════════════════════════════
//  TABLES SAUVAGES — script partagé
//  · apparition au scroll (IntersectionObserver)
//  · narrateur (synthèse vocale, dans la langue de la page)
// ════════════════════════════════════════════════════════════

// Menu burger (mobile)
const burger = document.querySelector('.burger');
const menu = document.querySelector('.menu');
if (burger && menu) {
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}
// Sous-menus : clic pour ouvrir/fermer (tactile + desktop ; le survol gère le reste)
document.querySelectorAll('.sub-toggle').forEach(t => {
  t.addEventListener('click', (e) => {
    e.preventDefault();
    const li = t.parentElement;
    const open = li.classList.toggle('open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
});

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
