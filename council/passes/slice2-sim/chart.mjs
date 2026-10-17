import fs from 'fs';
const root = process.argv[2];
const { createFight, act, outcome } = await import(root + '/slice/fight.js');
const { odds } = await import(root + '/slice/offering.js');
const cfg = JSON.parse(fs.readFileSync(root + '/data/slice.json'));
const spirit = JSON.parse(fs.readFileSync(root + '/data/spirits.json')).records[0];
const A = ['wood','fire','earth','metal','water'];
const name = { wood:'controls', fire:'generates', earth:'same', metal:'generatedBy', water:'controlledBy' };
let best = [], all = 0;
function run(seq) { const f = createFight(cfg, spirit); for (const a of seq) { act(f, a, cfg, spirit); if (f.over) return null; } return f; }
function rec(seq, n) {
  if (seq.length) { const f = run(seq); if (!f) return; all++; const p = odds(outcome(f), 'fertilize', cfg, 0);
    best.push({ seq: seq.map(a => name[a]).join(' > '), p: +p.toFixed(3), turns: seq.length, hp: f.player.hp }); }
  if (seq.length < n) for (const a of A) rec([...seq, a], n);
}
rec([], 6);
best.sort((a, b) => b.p - a.p || a.turns - b.turns);
console.log('sequences that end alive:', all);
console.log('top 8:'); best.slice(0, 8).forEach(b => console.log(' ', b.p, b.turns, 'hp', b.hp, b.seq));
const only = s => best.filter(b => b.seq.split(' > ').every(x => x === s)).sort((a,b)=>b.p-a.p)[0];
for (const s of Object.values(name)) console.log('only', s, '->', JSON.stringify(only(s)));
const without = s => best.filter(b => !b.seq.includes(s))[0];
console.log('best without same/generatedBy:', JSON.stringify(best.filter(b => !/same|generatedBy/.test(b.seq))[0]));
