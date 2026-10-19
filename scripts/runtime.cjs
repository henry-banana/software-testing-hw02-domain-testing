// Runtime adapter: source bytes are copied unchanged; only port and test clock differ.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {spawn} = require('node:child_process');
const {createRequire} = require('node:module');
const repo = path.resolve(__dirname, '..');
const sut = path.resolve(process.env.HW02_SUT || path.join(repo, '..', 'eshop-sut'));
const runtime = path.resolve(process.env.HW02_RUNTIME || path.join(repo, '..', '.hw02-runtime'));
const fixed = '2026-10-19T08:00:00.000Z';
function hash(file) { return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'); }
function dependency(name) { return createRequire(path.join(sut, 'backend', 'package.json'))(name); }
function stage(label='api') {
  // Refuse to stage on the original backend: database.js drops tables at import.
  if(!/^[a-z-]+$/.test(label))throw Error('Invalid runtime label');
  const target = path.join(runtime, label, 'backend');
  if (target.toLowerCase() === path.join(sut, 'backend').toLowerCase() || !target.startsWith(runtime + path.sep)) throw Error('Unsafe runtime path');
  fs.mkdirSync(target, {recursive:true});
  for (const file of ['server.js','database.js']) fs.copyFileSync(path.join(sut,'backend',file),path.join(target,file));
  return target;
}
function start(port=3100, freeze=true, label='api') {
  const target=stage(label);
  const child=spawn(process.execPath,[__filename,'child'],{env:{...process.env,NODE_PATH:path.join(sut,'backend','node_modules'),HW02_SERVER:path.join(target,'server.js'),HW02_PORT:String(port),HW02_CLOCK:freeze?fixed:''},stdio:['ignore','pipe','pipe']});
  let log=''; child.stdout.on('data',d=>log+=d);child.stderr.on('data',d=>log+=d);
  child.on('error',e=>log+=String(e));
  return {child, target, log:()=>log};
}
async function ready(port, child) {
  for(let i=0;i<100;i++) {
    if(child.exitCode!==null)throw Error('Backend exited '+child.exitCode);
    try {const r=await fetch(`http://127.0.0.1:${port}/api/products`,{signal:AbortSignal.timeout(500)});const a=await r.json();if(Array.isArray(a)&&a.length===5)return;}catch{}
    await new Promise(r=>setTimeout(r,100));
  }
  throw Error('Backend readiness timeout');
}
if(require.main===module&&process.argv[2]==='child'){
  require('node:module').Module._initPaths();
  if(process.env.HW02_CLOCK){
    const RealDate=Date, now=RealDate.parse(process.env.HW02_CLOCK);
    global.Date=class extends RealDate{constructor(...args){super(...(args.length?args:[now]));}static now(){return now;}};
  }
  const http=require('node:http'),listen=http.Server.prototype.listen;
  http.Server.prototype.listen=function(...args){args[0]=Number(process.env.HW02_PORT);return listen.apply(this,args);};
  require(process.env.HW02_SERVER);
}else module.exports={repo,sut,runtime,fixed,hash,dependency,start,ready};
