const fs = require('node:fs');
const path = require('node:path');
const {execFileSync} = require('node:child_process');
const root = path.resolve(__dirname, '..');
const git = args => execFileSync('git', args, {cwd: root, encoding: 'utf8'}).trim();
const head = git(['rev-parse', 'HEAD']);
const log = git(['log', '--date=iso-strict', '--format=commit %H%nAuthor: %an%nDate: %ad%n%n    %s%n']);
fs.writeFileSync(path.join(root, 'git-commit-log.txt'),
  `Git Commit Log — HW02\n\nSnapshot HEAD: ${head}\nExported at UTC: ${new Date().toISOString()}\n` +
  'Scope: complete reachable history through Snapshot HEAD. The later commit recording this export itself is outside that boundary.\n' +
  'Dates are actual Git dates; no historical steps were recreated from the old standalone log.\n\n' + log + '\n');
console.log('Exported actual Git history through ' + head);
