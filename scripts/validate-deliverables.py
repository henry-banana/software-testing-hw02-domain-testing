"""Read-only integrity checks for the HW02 submission, not a SUT test suite."""
from pathlib import Path
from urllib.parse import unquote
import collections, hashlib, json, os, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
errors, warnings = [], []

def require(condition, message):
    if not condition: errors.append(message)

def without_fences(text):
    output=[]; fence=None
    for line in text.splitlines():
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        if fence:
            if match and match[1][0]==fence[0] and len(match[1])>=len(fence): fence=None
            output.append('')
        elif match:
            fence=match[1];output.append('')
        else:output.append(line)
    return '\n'.join(output)

def slug(title):
    return re.sub(r'\s','-',re.sub(r'[^\w\s-]','',title.lower().strip()))

def anchors(p):
    txt=without_fences(p.read_text(encoding='utf-8-sig'))
    result=set(re.findall(r'<a id="([^"]+)"',txt))
    seen=collections.Counter()
    for title in re.findall(r'^#{1,6}\s+(.+)',txt,re.M):
        key=slug(title);suffix='-'+str(seen[key]) if seen[key] else '';seen[key]+=1;result.add(key+suffix)
    return result

files=list(ROOT.rglob('*.md'))
for p in files:
    if '.git' in p.parts: continue
    txt=without_fences(p.read_text(encoding='utf-8-sig'))
    for match in re.finditer(r'!?\[[^\n]*?\]\((<[^>]+>|[^\s)]+)\)',txt):
        dest=match[1].strip('<>')
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',dest):continue
        path,_,fragment=unquote(dest).partition('#');target=(p.parent/path).resolve() if path else p
        require(target.exists(),f'{p.relative_to(ROOT)}: missing link {dest}')
        if target.is_file() and target.suffix=='.md' and fragment:
            require(fragment in anchors(target),f'{p.relative_to(ROOT)}: missing anchor {dest}')

tc, raw={},{}
for p in (ROOT/'tests').glob('*.md'):
    txt=p.read_text(encoding='utf-8')
    for m in re.finditer(r'^## ([ABCD]-(?:API|UI)-\d+)\n(.*?)(?=^## |\Z)',txt,re.M|re.S):
        status=re.search(r'^\| Status \| ([A-Z ]+) \|$',m[2],re.M)
        require(status is not None,f'{m[1]}: no status')
        if status:
            require(m[1] not in tc,'Duplicate TC '+m[1]);tc[m[1]]=status[1]
for p in (ROOT/'evidence/execution').glob('?-api.md'):
    text=p.read_text(encoding='utf-8')
    require('Original SUT files unchanged after run: **PASS**' in text,f'{p.name}: preservation check absent')
    for m in re.finditer(r'^## ([ABCD]-API-\d+)\n(.*?)(?=^## |\Z)',text,re.M|re.S):
        state=re.search(r'^Status: (.+)',m[2],re.M)[1]
        trace=json.loads(re.search(r'```json\s*(.*?)```',m[2],re.S)[1])
        raw[m[1]]=state
        require(tc.get(m[1])==state,f'{m[1]} status differs between case and raw')
        require(bool(trace),m[1]+': no trace')
    sut=Path(os.environ.get('HW02_SUT',str(ROOT.parent/'eshop-sut')))
    for rel,digest in re.findall(r'^\| ([^|]+) \| ([0-9a-f]{64}) \|$',text,re.M):
        source=sut/rel
        if source.exists():require(hashlib.sha256(source.read_bytes()).hexdigest()==digest,p.name+': current SUT hash differs for '+rel)
require(len(tc)==114,f'Expected114 unique TC-IDs, got{len(tc)}')
require(len(raw)==81,f'Expected81 raw API IDs, got{len(raw)}')
require(collections.Counter(raw.values())=={'PASS':37,'FAIL':42,'OBSERVATION':2},'Unexpected API outcome distribution')
total=collections.Counter(tc.values())
require(total=={'PASS':49,'FAIL':56,'OBSERVATION':4,'INCOMPLETE':5},'Unexpected consolidated outcomes: '+str(dict(total)))
for name in ['README.md','23120262_Report.md']:
    body=(ROOT/name).read_text(encoding='utf-8')
    require('| **Tổng** | 114 | 109 | 49 | 56 | 4 | 5 | 0 |' in body,name+': summary drift')

bugfiles={p.stem:p for p in (ROOT/'bugs').glob('*.md') if re.fullmatch(r'BUG-[ABCD]\d{2}',p.stem)}
require(len(bugfiles)==18,f'Expected18 bug groups, got{len(bugfiles)}')
for id,state in tc.items():
    if state!='FAIL':continue
    casefile=next(p for p in (ROOT/'tests').glob('*.md') if f'## {id}\n' in p.read_text(encoding='utf-8'))
    block=re.search(r'^## '+id+r'\n(.*?)(?=^## |\Z)',casefile.read_text(encoding='utf-8'),re.M|re.S)[1]
    bugs=re.search(r'^\| Bug \| (.+) \|$',block,re.M)[1]
    require(bugs in bugfiles,id+': missing mapped bug '+bugs)
    if bugs in bugfiles:require(id in bugfiles[bugs].read_text(encoding='utf-8'),id+': bug missing reverse trace')
for bug,p in bugfiles.items():
    for heading in ['Preconditions','Steps to Reproduce','Expected Result','Actual Result','Impact','Root Cause','Screenshots','Regression']:
        require(heading.lower() in p.read_text(encoding='utf-8').lower(),bug+': missing '+heading)
for feature in 'ABCD':
    analysis=next((ROOT/'reports').glob(feature+'-*-domain.md')) if feature!='D' else ROOT/'reports/D-mobile-domain.md'
    text=analysis.read_text(encoding='utf-8')
    domain_rows=re.findall(r'^\| ('+feature+r'-D\d+) \|.*$',text,re.M)
    require(bool(domain_rows),feature+': no stable domain IDs')
    for id in tc:
        if id.startswith(feature+'-'):require(id in text,feature+': uncovered TC in domain/analysis '+id)

photos=[p for p in (ROOT/'evidence/screenshots').rglob('*') if p.is_file()]
require(len(photos)==68,f'Expected68 screenshots, got{len(photos)}')
register=(ROOT/'evidence/README.md').read_text(encoding='utf-8')
for p in photos:
    require(hashlib.sha256(p.read_bytes()).hexdigest() in register,'Photo hash absent: '+p.name)

reflection=next((ROOT/'ai-audit').glob('[[]AI-04]*'))
paragraph=re.search(r'## 2\. AI Critique.*?\n\n(.*?)(?=\n\n)',reflection.read_text(encoding='utf-8'),re.S)[1]
require(200<=len(paragraph.split())<=300,'AI Critique outside200–300 words')
for n,label in [('02','AI Audit Report'),('03','AI Disclosure Form'),('04','AI Reflective Statement'),('05','AI Privacy Checklist')]:
    require((ROOT/'ai-audit'/f'[AI-{n}] - FIT@HCMUS - {label}_Vn.md').exists(),'Template filename mismatch AI-'+n)
require(not (ROOT/'interactions').exists(),'Unexpected interactions directory')
require(not (ROOT/'TASKS.md').exists(),'Coordination TASKS should stay outside submission')
for script in ['cases.cjs','runtime.cjs','run-api.cjs','show-bug.cjs','export-git-log.cjs']:
    r=subprocess.run(['node','--check',str(ROOT/'scripts'/script)],capture_output=True,text=True)
    require(r.returncode==0,script+': '+r.stderr)

logpath=ROOT/'git-commit-log.txt'
if logpath.exists():
    text=logpath.read_text(encoding='utf-8');m=re.search(r'^Snapshot HEAD: ([0-9a-f]{40})',text,re.M)
    require(m is not None,'Git log has no declared snapshot boundary')
    if m:
        expected=subprocess.check_output(['git','log',m[1],'--date=iso-strict','--format=commit %H%nAuthor: %an%nDate: %ad%n%n    %s%n'],cwd=ROOT,encoding='utf-8').strip()
        require(expected in text,'Exported Git log differs from actual declared revision')
else:errors.append('Missing git-commit-log.txt')

warnings += ['5 UI TCs incomplete: A-UI-07, B-UI-06, C-UI-02, C-UI-06, D-UI-12',
             'Group Issues, Issue screenshots and 11 API-only bug screenshots pending',
             'Video has requested temporary URL; student will replace it',
             'Student final human review, lecture comparison, PDF/ZIP remain outside automated verification']
for error in errors:print('FAIL:',error)
print(json.dumps({'technical_integrity':'FAIL' if errors else 'PASS','test_cases':len(tc),'api_cases':len(raw),'outcomes':dict(total),'bugs':len(bugfiles),'screenshots':len(photos),'critique_words':len(paragraph.split()),'errors':len(errors)},ensure_ascii=False))
for warning in warnings:print('PENDING:',warning)
sys.exit(1 if errors else 0)
