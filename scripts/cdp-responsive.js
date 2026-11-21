const wsUrl=process.argv[2]; const ws=new WebSocket(wsUrl); let id=1; const p=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data); if(m.id&&p.has(m.id)){const {r,j}=p.get(m.id);p.delete(m.id);m.error?j(new Error(m.error.message)):r(m.result);}});
const open=new Promise((r,j)=>{ws.addEventListener('open',r);ws.addEventListener('error',j)});
const send=(method,params={})=>new Promise((r,j)=>{const i=id++;p.set(i,{r,j});ws.send(JSON.stringify({id:i,method,params}))});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{await open; await send('Page.enable'); await send('Runtime.enable');
const ev=async x=>{const r=await send('Runtime.evaluate',{expression:x,awaitPromise:true,returnByValue:true}); return r.result.value};
const origin=await ev('location.origin');
const paths=['/','/roadmaps/','/roadmaps/etapa/0/','/roadmaps/leccion/1/','/roadmaps/evaluaciones/','/roadmaps/evidencias/','/roadmaps/conocimiento/','/biblioteca/','/biblioteca/1/','/backups/','/gamificacion/perfil/'];
let bad=[];
for(const [w,h] of [[1024,720],[768,900]]){
  await send('Emulation.setDeviceMetricsOverride',{width:w,height:h,deviceScaleFactor:1,mobile:false});
  for(const path of paths){
    await send('Page.navigate',{url:origin+path}); await sleep(350);
    const m=await ev("JSON.stringify({s:document.documentElement.scrollWidth,c:document.documentElement.clientWidth,t:document.title})");
    const x=JSON.parse(m); if(x.s>x.c+2) bad.push({path,w,scroll:x.s,client:x.c});
    console.log(w,path,x.s,x.c,x.t);
  }
}
await send('Emulation.clearDeviceMetricsOverride');
console.log('BAD='+JSON.stringify(bad));
ws.close();
})().catch(e=>{console.error(e);process.exit(1)});
