// Counts clicks on links that leave this site, as GoatCounter events. Each link shows up in the GoatCounter
// dashboard as "out: <host><path>", next to the page views. Links to the lab's project sites use the
// reiserlab.github.io address, so they count as leaving the site too.
// Loaded only when `goatcounter` is set in data/site.yaml. Does nothing if GoatCounter is blocked.
(function () {
  function eventName(a) {
    if (a.protocol === 'mailto:') return 'email link';
    if (a.protocol !== 'http:' && a.protocol !== 'https:') return null;
    if (a.hostname === location.hostname) return null;
    return 'out: ' + a.hostname.replace(/^www\./, '') + a.pathname.replace(/\/$/, '') + a.search;
  }

  function onClick(e) {
    if (e.type === 'auxclick' && e.button !== 1) return;  // auxclick: count middle clicks only
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    // Links with their own data-goatcounter-click name are counted by GoatCounter's script.
    if (!a || a.hasAttribute('data-goatcounter-click')) return;
    var name = eventName(a);
    if (!name || !window.goatcounter || !window.goatcounter.count) return;
    window.goatcounter.count({
      path: name,
      // A card link holds a heading and a description; the heading alone is the clearer label.
      title: (a.querySelector('h1, h2, h3, h4') || a).textContent.replace(/\s+/g, ' ').trim().slice(0, 120),
      event: true,
    });
  }

  document.addEventListener('click', onClick, true);
  document.addEventListener('auxclick', onClick, true);
})();
