const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const id = process.argv[2];
if (!/^BUG-[ABCD]\d{2}$/.test(id || '')) throw Error('Usage: node scripts/show-bug.cjs BUG-B03');
const report = fs.readFileSync(path.join(root, 'bugs', id + '.md'), 'utf8');
const representative = report.match(/## 5\. Actual Result và hậu điều kiện\n([\s\S]*?)\n## 6\./);
console.log(id + ' — DISPLAY OF CAPTURED EVIDENCE, NOT A NEW SUT EXECUTION\n');
console.log(representative ? representative[1] : report);
