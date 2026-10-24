// Loads a built board against an in-memory store and reads the Your eyes tab: one card per strand with open looks,
// older looks folded under the newest, and a yes that writes done + note to the step.
//   node board/checks/looks.mjs board/council-board.html [store.json] [shot.png]   (PLAYWRIGHT_MODULE=<path> for a global install)
// store.json is {lists: {...}, steps: {...}}; without it a small fixture is used.
import fs from 'fs'
const pw = await import('playwright').catch(() => import(process.env.PLAYWRIGHT_MODULE))
const { chromium } = pw.chromium ? pw : pw.default
const html = fs.readFileSync(process.argv[2], 'utf8')
const fixture = {
  lists: { boat: { title: 'Studio boat', repo: 'bars-engine' }, kit: { title: 'Room kit', repo: 'bars-engine' } },
  steps: {
    'boat-look-1': { list: 'boat', n: 1, do: 'Look at the old boat. Note yes or what is off.', href: 'https://example.com/old', due: '2026-10-27' },
    'boat-look-2': { list: 'boat', n: 2, do: 'Look at the new boat. Note yes or what is off.', href: 'https://example.com/new', due: '2026-10-28', lookTitle: 'The new boat' },
    'kit-look-01': { list: 'kit', n: 1, do: 'Open the nook.', href: 'https://example.com/nook', where: 'Links: nook https://example.com/nook · scroll https://example.com/scroll', due: '2026-10-24' },
    'kit-look-00': { list: 'kit', n: 0, do: 'Looked already.', href: 'https://example.com/x', done: true, doneAt: '2026-10-20T00:00:00Z', note: 'Yes' },
    'vercel-01': { list: 'kit', n: 2, do: 'Add a setting in Vercel.', due: '2026-10-24' },
  },
}
const store = process.argv[3] ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : fixture
const kinds = ['lists', 'steps', 'blockers', 'contacts', 'shows', 'picks', 'positions', 'questions', 'terms', 'causes',
  'steer', 'morning', 'ttv', 'seeds', 'pickup']
const S = { ...Object.fromEntries(kinds.map(k => [k, {}])), contacts: { ari: { name: 'Ari' } }, ...store }
const shim = `<script>(() => {
  const S = ${JSON.stringify(S).replace(/</g, '\\u003c')}; window.__writes = [];
  const snap = c => ({docs: Object.entries(S[c] || {}).map(([id, d]) => ({id, exists: true, data: () => d}))});
  const doc = p => { const [c, id] = p.split('/'); return {
    onSnapshot(cb){ cb({id, exists: !!(S[c]||{})[id], data: () => (S[c]||{})[id]}); return () => {}; },
    async set(d){ window.__writes.push([p, 'set', d]); }, async update(d){ window.__writes.push([p, 'update', d]); },
    async get(){ return {exists: false, data: () => null}; } }; };
  const db = { doc, collection: c => ({ onSnapshot(cb){ cb(snap(c)); return () => {}; } }) };
  window.claude = { use: async k => { if (k === 'db') return db; throw new Error('no ' + k); } };
})();</script>`
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch())
const page = await browser.newPage({ viewport: { width: 390, height: 900 } })
const errors = []
await page.addInitScript(() => { try { localStorage.setItem('ttv-skip', '1') } catch {} })
page.on('pageerror', e => errors.push(String(e)))
await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">${shim}</head><body>${html}</body></html>`)
await page.waitForTimeout(500)
await page.evaluate(() => document.getElementById('tab-looks').click())
const out = await page.evaluate(() => ({
  tabHidden: document.getElementById('tab-looks').hidden,
  count: document.getElementById('n-looks').textContent,
  cards: [...document.querySelectorAll('#looks-open .ey-card')].map(c => ({ id: c.id.slice(3), title: c.querySelector('h3').textContent,
    go: (c.querySelector('.ey-go') || {}).href || '', links: c.querySelectorAll('.ey-links a').length,
    older: c.querySelectorAll('.ey-older li').length, still: !!c.querySelector('.ey-still img') })),
  seen: document.querySelectorAll('#looks-seen .ey-card').length,
  pageWidth: document.documentElement.scrollWidth,
}))
if (process.argv[4]) await page.screenshot({ path: process.argv[4], fullPage: true })
const first = out.cards[0] && out.cards[0].id
if (first) { await page.evaluate(id => document.querySelector(`[data-eyes="yes"][data-step="${id}"]`).click(), first); await page.waitForTimeout(100) }
out.writes = await page.evaluate(() => window.__writes.filter(w => w[0].startsWith('steps/')).map(([p, k, d]) => [p, k, d.done, d.note]))
out.errors = errors
await browser.close()
console.log(JSON.stringify(out))
