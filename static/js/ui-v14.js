/* V14 shell interactions: persisted collapse, accessible mobile drawer. */
(function(){
'use strict';
var side=document.getElementById('sidebar'),main=document.getElementById('mainContent'),toggle=document.getElementById('toggleSidebar'),mobile=document.getElementById('mobileNavToggle'),backdrop=document.getElementById('sidebarBackdrop');
if(!side||!main)return;
var key='cg-sidebar-collapsed',small=function(){return window.matchMedia('(max-width:620px)').matches;};
function setCollapsed(value,save){side.classList.toggle('collapsed',value);main.classList.toggle('collapsed',value);if(toggle){toggle.setAttribute('aria-expanded',String(!value));toggle.setAttribute('aria-label',value?'Expandir menú lateral':'Contraer menú lateral');toggle.title=value?'Expandir menú':'Contraer menú';var i=toggle.querySelector('i');if(i){i.classList.toggle('fa-chevron-left',!value);i.classList.toggle('fa-chevron-right',value);}}if(save){try{localStorage.setItem(key,value?'1':'0');}catch(e){}}}
function closeMobile(){side.classList.remove('mobile-open');if(backdrop)backdrop.classList.remove('is-visible');if(mobile)mobile.setAttribute('aria-expanded','false');}
function openMobile(){side.classList.add('mobile-open');if(backdrop)backdrop.classList.add('is-visible');if(mobile)mobile.setAttribute('aria-expanded','true');}
var saved=null;try{saved=localStorage.getItem(key);}catch(e){}setCollapsed(saved==='1',false);
if(toggle)toggle.addEventListener('click',function(){if(small()){side.classList.contains('mobile-open')?closeMobile():openMobile();return;}setCollapsed(!side.classList.contains('collapsed'),true);});
if(mobile)mobile.addEventListener('click',function(){side.classList.contains('mobile-open')?closeMobile():openMobile();});
if(backdrop)backdrop.addEventListener('click',closeMobile);
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeMobile();});
window.addEventListener('resize',function(){if(!small())closeMobile();});
document.querySelectorAll('.nav-item[data-url]').forEach(function(item){var url=item.getAttribute('data-url'),label=item.querySelector('.nav-label');if(label&&!item.hasAttribute('title'))item.setAttribute('title',label.textContent.trim());if(item.disabled||item.classList.contains('cg-btn-disabled'))return;item.addEventListener('click',function(){if(url&&url!=='#')window.location.assign(url);closeMobile();});});
})();
