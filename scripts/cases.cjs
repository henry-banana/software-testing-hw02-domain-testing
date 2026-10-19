// Test inputs/expected behavior come from SRS FR-04/09/12/17/20 (+ mapped FR-06/07).
// Fixtures arrange state; public HTTP/UI observations determine outcomes.
const cases=[];
function add(feature,id,title,technique,rule,kind,input,expected,extra={}){cases.push({feature,id,title,technique,rule,kind,input,expected,...extra});}
function a(n,title,phone,valid,technique='Domain',extra={}){add('A',`A-API-${String(n).padStart(2,'0')}`,title,technique,'FR-04 phone: starts 0, 10–11 digits; numeral encoding unspecified','profile',{name:'HW02 User',shipping_address:'1 Test Street',phone},valid?'Accept and persist the exact valid phone':'Reject; stored phone stays 0912345678',{valid,bug:'BUG-A01',...extra});}
a(1,'10 digits: lower ON boundary','0912345678',true,'Domain+BVA');
a(2,'11 digits: upper ON boundary','09123456789',true,'Domain+BVA');
a(3,'9 digits: lower OFF boundary','091234567',false,'Domain+BVA');
a(4,'12 digits: upper OFF boundary','091234567890',false,'Domain+BVA');
a(5,'Empty phone','',false);a(6,'One digit','0',false);a(7,'8 digits: invalid IN point','09123456',false);
a(8,'13 digits: invalid IN point','0912345678901',false);
a(9,'Wrong leading digit, length 10','1912345678',false);
a(10,'Wrong leading digit, length 11','19123456789',false);
a(11,'Alphabetic character','091234567a',false);a(12,'Embedded space','09123 5678',false);
a(13,'Country prefix instead of 0','+84912345678',false);a(14,'Hyphenated digits','09123-5678',false);
a(15,'Unicode fullwidth digits','０９１２３４５６７８',false,'Domain',{observation:true});
cases.at(-1).expected='Record Unicode numeral acceptance; SRS does not explicitly specify numeral encoding';
a(16,'Null phone',null,false);
add('A','A-API-17','Unicode name and address','Domain','FR-04 editable fields','profile',{name:'Người Dùng HW02',phone:'0912345678',shipping_address:'Đường Thử Nghiệm'},'Persist Unicode name and address exactly',{valid:true});
add('A','A-API-18','Client role escalation','Domain','FR-04 + SEC-06: cannot self-edit role','profile-role',{name:'HW02 User',phone:'0912345678',shipping_address:'1 Test Street',role:'admin'},'Reject or ignore role; GET /users/me remains role=user',{bug:'BUG-A02'});
add('A','A-API-19','Body user id cannot redirect update','Domain','FR-04 own profile only','profile-owner',{name:'Owner Only',phone:'0912345678',shipping_address:'1 Test Street',id:3,user_id:3},'Update authenticated user 2; user 3 unchanged');
for(const [id,auth] of [[20,'none'],[21,'invalid']]) add('A',`A-API-${id}`,'Profile update: '+auth+' token','Domain','FR-04 + SEC-02','profile-auth',{phone:'0912345678'},'Reject unauthenticated update (401/403); profile unchanged',{auth});
add('A','A-API-22','Profile read needs authentication','Domain','SEC-02','profile-read',{},'GET profile without JWT returns 401/403',{auth:'none'});

function b(n,title,input,expected,extra={}){add('B',`B-API-${String(n).padStart(2,'0')}`,title,extra.technique||'Domain','FR-09 C1–C5 + discount formula','coupon',input,expected,{auth:'user',...extra});}
b(1,'Fixed discount nominal',{code:'BIGBUY',total_amount:600000,user_id:2},'discount=50000; final=550000',{money:[50000,550000]});
b(2,'Below fixed minimum',{code:'BIGBUY',total_amount:499999,user_id:2},'Reject insufficient total',{reject:true,technique:'Domain+BVA'});
b(3,'Exactly fixed minimum',{code:'BIGBUY',total_amount:500000,user_id:2},'discount=50000; final=450000',{money:[50000,450000],bug:'BUG-B01',technique:'Domain+BVA'});
b(4,'Above fixed minimum',{code:'BIGBUY',total_amount:500001,user_id:2},'discount=50000; final=450001',{money:[50000,450001],technique:'Domain+BVA'});
b(5,'Below percent minimum',{code:'SAVE10',total_amount:299999,user_id:2},'Reject insufficient total',{reject:true,technique:'Domain+BVA'});
b(6,'Exactly percent minimum',{code:'SAVE10',total_amount:300000,user_id:2},'discount=30000; final=270000',{money:[30000,270000],bug:'BUG-B01',technique:'Domain+BVA'});
b(7,'Above percent minimum',{code:'SAVE10',total_amount:300001,user_id:2},'discount=30000.1; final=270000.9 (SRS has no rounding rule)',{money:[30000.1,270000.9],bug:'BUG-B02',technique:'Domain+BVA'});
b(8,'Percent formula with integer result',{code:'SAVE10',total_amount:400000,user_id:2},'discount=40000; final=360000',{money:[40000,360000],bug:'BUG-B02'});
b(9,'Nonexistent code',{code:'NO_SUCH_CODE',total_amount:600000,user_id:2},'Reject nonexistent code',{reject:true});
b(10,'Inactive code',{code:'OFF',total_amount:600000,user_id:2},'Reject inactive code',{reject:true});
b(11,'Missing code',{total_amount:600000,user_id:2},'Reject missing code',{reject:true});
b(12,'Expired before current time by 1 ms',{code:'TIME',total_amount:400000,user_id:2},'Reject expired coupon',{reject:true,expiry:-1,technique:'Domain+BVA'});
b(13,'Expiry exactly equals current time',{code:'TIME',total_amount:400000,user_id:2},'Reject: current time must be strictly before expiry',{reject:true,expiry:0,bug:'BUG-B03',technique:'Domain+BVA'});
b(14,'Expiry after current time by 1 ms',{code:'TIME',total_amount:400000,user_id:2},'discount=10000; final=390000',{money:[10000,390000],expiry:1,technique:'Domain+BVA'});
for(const [n,used] of [[15,0],[16,1],[17,2],[18,3]]) b(n,`VIP100 used=${used}, limit=2`,{code:'VIP100',total_amount:400000,user_id:2},used<2?'discount=100000; final=300000':'Reject exhausted coupon',{used,...(used<2?{money:[100000,300000]}:{reject:true}),technique:'Domain+BVA'});
for(const [n,auth]of[[19,'none'],[20,'invalid'],[21,'expired']])b(n,'Coupon with '+auth+' JWT',{code:'BIGBUY',total_amount:600000,user_id:2},'Reject invalid/missing authentication (401/403)',{auth,rejectAuth:true,bug:'BUG-B04'});
b(22,'Exhausted authenticated user spoofs user_id=3',{code:'VIP100',total_amount:400000,user_id:3},'Reject: user 2 already used limit; client user_id is not identity',{used:2,reject:true,bug:'BUG-B05'});
b(23,'Exhausted authenticated user omits user_id',{code:'VIP100',total_amount:400000},'Reject: authenticated user 2 already used limit',{used:2,reject:true,bug:'BUG-B05'});
b(24,'Intersection: minimum equality and last eligible use',{code:'VIP100',total_amount:300000,user_id:2},'discount=100000; final=200000',{used:1,money:[100000,200000],bug:'BUG-B01',technique:'Domain+BVA'});
b(25,'Multiple invalid conditions',{code:'OFF',total_amount:0},'Reject; no error precedence is specified',{auth:'none',reject:true});
b(26,'Percent 100 formula',{code:'P100',total_amount:400000,user_id:2},'discount=400000; final=0',{money:[400000,0],bug:'BUG-B02'});

const base={code:'HW02_NEW',type:'fixed',discount_value:1,min_order_amount:0,expired_at:'2099-12-31',max_uses_per_user:1};
function c(n,title,patch,valid,extra={}){const input={...base,...patch};if(extra.omit)delete input[extra.omit];add('C',`C-API-${String(n).padStart(2,'0')}`,title,extra.technique||'Domain','FR-17 required fields/constraints; FR-12 admin role','admin-create',input,valid?'Admin creates coupon and list contains exact supplied values':'Reject invalid coupon; list has no newly created record',{valid,auth:'admin',bug:'BUG-C01',...extra});}
c(1,'Nominal fixed coupon',{},true);c(2,'Nominal percent coupon',{type:'percent',discount_value:10},true);
let cn=3;
for(const field of Object.keys(base))c(cn++,`Missing mandatory ${field}`,{},false,{omit:field,bug:'BUG-C01'});
c(9,'Empty code',{code:''},false,{bug:'BUG-C01'});
c(10,'Duplicate code',{code:'SAVE10'},false,{bug:'BUG-C02'});
c(11,'Unknown type',{type:'other'},false,{bug:'BUG-C03'});
c(12,'discount_value=-1',{discount_value:-1},false,{bug:'BUG-C04',technique:'Domain+BVA'});
c(13,'discount_value=0',{discount_value:0},false,{bug:'BUG-C04',technique:'Domain+BVA'});
c(14,'discount_value=1',{discount_value:1},true,{technique:'Domain+BVA'});
c(15,'min_order_amount=-1',{min_order_amount:-1},false,{bug:'BUG-C05',technique:'Domain+BVA'});
c(16,'min_order_amount=0',{min_order_amount:0},true,{technique:'Domain+BVA'});
c(17,'min_order_amount=1',{min_order_amount:1},true,{technique:'Domain+BVA'});
c(18,'max_uses_per_user=-1',{max_uses_per_user:-1},false,{bug:'BUG-C06',technique:'Domain+BVA'});
c(19,'max_uses_per_user=0',{max_uses_per_user:0},false,{bug:'BUG-C06',technique:'Domain+BVA'});
c(20,'max_uses_per_user=1',{max_uses_per_user:1},true,{technique:'Domain+BVA'});
c(21,'max_uses_per_user=2',{max_uses_per_user:2},true,{technique:'Domain+BVA'});
c(22,'No JWT creates coupon',{},false,{auth:'none',authCase:true,bug:'BUG-C07'});
c(23,'User role creates coupon',{},false,{auth:'user',authCase:true,bug:'BUG-C07'});
cases.at(-1).expected='Reject non-admin create (401/403); valid coupon data must not be inserted';
c(24,'Invalid JWT creates coupon',{},false,{auth:'invalid',authCase:true,bug:'BUG-C07'});
for(const [n,auth]of[[25,'admin'],[26,'user'],[27,'none']])add('C',`C-API-${n}`,'List coupons as '+auth,'Domain','FR-12/FR-17','admin-list',{},auth==='admin'?'Return coupon list':'Reject non-admin access (401/403)',{auth,valid:auth==='admin',bug:'BUG-C08'});
for(const [n,auth]of[[28,'admin'],[29,'user'],[30,'none']])add('C',`C-API-${n}`,'Delete coupon as '+auth,'Domain','FR-12/FR-17','admin-delete',{code:'DELETE_ME'},auth==='admin'?'Coupon removed; other coupons unchanged':'Reject non-admin delete; coupon remains',{auth,valid:auth==='admin',bug:'BUG-C09'});
add('D','D-API-01','Product 1 support API','Domain','FR-20 + FR-06 mapped detail data','product',{id:1},'Product 1 name/price/description/image/category ID match fixture',{valid:true});
add('D','D-API-02','Product 2 support API','Domain','FR-20 + FR-06 mapped detail data','product',{id:2},'Product 2 data usable; price numerically 28000000 (JSON type not specified)',{valid:true});
add('D','D-API-03','Missing product support API observation','Domain','FR-20: missing-product HTTP schema unspecified','product',{id:999999},'Record HTTP/body; no mandated status code in SRS',{observation:true});

function ui(feature,id,title,input,expected,extra={}){add(feature,id,title,extra.technique||'Domain','UI '+(feature==='A'?'FR-04':feature==='B'?'FR-09':feature==='C'?'FR-17/FR-12':'FR-20 with mapped FR-06/07'), 'manual',input,expected,{status:'NOT RUN',...extra});}
for(const[n,phone,valid]of[[1,'091234567',false],[2,'0912345678',true],[3,'09123456789',true],[4,'091234567890',false],[5,'1912345678',false]])ui('A',`A-UI-0${n}`,'Profile phone '+phone,{phone},valid?'Update succeeds; re-login shows the exact phone':'Reject; saved profile remains unchanged',{technique:'Domain+BVA'});
ui('A','A-UI-06','Email field cannot be changed',{email:'other@example.invalid'},'Email is not editable via UI; original email unchanged');
ui('A','A-UI-07','Unicode editable profile fields',{name:'Người Dùng HW02',shipping_address:'Đường Thử Nghiệm',phone:'0912345678'},'Valid update accepted; name/address persist after fresh login');
for(const[n,code,total,expected]of[[1,'BIGBUY',499999,'Reject below minimum'],[2,'BIGBUY',500000,'Discount 50000; final 450000'],[3,'BIGBUY',500001,'Discount 50000; final 450001'],[4,'SAVE10',400000,'Discount 40000; final 360000'],[5,'EXPIRED',400000,'Reject expired coupon'],[6,'VIP100',400000,'After exactly 2 completed uses, third attempt rejected']])ui('B',`B-UI-0${n}`,'Checkout '+code+' / '+total,{code,total},expected,{technique:n<=3?'Domain+BVA':'Domain'});
for(const[n,patch,expected]of[[1,{discount_value:0},'Reject discount_value=0'],[2,{},'Create coupon; same values visible after reload'],[3,{min_order_amount:-1},'Reject negative minimum'],[4,{max_uses_per_user:0},'Reject zero usage limit'],[5,{code:'SAVE10'},'Reject duplicate; original SAVE10 unchanged']])ui('C',`C-UI-0${n}`,'Admin coupon form '+n,{...base,code:`HW02_C_UI_0${n}`,...patch},expected,{technique:n<=4?'Domain+BVA':'Domain'});
ui('C','C-UI-06','Admin delete lifecycle',{code:'HW02_DELETE_UI'},'Create test coupon, delete it; disappears after reload; SAVE10 unchanged');
for(const[n,q,expected]of[[1,'','Reject empty quantity; no new cart item'],[2,'-1','Reject negative; cart unchanged'],[3,'0','Reject zero; cart unchanged'],[4,'1','Cart contains quantity=1, total=30000000'],[5,'2','Cart contains quantity=2, total=60000000'],[6,'1.5','Reject fractional; cart unchanged'],[7,'abc','Reject nonnumeric; cart unchanged'],[8,'1abc','Reject mixed text; cart unchanged']])ui('D',`D-UI-0${n}`,'Mobile quantity '+JSON.stringify(q),{product:1,quantity:q},expected,{technique:n>=2&&n<=5?'Domain+BVA':'Domain',mapping:'FR-20 functionality + FR-06 positive integer; student confirms mapping'});
ui('D','D-UI-09','Mobile complete product detail',{product:1},'Image/name/price/description/category visible and correct; mapped FR-06',{mapping:'FR-20 + FR-06'});
ui('D','D-UI-10','Mobile even-id price display',{product:2},'Samsung price displayed as 28,000,000 ₫ using locale separator; no crash');
ui('D','D-UI-11','Mobile add feedback',{product:1,quantity:'1'},'Visible feedback after Add; cart quantity 1');
ui('D','D-UI-12','Same product twice',{product:1,quantity:'1',repetitions:2},'One cart line quantity=2; total=60000000',{mapping:'FR-07 reused through FR-20'});
ui('D','D-UI-13','Detail quantity resets after switching products',{products:[1,2],quantity:'2'},'Record selected quantity for product 2; SRS does not specify default reset policy',{observation:true});
ui('D','D-UI-14','Very large quantity exploratory input',{product:1,quantity:'9007199254740992'},'Record behavior/precision; upper limit unspecified, do not declare violation solely from size',{observation:true});
// Design metadata is independent of execution. UI verdicts are recorded in Markdown.
for (const tc of cases.filter(tc => tc.kind === 'manual')) {
  delete tc.status;
  if (tc.id === 'A-UI-05' || tc.id === 'C-UI-02' || tc.id === 'D-UI-02') tc.technique = 'Domain';
}
for (const tc of cases.filter(tc => tc.feature === 'C' && tc.kind === 'admin-create' && tc.authCase)) {
  tc.expected = tc.auth === 'user'
    ? 'Reject non-admin create (401/403); valid coupon data must not be inserted'
    : 'Reject missing/invalid JWT (401/403); valid coupon data must not be inserted';
}
module.exports={cases,base};
