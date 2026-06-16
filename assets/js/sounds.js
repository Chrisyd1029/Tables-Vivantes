// ════════════════════════════════════════════════════════════
//  DICTIONNAIRE DE SONS — synthèse Web Audio (bruits de bois)
//  Aucun fichier audio : frappes (knock), grincements (creak,
//  friction « stick-slip ») et vibrations (rumble) générés au clic.
// ════════════════════════════════════════════════════════════
(() => {
  let ctx, master;
  const buffers = {};

  function ensure() {
    if (ctx) return;
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    master = ctx.createGain(); master.gain.value = 0.9;
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 3400;
    master.connect(lp); lp.connect(ctx.destination);
  }
  function noise(dur) {
    const key = Math.round(dur * 1000);
    if (buffers[key]) return buffers[key];
    const len = Math.max(1, Math.floor(ctx.sampleRate * dur));
    const b = ctx.createBuffer(1, len, ctx.sampleRate); const d = b.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    return buffers[key] = b;
  }
  function knock(t, freq, gain, decay) {
    decay = decay || 0.16;
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(gain, t + 0.004);
    g.gain.exponentialRampToValueAtTime(0.0001, t + decay);
    g.connect(master);
    [1, 2.6, 5.1].forEach((m, i) => {
      const o = ctx.createOscillator(); o.type = 'sine'; o.frequency.value = freq * m;
      const pg = ctx.createGain(); pg.gain.value = 1 / (i * 1.8 + 1);
      o.connect(pg); pg.connect(g); o.start(t); o.stop(t + decay);
    });
    const n = ctx.createBufferSource(); n.buffer = noise(0.05);
    const bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = freq * 2.2; bp.Q.value = 1.5;
    const ng = ctx.createGain(); ng.gain.setValueAtTime(gain * 0.9, t); ng.gain.exponentialRampToValueAtTime(0.0001, t + 0.045);
    n.connect(bp); bp.connect(ng); ng.connect(master); n.start(t); n.stop(t + 0.06);
  }
  function creak(t, dur, f0, f1, gain) {
    gain = gain || 0.5;
    const n = ctx.createBufferSource(); n.buffer = noise(dur + 0.2); n.loop = true;
    const bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.Q.value = 9;
    bp.frequency.setValueAtTime(f0, t); bp.frequency.exponentialRampToValueAtTime(f1, t + dur);
    const g = ctx.createGain(); g.gain.setValueAtTime(0.0001, t);
    const stepT = 0.018, steps = Math.max(2, Math.floor(dur / stepT));
    for (let i = 0; i <= steps; i++) {
      const tt = t + i * stepT;
      const arc = Math.sin(Math.PI * i / steps);
      const slip = 0.3 + 0.7 * Math.pow(Math.abs(Math.sin(i * 1.9 + Math.sin(i * 0.7))), 1.5);
      g.gain.setValueAtTime(Math.max(0.0001, gain * arc * slip), tt);
    }
    g.gain.exponentialRampToValueAtTime(0.0001, t + dur + 0.02);
    n.connect(bp); bp.connect(g); g.connect(master); n.start(t); n.stop(t + dur + 0.06);
  }
  function rumble(t, dur, freq, gain) {
    freq = freq || 50; gain = gain || 0.6;
    const o = ctx.createOscillator(); o.type = 'triangle';
    o.frequency.setValueAtTime(freq, t); o.frequency.linearRampToValueAtTime(freq * 1.3, t + dur);
    const lfo = ctx.createOscillator(); lfo.type = 'sine'; lfo.frequency.value = 6;
    const lg = ctx.createGain(); lg.gain.value = freq * 0.08; lfo.connect(lg); lg.connect(o.frequency);
    const g = ctx.createGain(); g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(gain, t + dur * 0.35);
    g.gain.setValueAtTime(gain, t + dur * 0.6);
    g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.connect(g); g.connect(master); o.start(t); o.stop(t + dur + 0.06); lfo.start(t); lfo.stop(t + dur + 0.06);
  }

  const now = () => ctx.currentTime + 0.05;
  const scores = {
    danger() { const t = now(); for (let i = 0; i < 6; i++) knock(t + i * 0.11, 330 - i * 10, 0.6, 0.10); return 0.85; },
    eau() { const t = now(); creak(t, 0.9, 170, 540, 0.5); knock(t + 0.98, 260, 0.4, 0.18); knock(t + 1.18, 300, 0.32, 0.18); return 1.5; },
    contact() { const t = now(); creak(t, 0.55, 150, 105, 0.55); return 0.7; },
    rassemblement() { const t = now(); rumble(t, 1.7, 44, 0.7); knock(t + 1.55, 150, 0.45, 0.3); return 2.0; },
    parade() { const t = now(); const beat = 0.16; for (let i = 0; i < 8; i++) knock(t + i * beat, i % 2 ? 200 : 300, 0.5, 0.12); creak(t + 8 * beat, 0.7, 220, 430, 0.45); return 8 * beat + 0.85; },
    detresse() { const t = now(); creak(t, 1.1, 620, 780, 0.5); return 1.25; }
  };

  function play(name, btn) {
    ensure();
    if (ctx.state === 'suspended') ctx.resume();
    const fn = scores[name]; if (!fn) return;
    const dur = fn();
    if (btn) { btn.classList.add('playing'); setTimeout(() => btn.classList.remove('playing'), Math.ceil(dur * 1000)); }
  }
  document.querySelectorAll('.word .play').forEach(b => b.addEventListener('click', () => play(b.dataset.sound, b)));
})();
