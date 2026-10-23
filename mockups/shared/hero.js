/* Scroll-driven frame scrubber for the home-page hero.
 *
 * Markup: <section data-scrub data-frames="N" data-pattern="path/f_%04d.webp">
 *           <div class="hero-sticky"><canvas class="hero-canvas"></canvas> ... [data-stop data-from data-to] ...</div>
 *         </section>
 * The section is tall; the inner block is sticky. Scroll progress through the
 * section (0..1) selects a frame, which is drawn cover-fit onto the canvas.
 * Frames load in priority order (every 8th, then 4th, then 2nd, then all) so
 * scrubbing works before everything has arrived. With prefers-reduced-motion
 * a single frame is shown and the text stops are all visible.
 */
(function () {
  const el = document.querySelector('[data-scrub]');
  if (!el) return;
  const canvas = el.querySelector('canvas');
  const poster = el.querySelector('.hero-poster');
  const stops = Array.from(el.querySelectorAll('.stop'));
  const N = parseInt(el.dataset.frames, 10);
  const pattern = el.dataset.pattern;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const flat = /[?&]flat=1/.test(location.search); // review aid: render the hero as one screen

  if (reduced || flat || !canvas.getContext) {
    el.classList.add('hero-static');
    stops.forEach(s => s.classList.add('is-active'));
    return;
  }

  const ctx = canvas.getContext('2d', { alpha: false });
  const frames = new Array(N);
  let current = 0, drawn = -1, ready = false;

  const src = i => pattern.replace('%04d', String(i + 1).padStart(4, '0'));

  function load(i) {
    if (frames[i]) return;
    const im = new Image();
    im.decoding = 'async';
    im.onload = () => {
      if (!ready) { ready = true; el.classList.add('hero-ready'); }
      if (i === current || drawn < 0) draw(true);
    };
    im.src = src(i);
    frames[i] = im;
  }

  // Priority loading: coarse to fine.
  [8, 4, 2, 1].forEach((step, k) => {
    setTimeout(() => { for (let i = 0; i < N; i += step) load(i); }, k * 120);
  });

  function nearestLoaded(i) {
    for (let d = 0; d < N; d++) {
      const a = frames[i - d], b = frames[i + d];
      if (a && a.complete && a.naturalWidth) return a;
      if (b && b.complete && b.naturalWidth) return b;
    }
    return null;
  }

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
    }
    draw(true);
  }

  function draw(force) {
    if (!force && drawn === current) return;
    const im = nearestLoaded(current);
    if (!im) return;
    const cw = canvas.width, ch = canvas.height;
    const s = Math.max(cw / im.naturalWidth, ch / im.naturalHeight);
    const dw = im.naturalWidth * s, dh = im.naturalHeight * s;
    ctx.drawImage(im, (cw - dw) / 2, (ch - dh) / 2, dw, dh);
    drawn = current;
    if (poster) poster.style.opacity = '0';
  }

  function progress() {
    const rect = el.getBoundingClientRect();
    const total = el.offsetHeight - window.innerHeight;
    if (total <= 0) return 0;
    return Math.min(1, Math.max(0, -rect.top / total));
  }

  function updateStops(p) {
    stops.forEach(s => {
      const a = parseFloat(s.dataset.from), b = parseFloat(s.dataset.to);
      s.classList.toggle('is-active', p >= a && p <= b);
    });
    el.classList.toggle('hero-done', p >= 0.999);
  }

  let ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const p = progress();
      current = Math.round(p * (N - 1));
      draw(false);
      updateStops(p);
      ticking = false;
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', resize);
  resize();
  onScroll();
})();
