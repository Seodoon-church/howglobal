/* HOW INTERNATIONAL — shared behavior */
(function(){
  'use strict';
  var store = {
    get:function(k){ try{return localStorage.getItem(k)}catch(e){return null} },
    set:function(k,v){ try{localStorage.setItem(k,v)}catch(e){} }
  };

  /* ---------- language ---------- */
  function applyLang(lang){
    var dict = window.I18N || {};
    document.documentElement.setAttribute('lang', lang);
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k = el.getAttribute('data-i18n'); var e = dict[k];
      if(e && e[lang]!=null){
        if(el.hasAttribute('data-i18n-html')) el.innerHTML = e[lang];
        else el.textContent = e[lang];
      }
    });
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el){
      var k = el.getAttribute('data-i18n-ph'); var e = dict[k];
      if(e && e[lang]!=null) el.setAttribute('placeholder', e[lang]);
    });
    document.querySelectorAll('[data-i18n-content]').forEach(function(el){
      var k = el.getAttribute('data-i18n-content'); var e = dict[k];
      if(e && e[lang]!=null) el.setAttribute('content', e[lang]);
    });
    document.querySelectorAll('.lang button').forEach(function(b){
      b.classList.toggle('on', b.getAttribute('data-lang')===lang);
    });
    store.set('how_lang', lang);
    window.HOW_LANG = lang;
    document.dispatchEvent(new CustomEvent('langchange',{detail:{lang:lang}}));
  }
  window.HOW_setLang = applyLang;
  var initLang = store.get('how_lang') || 'ko';

  /* ---------- dom ready ---------- */
  document.addEventListener('DOMContentLoaded', function(){
    // year
    var y = document.getElementById('year'); if(y) y.textContent = new Date().getFullYear();

    // active nav
    var page = document.body.getAttribute('data-page');
    if(page) document.querySelectorAll('.menu a[data-nav]').forEach(function(a){
      if(a.getAttribute('data-nav')===page) a.classList.add('active');
    });

    // mobile menu
    var burger = document.querySelector('.burger'), menu = document.querySelector('.menu');
    if(burger && menu){
      burger.addEventListener('click', function(){
        menu.classList.toggle('open');
        burger.setAttribute('aria-expanded', menu.classList.contains('open'));
      });
      menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){menu.classList.remove('open')})});
    }

    // language buttons
    document.querySelectorAll('.lang button').forEach(function(b){
      b.addEventListener('click', function(){ applyLang(b.getAttribute('data-lang')); });
    });
    applyLang(initLang);

    // reveal
    var rvs = document.querySelectorAll('.rv');
    if('IntersectionObserver' in window){
      var io = new IntersectionObserver(function(es){
        es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
      },{threshold:.14, rootMargin:'0px 0px -8% 0px'});
      rvs.forEach(function(el){io.observe(el)});
    } else { rvs.forEach(function(el){el.classList.add('in')}); }
    window.addEventListener('load', function(){
      document.querySelectorAll('.hero .rv, .subhero .rv').forEach(function(el){el.classList.add('in')});
    });

    // page modules
    if(page==='news') renderList('news','data/news.json');
    if(page==='library') renderList('library','data/library.json');
    if(page==='quote') initQuoteForm();
  });

  /* ---------- news / library ---------- */
  function fmtDate(s,lang){
    try{ var d=new Date(s);
      return d.toLocaleDateString(lang==='en'?'en-US':'ko-KR',{year:'numeric',month:'2-digit',day:'2-digit'});
    }catch(e){return s}
  }
  function renderList(kind, url){
    var host = document.getElementById(kind+'-list'); if(!host) return;
    fetch(url).then(function(r){return r.ok?r.json():[]}).then(function(items){
      if(!items || !items.length){ showEmpty(host, kind); return; }
      draw(host, kind, items);
      document.addEventListener('langchange', function(){ draw(host, kind, items); });
    }).catch(function(){ showEmpty(host, kind); });
  }
  function showEmpty(host, kind){
    var lang = window.HOW_LANG || 'ko';
    var msgKo = kind==='news' ? '등록된 소식이 준비 중입니다. 곧 업데이트됩니다.' : '자료를 준비 중입니다. 곧 업로드됩니다.';
    var msgEn = kind==='news' ? 'News is being prepared. Check back soon.' : 'Resources are being prepared. Coming soon.';
    host.innerHTML = '<div class="empty"><span class="mono">'+(kind==='news'?'NO POSTS':'NO FILES')+'</span><p>'+(lang==='en'?msgEn:msgKo)+'</p></div>';
  }
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function draw(host, kind, items){
    var lang = window.HOW_LANG || 'ko';
    host.innerHTML = '<div class="list">' + items.map(function(it){
      var title = esc(it['title_'+lang] || it.title_ko || '');
      if(kind==='news'){
        var cat = esc(it['cat_'+lang] || it.cat_ko || '');
        var ex = esc(it['excerpt_'+lang] || it.excerpt_ko || '');
        return '<article class="litem"><div class="meta"><span class="cat">'+cat+'</span><br>'+fmtDate(it.date,lang)+'</div>'
             + '<div><h3>'+title+'</h3><p>'+ex+'</p></div>'
             + '<a class="act" href="'+(it.link||'#')+'"'+(it.link?' target="_blank" rel="noopener"':'')+'>'+(lang==='en'?'Read':'자세히')+' →</a></article>';
      } else {
        var type = esc(it.type||'PDF'), size = esc(it.size||'');
        var dl = lang==='en'?'Download':'다운로드';
        return '<article class="litem"><div class="meta"><span class="cat">'+type+'</span><br>'+size+'</div>'
             + '<div><h3>'+title+'</h3><p>'+esc(it['desc_'+lang]||it.desc_ko||'')+'</p></div>'
             + '<a class="act" href="'+(it.file||'#')+'"'+(it.file?' download':'')+'>'+dl+' ↓</a></article>';
      }
    }).join('') + '</div>';
  }

  /* ---------- quote form ---------- */
  function initQuoteForm(){
    var form = document.getElementById('quote-form');
    var success = document.getElementById('quote-success');
    var resetBtn = document.getElementById('quote-reset');
    var quoteFields = document.getElementById('quote-fields');
    if(!form) return;

    // preset type from ?type=media|distribution|healthcare|other
    try{
      var p = new URLSearchParams(location.search).get('type');
      if(p){ selectType(p); }
    }catch(e){}

    // type card selection
    form.querySelectorAll('.qtype-card').forEach(function(card){
      card.addEventListener('click', function(){
        var t = card.getAttribute('data-type');
        selectType(t);
      });
    });

    function selectType(t){
      form.querySelectorAll('.qtype-card').forEach(function(c){c.classList.remove('active')});
      var target = form.querySelector('.qtype-card[data-type="'+t+'"]');
      if(target){ target.classList.add('active'); var r = target.querySelector('input[type=radio]'); if(r) r.checked = true; }
      if(quoteFields){
        if(t==='media'){ quoteFields.classList.remove('hidden'); }
        else { quoteFields.classList.add('hidden'); }
      }
    }

    // reset button
    if(resetBtn){ resetBtn.addEventListener('click', function(){ if(success) success.style.display='none'; form.style.display=''; form.reset(); selectType('media'); }); }

    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var lang = window.HOW_LANG || 'ko';
      var checkedType = (form.querySelector('input[name="qtype"]:checked')||{}).value || 'media';
      var data = {
        type: checkedType,
        budget: (form.budget||{}).value || '',
        projtype: (form.projtype||{}).value || '',
        schedule: (form.schedule||{}).value.trim() || '',
        ref: (form.ref||{}).value.trim() || '',
        company: form.company.value.trim(),
        name: form.name.value.trim(),
        email: form.email.value.trim(),
        phone: form.phone.value.trim(),
        message: form.message.value.trim(),
        consent: form.consent.checked,
        createdAt: new Date().toISOString()
      };
      if(!data.name||!data.email||!data.message||!data.consent){
        toast(lang==='en'?'Please fill required fields and agree to the policy.':'필수 항목과 개인정보 동의를 확인해 주세요.',true); return;
      }
      if(window.HOW_submitInquiry){
        window.HOW_submitInquiry(data).then(function(){ done(data.email); }).catch(function(){ mailFallback(data); });
      } else { mailFallback(data); }

      function done(email){
        form.style.display='none';
        if(success){
          var ep = success.querySelector('p');
          if(ep) ep.textContent = '담당자가 확인 후 1~2영업일 내 '+(email||'고객님의 이메일')+'로 회신드립니다.';
          success.style.display='';
        }
      }
      function mailFallback(d){
        var typeLabel = {distribution:'유통 제휴',healthcare:'헬스케어 제휴',media:'미디어 개발·견적',other:'기타 문의'}[d.type]||d.type;
        var subj = encodeURIComponent('['+typeLabel+'] '+d.name+(d.company?' / '+d.company:''));
        var body = encodeURIComponent('유형: '+typeLabel+'\n이름: '+d.name+'\n회사: '+d.company+'\n이메일: '+d.email+'\n연락처: '+d.phone+(d.budget?'\n예산: '+d.budget:'')+(d.schedule?'\n일정: '+d.schedule:'')+'\n\n'+d.message);
        window.location.href='mailto:howintlsoft@gmail.com?subject='+subj+'&body='+body;
        toast(lang==='en'?'Opening your email app…':'메일 앱으로 문의 내용을 전달합니다…');
      }
    });
  }

  /* ---------- contact form (legacy) ---------- */
  function toast(msg, err){
    var t = document.getElementById('toast'); if(!t){alert(msg);return;}
    t.textContent = msg; t.classList.toggle('err', !!err); t.classList.add('show');
    setTimeout(function(){t.classList.remove('show')}, 3600);
  }
  function initContactForm(){
    var form = document.getElementById('inquiry-form'); if(!form) return;
    // preset inquiry type from ?type=distribution|software
    try{
      var p = new URLSearchParams(location.search).get('type');
      if(p==='software' || p==='distribution'){
        var r = form.querySelector('input[name="type"][value="'+p+'"]');
        if(r) r.checked = true;
      }
    }catch(e){}
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var lang = window.HOW_LANG || 'ko';
      var data = {
        type: (form.querySelector('input[name="type"]:checked')||{}).value || 'distribution',
        name: form.name.value.trim(), company: form.company.value.trim(),
        email: form.email.value.trim(), phone: form.phone.value.trim(),
        message: form.message.value.trim(), consent: form.consent.checked,
        createdAt: new Date().toISOString()
      };
      if(!data.name || !data.email || !data.message || !data.consent){
        toast(lang==='en'?'Please fill required fields and agree to the policy.':'필수 항목과 개인정보 동의를 확인해 주세요.', true); return;
      }
      // If Firestore is wired (admin phase), submit there; else mailto fallback.
      if(window.HOW_submitInquiry){
        window.HOW_submitInquiry(data).then(function(){ done(); }).catch(function(){ mailFallback(data); });
      } else { mailFallback(data); }

      function done(){ form.reset(); toast(lang==='en'?'Thanks! We\'ll get back to you shortly.':'문의가 접수되었습니다. 빠르게 회신드리겠습니다.'); }
      function mailFallback(d){
        var subj = encodeURIComponent('['+ (d.type==='software'?'개발 의뢰':'유통 제휴') +'] '+ d.name + (d.company?(' / '+d.company):''));
        var body = encodeURIComponent(
          '유형: '+(d.type==='software'?'개발 의뢰':'유통 제휴')+'\n이름: '+d.name+'\n회사: '+d.company+'\n이메일: '+d.email+'\n연락처: '+d.phone+'\n\n'+d.message);
        window.location.href = 'mailto:howintlsoft@gmail.com?subject='+subj+'&body='+body;
        toast(lang==='en'?'Opening your email app…':'메일 앱으로 문의 내용을 전달합니다…');
      }
    });
  }
})();
