// Loads a built board against an in-memory store, empty and then filled, and prints what Your steps and Outreach say.
// An empty store must read as a fault, never as "Nothing waiting on you" (council/postmortems/2026-10-20-steps-outreach-blank.md).
//   node board/checks/store_fault.mjs board/council-board.html   (PLAYWRIGHT_MODULE=<path> for a global install)
import fs from 'fs'
const pw = await import('playwright').catch(() => import(process.env.PLAYWRIGHT_MODULE))
const { chromium } = pw.chromium ? pw : pw.default
const html = fs.readFileSync(process.argv[2], 'utf8')
const kinds = ['lists', 'steps', 'blockers', 'contacts', 'shows', 'picks', 'positions', 'questions', 'terms', 'causes',
  'steer', 'morning', 'ttv', 'seeds', 'pickup']
const shim = store => `<script>(() => {
  const S = ${JSON.stringify(store)};
  const snap = c => ({docs: Object.entries(S[c] || {}).map(([id, d]) => ({id, exists: true, data: () => d}))});
  const doc = p => { const [c, id] = p.split('/'); return {
    onSnapshot(cb){ cb({id, exists: !!(S[c]||{})[id], data: () => (S[c]||{})[id]}); return () => {}; },
    async set(){}, async update(){}, async get(){ return {exists: false, data: () => null}; } }; };
  const db = { doc, collection: c => ({ onSnapshot(cb){ cb(snap(c)); return () => {}; } }) };
  window.claude = { use: async k => { if (k === 'db') return db; throw new Error('no ' + k); } };
})();</script>`
const empty = Object.fromEntries(kinds.map(k => [k, {}]))
const filled = { ...empty, lists: { a: { title: 'A list', repo: 'x', why: 'test' } },
  steps: { 'a-01': { list: 'a', n: 1, do: 'Do the thing', due: '2026-10-21', device: 'phone' } },
  contacts: { ari: { name: 'Ari' } } }
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch())
const out = {}
for (const [name, store] of Object.entries({ empty, filled })) {
  const page = await browser.newPage()
  const errors = []
  page.on('pageerror', e => errors.push(String(e)))
  await page.setContent(`<!doctype html><html><head><meta charset="utf-8">${shim(store)}</head><body>${html}</body></html>`)
  await page.evaluate(() => { try { localStorage.setItem('ttv-skip', '1') } catch {} })
  await page.waitForTimeout(500)
  const read = id => page.$eval(id, e => ({ hidden: e.hidden, fault: e.classList.contains('store-fault'), text: e.textContent }))
  out[name] = { steps: await read('#steps-empty'), outreach: await read('#oc-empty'), errors }
  await page.close()
}
await browser.close()
console.log(JSON.stringify(out))
