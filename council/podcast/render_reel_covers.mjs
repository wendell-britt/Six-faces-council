// Renders Instagram Reel covers for a podcast episode's clips, in the same look as the YouTube thumbnails
// (render_thumbnails.mjs). Part of step 6 of the podcast episode move (council/moves/podcast-episode.md).
//
//   NODE_PATH=$(npm root -g) node council/podcast/render_reel_covers.mjs <spec.json> <out-dir>
//
// A cover is designed, like a thumbnail, never a frame from the video (Wendell, 2026-10-07: "don't want a frame
// from the video for the cover photo. This is essentially working as a youtube thumbnail but for the clips and for
// instagram"). Each clip in the spec becomes a 1080 x 1920 PNG. Everything that matters sits inside the middle
// 1080 x 1440, because the profile grid crops a Reel to 3:4, and above the bottom 380 pixels, where the feed lays
// its caption and buttons over the video. The contact sheet shows each cover at full height, as the grid crops it,
// and at grid size on a phone.
//
// A clip picks a motif (mirror, distance, hourglass, downhill, space, quote) and its words. *Stars* in a headline get the pink-to-gold.

import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';

const { chromium } = createRequire(import.meta.url)('playwright');

const W = 1080, H = 1920, GRID_TOP = 240, GRID_H = 1440;

const css = `
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@600;700;800&family=Space+Mono:wght@700&display=block');
*{box-sizing:border-box;margin:0}
html,body{width:${W}px;height:${H}px;overflow:hidden;background:#0b0910}
.t{position:relative;width:${W}px;height:${H}px;overflow:hidden;color:#f4f1ea;font-family:Jost,Futura,sans-serif;
  background:radial-gradient(120% 70% at 30% 0%,#241134,#0b0910 62%)}
.glow{position:absolute;border-radius:50%;filter:blur(12px)}
.kick{position:absolute;left:80px;top:${GRID_TOP + 70}px;font:700 26px 'Space Mono',monospace;letter-spacing:.22em;text-transform:uppercase;color:#ff5fa8}
.ep{position:absolute;right:80px;top:${GRID_TOP + 58}px;font:800 36px Jost;color:#0b0910;background:linear-gradient(135deg,#ffe08a,#e6b93f 55%,#c07a1e);
  padding:6px 20px;border-radius:12px}
.hl{position:absolute;left:80px;right:80px;font-weight:800;letter-spacing:-.025em;line-height:.98}
.grad{background:linear-gradient(100deg,#ff5fa8 10%,#e6b93f 90%);-webkit-background-clip:text;background-clip:text;color:transparent}
.guest{position:absolute;left:80px;font:700 42px Jost;color:#ecd9f6}
.guest b{color:#e6b93f;font-weight:800}
.clip{position:absolute;right:80px;font:700 26px 'Space Mono',monospace;letter-spacing:.18em;color:#a99bb8}
`;

function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function words(s) { return esc(s).replace(/\*([^*]+)\*/g, '<span class="grad">$1</span>').replace(/\n/g, '<br>'); }

const motifs = {
  // Two faces turned to each other; what each cannot see of itself shows only in the other.
  mirror: () => `
    <svg width="${W}" height="${H}" style="position:absolute;inset:0">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <ellipse cx="540" cy="620" rx="150" ry="215" fill="none" stroke="#cbc2d8" stroke-opacity=".35" stroke-width="7" stroke-dasharray="4 16" stroke-linecap="round"/>
      <path d="M330 470 q-80 70 -40 170 q20 40 -10 70 q40 10 30 60 q40 40 90 30" fill="none" stroke="#cbc2d8" stroke-opacity=".6" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M750 470 q80 70 40 170 q-20 40 10 70 q-40 10 -30 60 q-40 40 -90 30" fill="none" stroke="url(#g)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M440 620 L640 620" stroke="url(#g)" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 14"/>
    </svg>
    <div class="glow" style="width:760px;height:620px;left:160px;top:330px;background:radial-gradient(ellipse,rgba(255,95,168,.22),rgba(34,211,238,.10) 55%,transparent 74%)"></div>`,

  // A far globe, faded and struck; two people side by side, close enough to touch.
  distance: () => `
    <svg width="${W}" height="${H}" style="position:absolute;inset:0">
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
    <div class="glow" style="width:520px;height:360px;left:280px;top:560px;background:radial-gradient(ellipse,rgba(230,185,63,.30),transparent 70%)"></div>`,

  // An hourglass half run: the question is about duration, and the answer belongs to the one feeling it.
  hourglass: () => `
    <svg width="${W}" height="${H}" style="position:absolute;inset:0">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <path d="M400 400 H680 M400 840 H680" stroke="#cbc2d8" stroke-opacity=".6" stroke-width="10" stroke-linecap="round"/>
      <path d="M420 400 C 420 540, 530 580, 530 620 C 530 660, 420 700, 420 840 M660 400 C 660 540, 550 580, 550 620 C 550 660, 660 700, 660 840"
        fill="none" stroke="#cbc2d8" stroke-opacity=".6" stroke-width="8" stroke-linecap="round"/>
      <path d="M470 500 Q540 530 610 500 Q590 560 540 600 Q490 560 470 500 Z" fill="url(#g)" opacity=".9"/>
      <path d="M540 610 V790" stroke="#e6b93f" stroke-width="5" stroke-dasharray="3 12" stroke-linecap="round"/>
      <path d="M450 830 Q540 740 630 830 Z" fill="url(#g)" opacity=".9"/>
    </svg>
    <div class="glow" style="width:620px;height:560px;left:230px;top:340px;background:radial-gradient(ellipse,rgba(230,185,63,.22),transparent 70%)"></div>`,

  // Help that only flows one way: a stack of arrows down from a high step, nothing coming back up.
  downhill: () => `
    <svg width="${W}" height="${H}" style="position:absolute;inset:0">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <path d="M180 470 H460 V860 H900" fill="none" stroke="#cbc2d8" stroke-opacity=".55" stroke-width="9" stroke-linejoin="round"/>
      <circle cx="320" cy="420" r="40" fill="none" stroke="#ecd9f6" stroke-width="8"/>
      <circle cx="720" cy="810" r="40" fill="none" stroke="#ecd9f6" stroke-width="8"/>
      <g stroke="url(#g)" stroke-width="9" stroke-linecap="round" fill="none">
        <path d="M380 480 C 520 520, 600 620, 660 760"/><path d="M640 735 L662 768 L690 742"/>
      </g>
      <path d="M680 880 C 600 960, 420 900, 330 520" fill="none" stroke="#cbc2d8" stroke-opacity=".35" stroke-width="6" stroke-dasharray="4 18" stroke-linecap="round"/>
    </svg>
    <div class="glow" style="width:640px;height:420px;left:330px;top:540px;background:radial-gradient(ellipse,rgba(255,95,168,.20),transparent 70%)"></div>`,

  // An empty space with its border held open, and one small light arriving in it.
  space: () => `
    <svg width="${W}" height="${H}" style="position:absolute;inset:0">
      <defs><radialGradient id="r"><stop offset="0" stop-color="#ffe08a"/><stop offset=".5" stop-color="#e6b93f" stop-opacity=".7"/><stop offset="1" stop-color="#e6b93f" stop-opacity="0"/></radialGradient></defs>
      <circle cx="540" cy="650" r="210" fill="none" stroke="#cbc2d8" stroke-opacity=".5" stroke-width="7" stroke-dasharray="6 20" stroke-linecap="round"/>
      <circle cx="540" cy="650" r="270" fill="none" stroke="#ff5fa8" stroke-opacity=".35" stroke-width="4"/>
      <circle cx="590" cy="600" r="70" fill="url(#r)"/>
      <circle cx="590" cy="600" r="14" fill="#ffe08a"/>
    </svg>
    <div class="glow" style="width:760px;height:620px;left:160px;top:310px;background:radial-gradient(ellipse,rgba(217,168,240,.16),transparent 70%)"></div>`,

  // A line from the episode, quoted.
  quote: () => `
    <div class="glow" style="width:1000px;height:800px;left:-300px;top:120px;background:radial-gradient(ellipse,rgba(217,168,240,.26),transparent 70%)"></div>
    <div style="position:absolute;left:66px;top:${GRID_TOP + 150}px;font:700 340px Georgia,serif;color:#ff5fa8;opacity:.9;line-height:1">“</div>`,
};

function page(s, c) {
  const top = c.top || 900;
  return `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="t">
    ${(motifs[c.motif] || motifs.quote)()}
    <div class="kick">${esc(s.show)}</div><div class="ep">EP ${esc(s.episode)}</div>
    <div class="hl" style="top:${top}px;font-size:${c.size || 120}px">${words(c.headline)}</div>
    ${c.sub ? `<div class="guest" style="top:${c.subTop || 1420}px;color:#e6b93f">${esc(c.sub)}</div>` : ''}
    ${c.noGuest ? '' : `<div class="guest" style="top:${c.guestTop || 1530}px">with <b>${esc(s.guest)}</b></div>`}
    <div class="clip" style="top:${(c.guestTop || 1530) + 12}px">CLIP ${esc(c.n)}</div>
  </div></body></html>`;
}

const [specPath, outDir] = process.argv.slice(2);
if (!specPath || !outDir) { console.error('usage: node render_reel_covers.mjs <spec.json> <out-dir>'); process.exit(2); }
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const pg = await browser.newPage({ viewport: { width: W, height: H } });
const made = [];
for (const c of spec.clips) {
  await pg.setContent(page(spec, c), { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  const file = path.join(outDir, `cover-${c.id}.png`);
  await pg.screenshot({ path: file });
  made.push({ c, file });
  console.log(`${file}  ${(fs.statSync(file).size / 1024).toFixed(0)} KB`);
}

// The contact sheet: each cover whole with the grid's 3:4 crop marked, and at the grid's size on a phone (about 130 wide).
const cols = made.map(({ c, file }) => {
  const b = fs.readFileSync(file).toString('base64');
  const s = 300 / W;
  return `<figure><figcaption>${esc(c.n)} · ${esc(c.name || c.id)}</figcaption>
    <div style="position:relative;width:300px"><img src="data:image/png;base64,${b}" width="300">
      <div style="position:absolute;left:0;right:0;top:${GRID_TOP * s}px;height:${GRID_H * s}px;outline:2px dashed #e6b93f"></div></div>
    <div style="width:130px;height:173px;overflow:hidden;margin-top:14px;border-radius:2px"><img src="data:image/png;base64,${b}" width="130" style="margin-top:${-GRID_TOP * 130 / W}px"></div></figure>`;
}).join('');
await pg.setViewportSize({ width: 1060, height: 600 });
await pg.setContent(`<!doctype html><meta charset="utf-8"><style>body{margin:0;padding:24px;background:#141216;color:#ecd9f6;font:600 18px system-ui;display:flex;gap:40px}
  figure{margin:0}figcaption{margin-bottom:8px}img{display:block}</style>${cols}`);
await pg.screenshot({ path: path.join(outDir, 'contact-sheet.png'), fullPage: true });
console.log(path.join(outDir, 'contact-sheet.png'));
await browser.close();
