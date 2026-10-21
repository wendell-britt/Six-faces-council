import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
const out = process.argv[2];
// streaks, seeded
let s = 7; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
const cols = ['#ff2d55', '#4fb3ff', '#e6b93f', '#2fbf71', '#ffffff'];
let streaks = '';
for (let i = 0; i < 90; i++) {
  const x = Math.round(r() * 1080), y = Math.round(r() * 1920), h = 80 + Math.round(r() * 320), c = cols[Math.floor(r() * cols.length)];
  const inText = x > 50 && x < 930 && ((y + h > 300 && y < 380) || (y + h > 840 && y < 1530));
  if (inText) continue;
  streaks += `<rect x="${x}" y="${y}" width="5" height="${h}" rx="2.5" fill="${c}" opacity="${(0.18 + r() * 0.35).toFixed(2)}"/>`;
}
const hex = (cx, cy, R) => { const p = []; for (let k = 0; k < 6; k++) { const a = Math.PI / 6 + k * Math.PI / 3; p.push(`${(cx + R * Math.cos(a)).toFixed(1)},${(cy + R * Math.sin(a)).toFixed(1)}`); } return p.join(' '); };
const html = `<!doctype html><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@600;700;800&family=Space+Mono:wght@700&display=block');
*{box-sizing:border-box;margin:0}html,body{width:1080px;height:1920px;overflow:hidden;background:#0a090e}
.t{position:relative;width:1080px;height:1920px;color:#fff;font-family:Jost,sans-serif}
.safe{position:absolute;left:80px;top:310px;width:820px;height:1190px;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center}
.kick{font:700 24px 'Space Mono',monospace;letter-spacing:.22em;color:#ff2d55}
.mark{font:800 44px Jost;letter-spacing:-.01em}.mark b{color:#e6b93f;font-weight:800}
.art{flex:1 1 auto;position:relative;margin:24px 0 30px}
.qm{font:700 190px Georgia,serif;color:#ff2d55;line-height:.6;height:70px;text-shadow:0 0 24px rgba(255,45,85,.6)}
.hl{font-weight:800;font-size:92px;line-height:1.0;letter-spacing:-.02em}
.hl .g{color:#e6b93f}
.foot{display:flex;justify-content:space-between;align-items:flex-end;margin-top:44px}
.guest{display:flex;gap:22px;align-items:center}
.badge{width:78px;height:78px}
.gn{font:800 42px Jost}.gs{font:600 28px Jost;color:#c9c3d6}
.clip{font:700 24px 'Space Mono',monospace;letter-spacing:.18em;color:#e6b93f;text-align:right;line-height:1.6}
</style><div class="t">
<svg width="1080" height="1920" style="position:absolute;inset:0"><defs>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="14" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
<clipPath id="cr"><polygon points="${hex(430, 600, 200)}"/></clipPath></defs>
<g filter="url(#soft)">${streaks}</g>
<polygon points="${hex(650, 600, 200)}" clip-path="url(#cr)" fill="#e6b93f" opacity=".32"/>
<polygon points="${hex(430, 600, 200)}" fill="none" stroke="#ff2d55" stroke-width="22" stroke-linejoin="round" filter="url(#glow)"/>
<polygon points="${hex(650, 600, 200)}" fill="none" stroke="#4fb3ff" stroke-width="22" stroke-linejoin="round" filter="url(#glow)"/>
</svg>
<div class="safe">
 <div class="top"><div class="kick">EP 01 · THE PODCAST</div><div class="mark">FLIRT<b>CRAFT</b></div></div>
 <div class="art"></div>
 <div class="qm">“</div>
 <div class="hl">Anywhere else,<br>I literally cannot<br>tell that I have<br><span class="g">permission<br>to flirt.</span></div>
 <div class="foot">
  <div class="guest"><svg class="badge" viewBox="0 0 80 80"><polygon points="${hex(40, 40, 34)}" fill="none" stroke="#e6b93f" stroke-width="4"/><text x="40" y="48" text-anchor="middle" font-family="Jost" font-weight="800" font-size="22" fill="#e6b93f">FC</text></svg>
   <div><div class="gn">QC</div><div class="gs">Writer, back from SlutCon</div></div></div>
  <div class="clip">CLIP 2<br>FLIRTCRAFT.APP</div>
 </div>
</div></div>`;
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await pg.setContent(html, { waitUntil: 'networkidle' }); await pg.evaluate(() => document.fonts.ready);
const chk = await pg.evaluate(() => { const o = []; document.querySelectorAll('.safe *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width && (r.left < 79 || r.right > 901 || r.top < 309 || r.bottom > 1501)) o.push(e.className + ' ' + JSON.stringify([r.left, r.top, r.right, r.bottom])); }); return o; });
console.log('outside safe box:', chk.length ? chk : 'none');
await pg.screenshot({ path: `${out}/cover-clip2-permission-to-flirt.jpg`, type: 'jpeg', quality: 92 });
await pg.screenshot({ path: `${out}/cover-clip2-permission-to-flirt-grid.jpg`, type: 'jpeg', quality: 92, clip: { x: 0, y: 240, width: 1080, height: 1440 } });
await b.close();
