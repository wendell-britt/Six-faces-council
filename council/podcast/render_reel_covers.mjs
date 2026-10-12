// Renders Instagram Reel covers for a podcast episode's clips, in the same look as the YouTube thumbnails
// (render_thumbnails.mjs). Part of step 6 of the podcast episode move (council/moves/podcast-episode.md).
//
//   NODE_PATH=$(npm root -g) node council/podcast/render_reel_covers.mjs <spec.json> <out-dir>
//
// A cover is designed, like a thumbnail, never a frame from the video (Wendell, 2026-10-07: "don't want a frame
// from the video for the cover photo. This is essentially working as a youtube thumbnail but for the clips and for
// instagram"). Each clip in the spec becomes a 1080 x 1920 cover and its 1080 x 1440 profile grid crop.
//
// Every cover follows the clip cover standard in cover_standard.json (COVER_STANDARD.md; Wendell, 2026-10-12: "We
// need to standardize this across all of our podcasta and the thumbnail studio"). The words, the drawing and the
// labels all sit inside the safe box, which survives the profile grid's 3:4 crop, the feed's 4:5 crop and the Reels
// screen's tabs, caption and right-hand buttons. The headline shrinks until everything fits, and the render fails if
// anything still pokes out. The contact sheet shows each cover with those zones marked, and its grid crop at phone size.
//
// A clip picks a motif (mirror, distance, hourglass, downhill, space, quote) and its words. *Stars* in a headline get
// the pink-to-gold. Optional per clip: size (the headline's starting size), sub (a gold line under it), noGuest.

import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const { chromium } = createRequire(import.meta.url)('playwright');

const STD = JSON.parse(fs.readFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)), 'cover_standard.json'), 'utf8'));
const { w: W, h: H } = STD.canvas;
const SAFE = STD.safe, GRID = STD.crops.grid_3x4, FEED = STD.crops.feed_4x5, UI = STD.ui_zones;
const VB = [160, 340, 800, 640]; // the part of the old 1080 x 1920 drawing space the motifs use

const css = `
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@600;700;800&family=Space+Mono:wght@700&display=block');
*{box-sizing:border-box;margin:0}
html,body{width:${W}px;height:${H}px;overflow:hidden;background:#0b0910}
.t{position:relative;width:${W}px;height:${H}px;overflow:hidden;color:#f4f1ea;font-family:Jost,Futura,sans-serif;
  background:radial-gradient(120% 70% at 30% 0%,#241134,#0b0910 62%)}
.safe{position:absolute;left:${SAFE.left}px;top:${SAFE.top}px;width:${SAFE.right - SAFE.left}px;height:${SAFE.bottom - SAFE.top}px;
  display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;gap:24px}
.kick{font:700 24px 'Space Mono',monospace;letter-spacing:.2em;text-transform:uppercase;color:#ff5fa8}
.ep{font:800 34px Jost;color:#0b0910;background:linear-gradient(135deg,#ffe08a,#e6b93f 55%,#c07a1e);padding:4px 18px;border-radius:12px;white-space:nowrap}
.art{flex:1 1 auto;min-height:0;position:relative;margin:28px 0 36px}
.art .box{position:relative;height:100%;max-width:100%;aspect-ratio:5/4;margin:0 auto}
.art.quote .box{aspect-ratio:auto;width:100%}
.glow{position:absolute;border-radius:50%;filter:blur(12px)}
.qmark{position:absolute;left:-14px;bottom:-120px;font:700 300px Georgia,serif;color:#ff5fa8;opacity:.9;line-height:1}
.hl{font-weight:800;letter-spacing:-.025em;line-height:.98;flex:none;white-space:nowrap}
.grad{background:linear-gradient(100deg,#ff5fa8 10%,#e6b93f 90%);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{font:700 40px Jost;color:#e6b93f;margin-top:40px;flex:none}
.foot{display:flex;justify-content:space-between;align-items:baseline;margin-top:44px;flex:none}
.guest{font:700 40px Jost;color:#ecd9f6}
.guest b{color:#e6b93f;font-weight:800}
.clip{font:700 24px 'Space Mono',monospace;letter-spacing:.18em;color:#a99bb8;margin-left:auto}
`;

function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function words(s) { return esc(s).replace(/\*([^*]+)\*/g, '<span class="grad">$1</span>').replace(/\n/g, '<br>'); }

const motifs = {
  // Two faces turned to each other; what each cannot see of itself shows only in the other.
  mirror: () => `
    <svg viewBox="${VB.join(' ')}" style="position:absolute;inset:0;width:100%;height:100%">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <ellipse cx="540" cy="620" rx="150" ry="215" fill="none" stroke="#cbc2d8" stroke-opacity=".35" stroke-width="7" stroke-dasharray="4 16" stroke-linecap="round"/>
      <path d="M330 470 q-80 70 -40 170 q20 40 -10 70 q40 10 30 60 q40 40 90 30" fill="none" stroke="#cbc2d8" stroke-opacity=".6" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M750 470 q80 70 40 170 q-20 40 10 70 q-40 10 -30 60 q-40 40 -90 30" fill="none" stroke="url(#g)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M440 620 L640 620" stroke="url(#g)" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 14"/>
    </svg>
    <div class="glow" style="width:95.0%;height:96.9%;left:0.0%;top:-1.6%;background:radial-gradient(ellipse,rgba(255,95,168,.22),rgba(34,211,238,.10) 55%,transparent 74%)"></div>`,

  // A far globe, faded and struck; two people side by side, close enough to touch.
  distance: () => `
    <svg viewBox="${VB.join(' ')}" style="position:absolute;inset:0;width:100%;height:100%">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <g stroke="#cbc2d8" stroke-opacity=".35" stroke-width="5" fill="none">
        <circle cx="830" cy="470" r="95"/><ellipse cx="830" cy="470" rx="42" ry="95"/><path d="M735 470 H925 M748 420 H912 M748 520 H912"/>
      </g>
      <path d="M720 380 L940 560" stroke="#ff5fa8" stroke-width="9" stroke-linecap="round"/>
      <circle cx="430" cy="560" r="58" fill="none" stroke="#ecd9f6" stroke-width="9"/>
      <path d="M300 800 C 300 680, 360 640, 430 640 C 480 640, 520 660, 540 690" fill="none" stroke="#ecd9f6" stroke-width="9" stroke-linecap="round"/>
      <circle cx="650" cy="560" r="58" fill="none" stroke="url(#g)" stroke-width="9"/>
      <path d="M780 800 C 780 680, 720 640, 650 640 C 600 640, 560 660, 540 690" fill="none" stroke="url(#g)" stroke-width="9" stroke-linecap="round"/>
      <circle cx="540" cy="692" r="13" fill="#e6b93f"/>
    </svg>
    <div class="glow" style="width:65.0%;height:56.2%;left:15.0%;top:34.4%;background:radial-gradient(ellipse,rgba(230,185,63,.30),transparent 70%)"></div>`,

  // An hourglass half run: the question is about duration, and the answer belongs to the one feeling it.
  hourglass: () => `
    <svg viewBox="${VB.join(' ')}" style="position:absolute;inset:0;width:100%;height:100%">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <path d="M400 400 H680 M400 840 H680" stroke="#cbc2d8" stroke-opacity=".6" stroke-width="10" stroke-linecap="round"/>
      <path d="M420 400 C 420 540, 530 580, 530 620 C 530 660, 420 700, 420 840 M660 400 C 660 540, 550 580, 550 620 C 550 660, 660 700, 660 840"
        fill="none" stroke="#cbc2d8" stroke-opacity=".6" stroke-width="8" stroke-linecap="round"/>
      <path d="M470 500 Q540 530 610 500 Q590 560 540 600 Q490 560 470 500 Z" fill="url(#g)" opacity=".9"/>
      <path d="M540 610 V790" stroke="#e6b93f" stroke-width="5" stroke-dasharray="3 12" stroke-linecap="round"/>
      <path d="M450 830 Q540 740 630 830 Z" fill="url(#g)" opacity=".9"/>
    </svg>
    <div class="glow" style="width:77.5%;height:87.5%;left:8.8%;top:0.0%;background:radial-gradient(ellipse,rgba(230,185,63,.22),transparent 70%)"></div>`,

  // Help that only flows one way: a stack of arrows down from a high step, nothing coming back up.
  downhill: () => `
    <svg viewBox="${VB.join(' ')}" style="position:absolute;inset:0;width:100%;height:100%">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <path d="M180 470 H460 V860 H900" fill="none" stroke="#cbc2d8" stroke-opacity=".55" stroke-width="9" stroke-linejoin="round"/>
      <circle cx="320" cy="420" r="40" fill="none" stroke="#ecd9f6" stroke-width="8"/>
      <circle cx="720" cy="810" r="40" fill="none" stroke="#ecd9f6" stroke-width="8"/>
      <g stroke="url(#g)" stroke-width="9" stroke-linecap="round" fill="none">
        <path d="M380 480 C 520 520, 600 620, 660 760"/><path d="M640 735 L662 768 L690 742"/>
      </g>
      <path d="M680 880 C 600 960, 420 900, 330 520" fill="none" stroke="#cbc2d8" stroke-opacity=".35" stroke-width="6" stroke-dasharray="4 18" stroke-linecap="round"/>
    </svg>
    <div class="glow" style="width:80.0%;height:65.6%;left:21.2%;top:31.2%;background:radial-gradient(ellipse,rgba(255,95,168,.20),transparent 70%)"></div>`,

  // An empty space with its border held open, and one small light arriving in it.
  space: () => `
    <svg viewBox="${VB.join(' ')}" style="position:absolute;inset:0;width:100%;height:100%">
      <defs><radialGradient id="r"><stop offset="0" stop-color="#ffe08a"/><stop offset=".5" stop-color="#e6b93f" stop-opacity=".7"/><stop offset="1" stop-color="#e6b93f" stop-opacity="0"/></radialGradient></defs>
      <circle cx="540" cy="650" r="210" fill="none" stroke="#cbc2d8" stroke-opacity=".5" stroke-width="7" stroke-dasharray="6 20" stroke-linecap="round"/>
      <circle cx="540" cy="650" r="270" fill="none" stroke="#ff5fa8" stroke-opacity=".35" stroke-width="4"/>
      <circle cx="590" cy="600" r="70" fill="url(#r)"/>
      <circle cx="590" cy="600" r="14" fill="#ffe08a"/>
    </svg>
    <div class="glow" style="width:95.0%;height:96.9%;left:0.0%;top:-4.7%;background:radial-gradient(ellipse,rgba(217,168,240,.16),transparent 70%)"></div>`,

  // A line from the episode, quoted.
  quote: () => `
    <div class="glow" style="width:110%;height:150%;left:-40%;top:-30%;background:radial-gradient(ellipse,rgba(217,168,240,.26),transparent 70%)"></div>
    <div class="qmark">“</div>`,
};

function page(s, c) {
  const art = c.motif === 'quote' || !motifs[c.motif] ? 'quote' : c.motif;
  return `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="t"><div class="safe">
    <div class="top"><div class="kick">${esc(s.show)}</div><div class="ep">EP ${esc(s.episode)}</div></div>
    <div class="art ${art}"><div class="box">${motifs[art]()}</div></div>
    <div class="hl" style="font-size:${c.size || 116}px">${words(c.headline)}</div>
    ${c.sub ? `<div class="sub">${esc(c.sub)}</div>` : ''}
    <div class="foot">${c.noGuest ? '' : `<div class="guest">with <b>${esc(s.guest)}</b></div>`}<div class="clip">CLIP ${esc(c.n)}</div></div>
  </div></div></body></html>`;
}

const [specPath, outDir] = process.argv.slice(2);
if (!specPath || !outDir) { console.error('usage: node render_reel_covers.mjs <spec.json> <out-dir>'); process.exit(2); }
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const pg = await browser.newPage({ viewport: { width: W, height: H } });
const made = [];
let bad = 0;
for (const c of spec.clips) {
  await pg.setContent(page(spec, c), { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  // Shrink the headline until it fits its width and leaves the drawing at least a fifth of the safe box.
  const fit = await pg.evaluate(({ SAFE }) => {
    const hl = document.querySelector('.hl'), art = document.querySelector('.art');
    let size = parseFloat(hl.style.fontSize);
    const minArt = (SAFE.bottom - SAFE.top) / 5;
    while (size > 56 && (hl.scrollWidth > hl.clientWidth + 1 || art.getBoundingClientRect().height < minArt)) {
      size -= 4; hl.style.fontSize = size + 'px';
    }
    // Everything drawn in words must sit inside the safe box.
    const out = [];
    for (const el of document.querySelectorAll('.kick,.ep,.hl,.sub,.guest,.clip')) {
      const r = el.getBoundingClientRect();
      const wide = el.classList.contains('hl') ? Math.max(...[...el.getClientRects()].map(x => x.right), el.scrollWidth + r.left) : r.right;
      if (r.top < SAFE.top - 1 || r.bottom > SAFE.bottom + 1 || r.left < SAFE.left - 1 || wide > SAFE.right + 1)
        out.push(`${el.className} at ${Math.round(r.left)},${Math.round(r.top)}-${Math.round(wide)},${Math.round(r.bottom)}`);
    }
    return { size, out };
  }, { SAFE });
  const base = path.join(outDir, `cover-${c.id}`);
  await pg.screenshot({ path: base + '.jpg', type: 'jpeg', quality: 92 });
  await pg.screenshot({ path: base + '-grid.jpg', type: 'jpeg', quality: 92, clip: { x: GRID.x, y: GRID.y, width: GRID.w, height: GRID.h } });
  made.push({ c, file: base + '.jpg' });
  console.log(`${base}.jpg  headline ${fit.size}px${fit.out.length ? '  OUTSIDE SAFE BOX: ' + fit.out.join('; ') : ''}`);
  if (fit.out.length) bad++;
}

// The contact sheet: each cover whole with the Reels screen's UI bands shaded, the safe box solid and the 4:5 and 3:4
// crops dashed; then its grid crop at the size a phone shows it (about 130 wide).
const s = 300 / W;
const cols = made.map(({ c, file }) => {
  const b = fs.readFileSync(file).toString('base64');
  const box = (x, y, w, h, st) => `<div style="position:absolute;left:${x * s}px;top:${y * s}px;width:${w * s}px;height:${h * s}px;${st}"></div>`;
  return `<figure><figcaption>${esc(c.n)} · ${esc(c.name || c.id)}</figcaption>
    <div style="position:relative;width:300px"><img src="data:image/jpeg;base64,${b}" width="300">
      ${box(0, 0, W, UI.top, 'background:rgba(255,40,40,.22)')}${box(0, H - UI.bottom, W, UI.bottom, 'background:rgba(255,40,40,.22)')}
      ${box(W - UI.right, UI.top, UI.right, H - UI.top - UI.bottom, 'background:rgba(255,40,40,.22)')}
      ${box(GRID.x, GRID.y, GRID.w, GRID.h, 'outline:2px dashed #e6b93f')}${box(FEED.x, FEED.y, FEED.w, FEED.h, 'outline:2px dashed #4fb4ff')}
      ${box(SAFE.left, SAFE.top, SAFE.right - SAFE.left, SAFE.bottom - SAFE.top, 'outline:2px solid #7fd1a8')}</div>
    <div style="width:130px;height:173px;overflow:hidden;margin-top:14px;border-radius:2px"><img src="data:image/jpeg;base64,${b}" width="130" style="margin-top:${-GRID.y * 130 / W}px"></div></figure>`;
}).join('');
await pg.setViewportSize({ width: 1060, height: 600 });
await pg.setContent(`<!doctype html><meta charset="utf-8"><style>body{margin:0;padding:24px;background:#141216;color:#ecd9f6;font:600 18px system-ui}
  .row{display:flex;gap:40px}figure{margin:0}figcaption{margin-bottom:8px}img{display:block}p{font-weight:400;font-size:14px;color:#a99bb8;margin:16px 0 0}</style>
  <div class="row">${cols}</div><p>Red: Reels tabs, caption and buttons. Gold dashes: profile grid 3:4. Blue dashes: feed 4:5. Green: safe box.</p>`);
await pg.screenshot({ path: path.join(outDir, 'contact-sheet.png'), fullPage: true });
console.log(path.join(outDir, 'contact-sheet.png'));
await browser.close();
if (bad) { console.error(`${bad} cover(s) break the safe box`); process.exit(1); }
