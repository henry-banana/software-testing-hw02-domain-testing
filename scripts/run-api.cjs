const fs=require('node:fs');
const path=require('node:path');
const {once}=require('node:events');
const {cases}=require('./cases.cjs');
const rt=require('./runtime.cjs');
const feature=process.argv[2];
if(!['A','B','C','D'].includes(feature))throw Error('Usage: node scripts/run-api.cjs A|B|C|D');
const port=3100,origin=`http://127.0.0.1:${port}`;
const started=new Date().toISOString();
const sourceFiles=['backend/server.js','backend/database.js','backend/database.sqlite','frontend-web/src/pages/Profile.jsx','frontend-web/src/pages/Checkout.jsx','frontend-admin/src/App.jsx','frontend-mobile/App.js'];
const hashes=Object.fromEntries(sourceFiles.map(f=>[f,rt.hash(path.join(rt.sut,f))]));
const clean=(value)=>Array.isArray(value)?value.map(clean):value&&typeof value==='object'?Object.fromEntries(Object.entries(value).filter(([k])=>!['password','token','reset_token','authorization'].includes(k.toLowerCase())).map(([k,v])=>[k,clean(v)])):value;
let database,server,trace=[],tokens={};
async function request(method,url,input,auth='user',record=true){
  const headers={'Content-Type':'application/json'};
  if(auth!=='none')headers.Authorization='Bearer '+(auth==='invalid'?'not-a-valid-jwt':tokens[auth]);
  const response=await fetch(origin+url,{method,headers,...(input===undefined?{}:{body:JSON.stringify(input)}),signal:AbortSignal.timeout(5000)});
  const raw=await response.text();let body;try{body=JSON.parse(raw);}catch{body=raw;}
  if(record)trace.push({method,url,authentication:auth,input:clean(input??null),status:response.status,body:clean(body)});
  return {status:response.status,body};
}
function sql(query,args=[]){return new Promise((resolve,reject)=>database.run(query,args,function(err){err?reject(err):resolve({id:this.lastID,changes:this.changes});}));}
async function fixtures(tc){
  await sql('DELETE FROM coupon_usage');
  await sql('DELETE FROM coupons');
  for(const row of [
    ['SAVE10','percent',10,300000,'2099-12-31',1,1],['BIGBUY','fixed',50000,500000,'2099-12-31',1,1],
    ['VIP100','fixed',100000,300000,'2099-12-31',1,2],['EXPIRED','percent',20,100000,'2020-01-01',1,1],
    ['OFF','fixed',10000,0,'2099-12-31',0,1],['TIME','fixed',10000,0,new Date(Date.parse(rt.fixed)+(tc.expiry??1000)).toISOString(),1,1],
    ['P100','percent',100,0,'2099-12-31',1,1],['DELETE_ME','fixed',1,0,'2099-12-31',1,1]
  ])await sql('INSERT INTO coupons(code,type,discount_value,min_order_amount,expired_at,is_active,max_uses_per_user) VALUES(?,?,?,?,?,?,?)',row);
  await sql("UPDATE users SET name='Test User',phone='0912345678',shipping_address='1 Test Street',role='user' WHERE id=2");
  await sql("UPDATE users SET name='Other User',phone='0987654321',shipping_address='Other Street',role='user' WHERE id=3");
  for(let i=0;i<(tc.used||0);i++)await sql("INSERT INTO coupon_usage(coupon_id,user_id) SELECT id,2 FROM coupons WHERE code='VIP100'");
}
function ok(r){return r.status>=200&&r.status<300;}
function denied(r){return r.status===401||r.status===403;}
function rejection(r){return r.status>=400&&r.status<500;}
async function execute(tc){
  switch(tc.kind){
    case 'profile':{
      const r=await request('PUT','/api/users/me',tc.input);
      const read=await request('GET','/api/users/me');
      const matches=Object.entries(tc.input).every(([k,v])=>read.body[k]===v);
      return tc.valid?ok(r)&&matches:rejection(r)&&read.body.phone==='0912345678';
    }
    case 'profile-role':{
      await request('PUT','/api/users/me',tc.input);
      return (await request('GET','/api/users/me')).body.role==='user';
    }
    case 'profile-owner':{
      const r=await request('PUT','/api/users/me',tc.input);
      const own=await request('GET','/api/users/me');const other=await request('GET','/api/users/me',undefined,'other');
      return ok(r)&&own.body.name==='Owner Only'&&other.body.name==='Other User';
    }
    case 'profile-auth':{
      const r=await request('PUT','/api/users/me',tc.input,tc.auth);
      const read=await request('GET','/api/users/me');
      return denied(r)&&read.body.phone==='0912345678';
    }
    case 'profile-read':return denied(await request('GET','/api/users/me',undefined,tc.auth));
    case 'coupon':{
      const r=await request('POST','/api/apply-coupon',tc.input,tc.auth);
      if(tc.rejectAuth)return denied(r);
      if(tc.reject)return rejection(r);
      return ok(r)&&Math.abs(r.body.discount_amount-tc.money[0])<1e-6&&Math.abs(r.body.final_amount-tc.money[1])<1e-6;
    }
    case 'admin-create':{
      const before=await request('GET','/api/coupons',undefined,'admin');
      const r=await request('POST','/api/admin/coupons',tc.input,tc.auth);
      const after=await request('GET','/api/coupons',undefined,'admin');
      if(!tc.valid)return (tc.authCase?denied(r):r.status>=400)&&after.body.length===before.body.length;
      const row=after.body.find(x=>x.id===r.body.id);
      return ok(r)&&row&&Object.entries(tc.input).every(([k,v])=>row[k]===v);
    }
    case 'admin-list':{
      const r=await request('GET','/api/coupons',undefined,tc.auth);
      return tc.valid?ok(r)&&Array.isArray(r.body):denied(r);
    }
    case 'admin-delete':{
      const before=await request('GET','/api/coupons',undefined,'admin');
      const id=before.body.find(x=>x.code==='DELETE_ME').id;
      const r=await request('DELETE',`/api/admin/coupons/${id}`,undefined,tc.auth);
      const after=await request('GET','/api/coupons',undefined,'admin');
      const removed=!after.body.some(x=>x.id===id);
      return tc.valid?ok(r)&&removed&&after.body.length===before.body.length-1:denied(r)&&!removed;
    }
    case 'product':{
      const r=await request('GET',`/api/products/${tc.input.id}`,undefined,'none');
      if(tc.observation)return true;
      const expected=tc.input.id===1?['iPhone 15 Pro Max',30000000]:['Samsung Galaxy S24 Ultra',28000000];
      return ok(r)&&r.body.name===expected[0]&&Number(r.body.price)===expected[1]&&typeof r.body.description==='string'&&typeof r.body.imageUrl==='string'&&r.body.category_id===1;
    }
    default:throw Error('Unsupported kind '+tc.kind);
  }
}
(async()=>{
  const results=[];
  try{
    // Never attach to a pre-existing listener: every run owns its runtime.
    const net=require('node:net');await new Promise((resolve,reject)=>{const p=net.createServer();p.once('error',reject);p.listen(port,'127.0.0.1',()=>p.close(resolve));});
    server=rt.start(port,true);await rt.ready(port,server.child);
    const sqlite3=rt.dependency('sqlite3').verbose();
    database=await new Promise((resolve,reject)=>{const db=new sqlite3.Database(path.join(server.target,'database.sqlite'),e=>e?reject(e):resolve(db));});
    await sql("INSERT INTO users(id,name,email,password,role,phone,shipping_address) VALUES(3,'Other User','other@hw02.invalid','Test1234!','user','0987654321','Other Street')");
    for(const[role,email,password]of[['admin','admin@eshop.com','Admin123!'],['user','test@eshop.com','Test1234!'],['other','other@hw02.invalid','Test1234!']]){
      const r=await request('POST','/api/login',{email,password},'none',false);if(!r.body.token)throw Error('Fixture login failed '+role);tokens[role]=r.body.token;
    }
    const source=fs.readFileSync(path.join(rt.sut,'backend','server.js'),'utf8');
    const secret=source.match(/const SECRET_KEY = "([^"]+)"/)[1];
    tokens.expired=rt.dependency('jsonwebtoken').sign({id:2,role:'user',exp:Math.floor(Date.parse(rt.fixed)/1000)-1},secret,{noTimestamp:true});
    for(const tc of cases.filter(x=>x.feature===feature&&x.kind!=='manual')){
      trace=[];const at=new Date().toISOString();let status,reason='';
      try{await fixtures(tc);const passed=await execute(tc);status=tc.observation?'OBSERVATION':passed?'PASS':'FAIL';}catch(e){status='BLOCKED';reason=String(e);}
      results.push({id:tc.id,status,at,expected:tc.expected,bug:status==='FAIL'?tc.bug:null,reason,trace});
      console.log(tc.id,status);
    }
  }finally{
    if(database)await new Promise(r=>database.close(r));
    if(server&&server.child.exitCode===null&&server.child.signalCode===null){const closed=once(server.child,'close');server.child.kill();await closed;}
  }
  const unchanged=Object.entries(hashes).every(([f,h])=>rt.hash(path.join(rt.sut,f))===h);
  const count={};for(const r of results)count[r.status]=(count[r.status]||0)+1;
  let md=`# ${feature} — Raw API execution\n\nStarted (UTC): ${started}\n\nFinished (UTC): ${new Date().toISOString()}\n\nHost timezone labels use UTC explicitly; add 07:00 for Asia/Saigon. SUT clock frozen at ${rt.fixed}; runner timestamp uses real clock.\n\nOrigin: ${origin}. Byte-identical copied backend source; HTTP listen port and global Date adapter only. SQLite fixtures are test setup; assertions observe public API. Password/token fields are omitted from evidence.\n\nOriginal SUT files unchanged after run: **${unchanged?'PASS':'FAIL'}**.\n\n## Source hashes\n\n| File | SHA-256 before (= after when PASS) |\n|---|---|\n`;
  for(const[f,h]of Object.entries(hashes))md+=`| ${f} | ${h} |\n`;
  md+=`\n## Results\n\n| ID | Status | Bug group |\n|---|---|---|\n`;
  for(const r of results)md+=`| ${r.id} | ${r.status} | ${r.bug||'—'} |\n`;
  for(const r of results)md+=`\n## ${r.id}\n\nStatus: ${r.status}\n\nTimestamp (UTC): ${r.at}\n\nExpected: ${r.expected}\n\n${r.reason?'Blocker: '+r.reason+'\n\n':''}Requests/responses (sanitized):\n\n\`\`\`json\n${JSON.stringify(r.trace,null,2)}\n\`\`\`\n`;
  fs.mkdirSync(path.join(rt.repo,'evidence','execution'),{recursive:true});
  fs.writeFileSync(path.join(rt.repo,'evidence','execution',`${feature}-api.md`),md);
  console.log(JSON.stringify({feature,count,originalUnchanged:unchanged}));
  if(!unchanged||results.some(r=>r.status==='BLOCKED'))process.exitCode=2;
})().catch(e=>{console.error(e);process.exitCode=2;});
