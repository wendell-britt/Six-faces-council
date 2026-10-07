// Renders YouTube thumbnails for a podcast episode from a spec file, in Mastering Allyship's look.
// Part of the podcast episode move (council/moves/podcast-episode.md).
//
//   node council/podcast/render_thumbnails.mjs <spec.json> <out-dir>
//
// The spec names the show, the episode, the guest and two to four concepts. Each concept picks a layout
// (question, ground or quote) and its words. Each concept becomes a 1280 x 720 PNG, the size YouTube asks for,
// plus one contact sheet that shows every draft at full size and at the size a phone's search results show.
// A concept may name a photo (a still from the video); the layout then puts it on the right.
//
// The palette and type are taken from the live /mastering-allyship page in bars-engine
// (src/app/mastering-allyship/page.tsx and src/styles/bars-tokens.css): the night violet ground, the
// pink-to-gold call to action, the cyan glow, Jost for display and Space Mono for the kicker.

import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';

// Loaded through require so NODE_PATH reaches a global install: NODE_PATH=$(npm root -g) node ...
const { chromium } = createRequire(import.meta.url)('playwright');

const W = 1280, H = 720;

const css = `
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@600;700;800&family=Space+Mono:wght@700&display=block');
*{box-sizing:border-box;margin:0}
html,body{width:${W}px;height:${H}px;overflow:hidden;background:#0b0910}
.t{position:relative;width:${W}px;height:${H}px;overflow:hidden;color:#f4f1ea;font-family:Jost,Futura,sans-serif;
  background:radial-gradient(125% 100% at 30% -10%,#241134,#0b0910 62%)}
.glow{position:absolute;border-radius:50%;filter:blur(10px)}
.kick{position:absolute;left:64px;top:52px;font:700 22px 'Space Mono',monospace;letter-spacing:.24em;text-transform:uppercase;color:#ff5fa8}
.ep{position:absolute;right:64px;top:44px;font:800 30px Jost;color:#0b0910;background:linear-gradient(135deg,#ffe08a,#e6b93f 55%,#c07a1e);
  padding:6px 18px;border-radius:10px}
.hl{position:absolute;left:64px;font-weight:800;letter-spacing:-.025em;line-height:.98}
.grad{background:linear-gradient(100deg,#ff5fa8 10%,#e6b93f 90%);-webkit-background-clip:text;background-clip:text;color:transparent}
.guest{position:absolute;left:64px;bottom:52px;font:700 34px Jost;color:#ecd9f6}
.guest b{color:#e6b93f;font-weight:800}
.photo{position:absolute;right:0;top:0;width:520px;height:${H}px;object-fit:cover;
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 30%);mask-image:linear-gradient(90deg,transparent,#000 30%)}
.line{position:absolute;left:0;right:0;height:3px}
`;

function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }

// Words wrapped in *stars* in a headline get the pink-to-gold gradient.
function words(s) { return esc(s).replace(/\*([^*]+)\*/g, '<span class="grad">$1</span>').replace(/\n/g, '<br>'); }

function photoTag(c, dir) {
  if (!c.photo) return '';
  const p = path.resolve(dir, c.photo);
  const b64 = fs.readFileSync(p).toString('base64');
  const mime = p.toLowerCase().endsWith('.png') ? 'image/png' : 'image/jpeg';
  return `<img class="photo" src="data:${mime};base64,${b64}">`;
}

const layouts = {
  // A question set large, the hook of the episode.
  question: (s, c, dir) => `
    <div class="glow" style="width:760px;height:520px;right:-160px;bottom:-180px;background:radial-gradient(ellipse,rgba(255,95,168,.34),rgba(34,211,238,.14) 52%,transparent 74%)"></div>
    ${photoTag(c, dir)}
    <div class="kick">${esc(s.show)}</div><div class="ep">EP ${esc(s.episode)}</div>
    <div class="hl" style="top:150px;font-size:${c.size || 118}px;max-width:${c.photo ? 760 : 1120}px">${words(c.headline)}</div>
    <div class="guest">with <b>${esc(s.guest)}</b></div>`,

  // The thesis drawn: a faded peak with a struck arrow above, a lit ground line with roots below.
  ground: (s, c, dir) => `
    <svg width="${W}" height="${H}" style="position:absolute;inset:0">
      <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#ff5fa8"/><stop offset="1" stop-color="#e6b93f"/></linearGradient></defs>
      <path d="M800 520 L1010 170 L1220 520" fill="none" stroke="#cbc2d8" stroke-opacity=".4" stroke-width="7" stroke-linejoin="round"/>
      <path d="M1010 160 L1010 60 M980 92 L1010 60 L1040 92" fill="none" stroke="#cbc2d8" stroke-opacity=".5" stroke-width="7" stroke-linecap="round"/>
      <path d="M960 80 L1060 140" stroke="#ff5fa8" stroke-width="8" stroke-linecap="round"/>
      <path d="M0 560 L${W} 560" stroke="url(#g)" stroke-width="6"/>
      ${[120, 300, 480, 660, 840, 1020, 1180].map((x, i) => `<path d="M${x} 560 q ${i % 2 ? 24 : -24} 50 ${i % 2 ? -8 : 8} 110" fill="none" stroke="#e6b93f" stroke-opacity=".55" stroke-width="4" stroke-linecap="round"/>`).join('')}
    </svg>
    <div class="glow" style="width:1400px;height:260px;left:-60px;top:440px;background:radial-gradient(ellipse,rgba(230,185,63,.22),transparent 70%)"></div>
    ${photoTag(c, dir)}
    <div class="kick">${esc(s.show)}</div><div class="ep">EP ${esc(s.episode)}</div>
    <div class="hl" style="top:150px;font-size:${c.size || 132}px;max-width:720px">${words(c.headline)}</div>
    <div class="guest" style="bottom:auto;top:${c.guestTop || 590}px">with <b>${esc(s.guest)}</b></div>`,

  // A line from the episode, quoted, with its speaker and what it is about.
  quote: (s, c, dir) => `
    <div class="glow" style="width:900px;height:600px;left:-260px;top:-260px;background:radial-gradient(ellipse,rgba(217,168,240,.26),transparent 70%)"></div>
    ${photoTag(c, dir)}
    <div class="kick">${esc(s.show)}</div><div class="ep">EP ${esc(s.episode)}</div>
    <div style="position:absolute;left:52px;top:70px;font:700 240px Georgia,serif;color:#ff5fa8;opacity:.9;line-height:1">“</div>
    <div class="hl" style="top:215px;font-size:${c.size || 112}px;max-width:${c.photo ? 760 : 1120}px">${words(c.headline)}</div>
    <div style="position:absolute;left:64px;top:${c.subTop || 470}px;font:700 40px Jost;color:#e6b93f">${esc(c.sub || '')}</div>
    <div class="guest">with <b>${esc(s.guest)}</b></div>`,
};

function page(s, c, dir) {
  const body = (layouts[c.layout] || layouts.question)(s, c, dir);
  return `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="t">${body}</div></body></html>`;
}

const [specPath, outDir] = process.argv.slice(2);
if (!specPath || !outDir) { console.error('usage: node render_thumbnails.mjs <spec.json> <out-dir>'); process.exit(2); }
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const specDir = path.dirname(path.resolve(specPath));
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const pg = await browser.newPage({ viewport: { width: W, height: H } });
const made = [];
for (const c of spec.concepts) {
  await pg.setContent(page(spec, c, specDir), { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  const file = path.join(outDir, `thumb-${c.id}.png`);
  await pg.screenshot({ path: file });
  made.push({ c, file });
  console.log(`${file}  ${(fs.statSync(file).size / 1024).toFixed(0)} KB`);
}

// The contact sheet: each draft large, and again at 246 x 138, about the size a phone's search results show.
const imgs = made.map(({ c, file }) => {
  const b = fs.readFileSync(file).toString('base64');
  return `<figure><figcaption>${esc(c.id.toUpperCase())} · ${esc(c.name || c.layout)}</figcaption>
    <div class="row"><img src="data:image/png;base64,${b}" width="640"><img src="data:image/png;base64,${b}" width="246"></div></figure>`;
}).join('');
await pg.setViewportSize({ width: 960, height: 400 });
await pg.setContent(`<!doctype html><meta charset="utf-8"><style>body{margin:0;padding:24px;background:#141216;color:#ecd9f6;font:600 18px system-ui}
  figure{margin:0 0 28px}figcaption{margin-bottom:8px}.row{display:flex;gap:24px;align-items:flex-start}img{border-radius:6px}</style>${imgs}`);
await pg.screenshot({ path: path.join(outDir, 'contact-sheet.png'), fullPage: true });
console.log(path.join(outDir, 'contact-sheet.png'));
await browser.close();
