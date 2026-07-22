# -*- coding: utf-8 -*-
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
DOMAIN = "https://howglobal.co.kr"

# ---------------------------------------------------------------- i18n
# key: (ko, en)
T = {
 "nav.business":("사업분야","Business"),
 "nav.about":("회사소개","About"),
 "nav.news":("뉴스","News"),
 "nav.library":("자료실","Resources"),
 "nav.contact":("협력 문의","Contact"),
 "cta.header":("협력 문의","Contact"),
 "brand.tag":("Global Distribution · Software","Global Distribution · Software"),
 # footer
 "foot.tagline":("검증된 유통, 우리가 만든 플랫폼.","Trusted distribution. Platforms we build."),
 "foot.sitemap":("Sitemap","Sitemap"),
 "foot.company":("Company","Company"),
 "foot.bizno":("사업자등록번호 214-88-51839","Business Reg. No. 214-88-51839"),
 "foot.addr":("경기도 화성시 동탄광역환승로73<br>반도유보라아이비파크8.0 206-604",
              "206-604, Banseo Yubora IV Park 8.0,<br>73 Dongtan Gwangyeok Hwanseung-ro, Hwaseong, Korea"),
 "foot.admin":("· 관리자","· Admin"),
 # home hero
 "home.eyebrow":("HOW INTERNATIONAL · 유통 × 소프트웨어","HOW INTERNATIONAL · DISTRIBUTION × SOFTWARE"),
 "home.h1":("검증된 제품을 유통하고,<br><span class=\"u\">필요한 플랫폼</span>을 직접 만듭니다.",
            "We distribute proven products<br>and <span class=\"u\">build the platforms</span> we need."),
 "home.lead":("하우인터내셔널은 미국·국산 우수 제품을 국내 시장에 유통하고, 현장의 문제를 푸는 웹·앱 플랫폼을 자체 개발합니다. 두 개의 사업부, 하나의 실행력.",
              "HOW International distributes premium products from the US and Korea, and builds its own web and app platforms that solve real problems. Two divisions, one team."),
 "home.cta1":("협력 문의하기 →","Get in touch →"),
 "home.cta2":("사업분야 살펴보기","Explore business"),
 "home.div1.t":("유통","Distribution"),
 "home.div1.p":("해외·국내에서 검증된 제품을 발굴해 국내 시장에 안정적으로 공급합니다.",
                "We source proven products at home and abroad and supply them reliably to Korea."),
 "home.div2.t":("소프트웨어 개발","Software"),
 "home.div2.p":("분양·교육·기록 등 실제 수요가 있는 영역의 플랫폼을 기획부터 운영까지 직접 만듭니다.",
                "We build platforms end-to-end in areas with real demand — sales, education, and records."),
 # strip
 "strip.k1":("Divisions","Divisions"), "strip.v1":("02 사업부문 — 유통 · 소프트웨어","02 divisions — Distribution · Software"),
 "strip.k2":("Distribution","Distribution"), "strip.v2":("02 유통 브랜드","02 distribution brands"),
 "strip.k3":("Platforms","Platforms"), "strip.v3":("03 자체 개발 플랫폼","03 in-house platforms"),
 "strip.k4":("Base","Base"), "strip.v4":("화성 · 대한민국","Hwaseong · Korea"),
 # home business
 "home.biz.eye":("사업분야 · Business","BUSINESS"),
 "home.biz.h2":("두 개의 사업부,<br>하나의 회사.","Two divisions,<br>one company."),
 "home.biz.note":("유통과 개발은 별개의 일처럼 보이지만, 좋은 제품을 알아보고 끝까지 책임진다는 원칙은 같습니다.",
                  "Distribution and development look different, but the principle is the same — recognize what's good and see it through."),
 "d1.ddesc":("해외·국내 우수 제품의 국내 총판 및 B2B 공급","Exclusive distribution and B2B supply of premium products"),
 "d2.ddesc":("기획·개발·운영을 직접 수행하는 자체 플랫폼","In-house platforms we plan, build, and operate"),
 "bio.tag":("미국 직수입","Imported from USA"),
 "bio.desc":("10종 유익 토양미생물로 작물 병해를 예방하고 생육을 돕는 토양생균제.",
             "A soil probiotic with 10 beneficial microbes that prevents crop disease and supports growth."),
 "pf.tag":("KFDA Class III","KFDA Class III"),
 "pf.desc":("6개의 치료 모듈을 하나로 통합한 6-in-1 통증치료 의료기기.",
            "A 6-in-1 pain-therapy device integrating six approved treatment modules."),
 "ms.tag":("PropTech","PropTech"),
 "ms.desc":("분양 현장을 위한 온라인 분양·관리 플랫폼.","An online sales-and-management platform for property offerings."),
 "kf.tag":("EdTech","EdTech"),
 "kf.desc":("외국인 학습자를 위한 한국어 학습 플랫폼.","A Korean-language learning platform for foreign learners."),
 "fa.tag":("Family","Family"),
 "fa.desc":("가족의 이야기를 한 권의 책으로 엮는 디지털 족보 플랫폼.","A digital family-tree platform that binds family stories into a book."),
 "link.view":("플랫폼 보기","View platform"),
 # partnership
 "part.eye":("협력 · Partnership","PARTNERSHIP"),
 "part.h2":("함께 할 방법은<br>두 가지입니다.","Two ways to<br>work with us."),
 "part.note":("제품 유통이든 플랫폼 개발이든, 먼저 이야기를 들려주세요. 영업일 기준 빠르게 회신드립니다.",
              "Distribution or development — tell us first. We reply quickly on business days."),
 "part.ch1":("유통 제휴","Distribution"),
 "part.ch1.p":("바이오타맥스·Painfree 8800의 총판, 대리점, 병·의원 및 B2B 공급을 논의합니다. 신규 수입·유통 품목 제안도 환영합니다.",
               "Discuss distributorship, dealerships, clinic and B2B supply for BiotaMax and Painfree 8800. New product proposals are welcome."),
 "part.ch1.go":("제휴 문의하기 →","Inquire →"),
 "part.ch2":("개발 의뢰","Software"),
 "part.ch2.p":("웹·앱 플랫폼 개발, 솔루션 도입, 기존 서비스 고도화를 문의합니다. 아이디어 단계의 상담도 가능합니다.",
               "Ask about web/app development, solution adoption, or improving existing services. Early-idea consults welcome."),
 "part.ch2.go":("개발 문의하기 →","Inquire →"),
 "part.cta":("협력 문의 폼 열기 →","Open the contact form →"),
 # about
 "about.crumb":("HOME / 회사소개","HOME / ABOUT"),
 "about.h1":("좋은 것을 알아보고,<br>끝까지 책임집니다.","We recognize what's good<br>and see it through."),
 "about.lead":("하우인터내셔널은 검증된 제품을 유통하고, 필요한 소프트웨어를 직접 개발하는 회사입니다. 규모보다 신뢰를, 유행보다 지속을 우선합니다.",
               "HOW International distributes proven products and builds the software it needs. We value trust over size, durability over trends."),
 "about.eye":("우리는 · Who we are","WHO WE ARE"),
 "about.big":("두 개의 사업부는 다른 언어를 쓰지만, 같은 기준으로 움직입니다.",
              "Our two divisions speak different languages but move by the same standard."),
 "about.p1":("유통 부문은 미국에서 직수입한 토양생균제 바이오타맥스와 국산 통증치료 의료기기 Painfree 8800을 국내에 공급합니다. 좋은 제품을 발굴하고, 인증과 품질을 지키며, 고객이 신뢰할 수 있는 유통 경로를 만듭니다.",
             "Our distribution division supplies BiotaMax — a soil probiotic imported directly from the US — and Painfree 8800, a Korean-made pain-therapy medical device. We source good products, uphold certification and quality, and build channels customers can trust."),
 "about.p2":("소프트웨어 부문은 분양(marketshare), 한국어 학습(KoreanFlow), 디지털 족보(우리家 이야기)까지 실제 수요가 있는 영역의 플랫폼을 직접 기획하고 개발·운영합니다.",
             "Our software division plans, builds, and operates platforms in areas with real demand — property sales (marketshare), Korean learning (KoreanFlow), and digital family history (Familya)."),
 "about.eye2":("일하는 방식 · How we work","HOW WE WORK"),
 "val1.t":("검증 우선","Proven first"),
 "val1.p":("유행이 아니라 근거로 판단합니다. 인증·품질·데이터로 확인된 것만 다룹니다.",
           "We judge by evidence, not hype — only what is verified by certification, quality, and data."),
 "val2.t":("끝까지 책임","Full ownership"),
 "val2.p":("소개로 끝내지 않습니다. 유통은 공급 이후를, 개발은 출시 이후를 함께합니다.",
           "We don't stop at the handoff. In distribution we stay past delivery; in software, past launch."),
 "val3.t":("직접 만든다","Built in-house"),
 "val3.p":("외주에 의존하지 않고 핵심 역량을 안에 둡니다. 그래서 더 빠르고 유연합니다.",
           "We keep core capability in-house rather than outsourcing — which makes us faster and more flexible."),
 "about.eye3":("회사 정보 · Company","COMPANY INFO"),
 "info.name":("사명","Company"), "info.biz":("대표 사업","Business"),
 "info.regno":("사업자등록번호","Business Reg. No."), "info.addr":("주소","Address"),
 "info.email":("이메일","Email"), "info.web":("웹사이트","Website"),
 "info.biz.v":("유통 · 소프트웨어 개발","Distribution · Software development"),
 "info.addr.v":("경기도 화성시 동탄광역환승로73 반도유보라아이비파크8.0 206-604",
                "206-604, Banseo Yubora IV Park 8.0, 73 Dongtan Gwangyeok Hwanseung-ro, Hwaseong, Gyeonggi, Korea"),
 # business page
 "biz.crumb":("HOME / 사업분야","HOME / BUSINESS"),
 "biz.h1":("두 개의 사업부.","Two divisions."),
 "biz.lead":("유통과 소프트웨어 개발. 하우인터내셔널이 실제로 하는 일을 한 곳에 정리했습니다.",
             "Distribution and software development — everything HOW International actually does, in one place."),
 "biz.d1.eye":("DIV.01 · 유통 / Distribution","DIV.01 · Distribution"),
 "biz.d2.eye":("DIV.02 · 소프트웨어 / Software","DIV.02 · Software"),
 "bio.p":("미국에서 직수입하는 토양생균제입니다. 10가지 유익한 토양 미생물이 작물의 병해를 예방하고 생육을 돕습니다.",
          "A soil probiotic imported directly from the US. Ten beneficial soil microbes prevent crop disease and support growth."),
 "bio.li1":("10종 유익 토양미생물 배합","Blend of 10 beneficial soil microbes"),
 "bio.li2":("작물 병해 예방 및 생육 촉진","Prevents disease, promotes growth"),
 "bio.li3":("친환경 농업 · 토양 개선","Eco-friendly farming and soil health"),
 "pf.p":("KFDA 허가를 받은 6-in-1 통합 통증치료 의료기기입니다. PSC·레이저·양자·초음파·PEMF·온열 6개 모듈을 하나의 콘솔에 담았습니다.",
         "A KFDA-approved 6-in-1 pain-therapy device. Six modules — PSC, laser, quantum, ultrasound, PEMF, and thermal — in a single console."),
 "pf.li1":("각각 KFDA 허가된 6개 치료 모듈","Six individually KFDA-approved modules"),
 "pf.li2":("비침습 통증 치료","Non-invasive pain treatment"),
 "pf.li3":("병·의원 · 재활 · 요양 도입","Adopted by clinics, rehab and care hospitals"),
 "ms.p":("분양 현장을 온라인으로 옮긴 분양·관리 솔루션입니다.","A sales-and-management solution that moves property offerings online."),
 "ms.li1":("온라인 분양 관리","Online sales management"),
 "ms.li2":("실시간 현황 파악","Real-time status"),
 "ms.li3":("현장별 맞춤 구성","Configurable per site"),
 "kf.p":("외국인 학습자를 위한 한국어 학습 플랫폼입니다.","A Korean-language learning platform for foreign learners."),
 "kf.li1":("단계별 학습 코스","Step-by-step courses"),
 "kf.li2":("발음 · 문법 훈련","Pronunciation and grammar"),
 "kf.li3":("웹 · 모바일 지원","Web and mobile"),
 "fa.p":("가족의 일상을 한 권의 책으로 엮는 디지털 족보 플랫폼입니다.","A digital family-tree platform that binds everyday family life into a book."),
 "fa.li1":("가계도 · 연대기","Family tree and chronicle"),
 "fa.li2":("사진첩 · 가족 톡방","Photo albums and family chat"),
 "fa.li3":("연감 PDF 자동 생성","Automatic yearbook PDF"),
 "link.site":("공식 사이트 →","Official site →"),
 # news / library
 "news.crumb":("HOME / 뉴스","HOME / NEWS"),
 "news.h1":("뉴스","News"),
 "news.lead":("하우인터내셔널의 새로운 소식과 보도자료입니다.","Updates and press from HOW International."),
 "lib.crumb":("HOME / 자료실","HOME / RESOURCES"),
 "lib.h1":("자료실","Resources"),
 "lib.lead":("회사소개서, 제품 카탈로그, 브로슈어 등 자료를 내려받을 수 있습니다.",
            "Download company profiles, product catalogs, and brochures."),
 # contact
 "ct.crumb":("HOME / 협력 문의","HOME / CONTACT"),
 "ct.h1":("협력 문의","Contact"),
 "ct.lead":("유통 제휴 또는 개발 의뢰, 어느 쪽이든 편하게 남겨주세요. 영업일 기준 빠르게 회신드립니다.",
            "Distribution or development — leave a note either way. We reply quickly on business days."),
 "ct.type":("문의 유형","Inquiry type"),
 "ct.type.d":("유통 제휴","Distribution"),
 "ct.type.s":("개발 의뢰","Software"),
 "ct.name":("이름","Name"), "ct.company":("회사 / 기관","Company"),
 "ct.email":("이메일","Email"), "ct.phone":("연락처","Phone"), "ct.msg":("문의 내용","Message"),
 "ph.name":("성함을 입력하세요","Your name"),
 "ph.company":("(선택) 회사 또는 기관명","Optional"),
 "ph.email":("you@example.com","you@example.com"),
 "ph.phone":("010-0000-0000","010-0000-0000"),
 "ph.msg":("문의하실 내용을 적어주세요.","Tell us how we can help."),
 "ct.consent":("개인정보 수집·이용에 동의합니다. (문의 응대 목적, 응대 후 파기)",
               "I agree to the collection and use of my personal data for this inquiry."),
 "ct.submit":("문의 보내기 →","Send inquiry →"),
 "ct.formnote":("접수 후 howintlsoft@gmail.com 으로 회신드립니다.","We'll reply from howintlsoft@gmail.com."),
 "ct.aside":("직접 연락","Direct contact"),
 "opt":("(선택)","optional"),
}

def w(el, key, tag_html=False, ph=False):
    ko = T[key][0]
    attr = 'data-i18n="%s"' % key
    if tag_html: attr += ' data-i18n-html'
    return attr, ko

# ---------------------------------------------------------------- chrome
def head(title, desc, path, page, extra_ld=""):
    url = DOMAIN + path
    org_ld = {
      "@context":"https://schema.org","@type":"Organization",
      "name":"하우인터내셔널","alternateName":"HOW INTERNATIONAL","url":DOMAIN,
      "logo":DOMAIN+"/assets/how-logo.png","email":"howintlsoft@gmail.com",
      "address":{"@type":"PostalAddress","streetAddress":"동탄광역환승로73 반도유보라아이비파크8.0 206-604",
                 "addressLocality":"화성시","addressRegion":"경기도","addressCountry":"KR"},
      "taxID":"214-88-51839",
      "description":"미국·국산 우수 제품을 유통하고 웹·앱 플랫폼을 자체 개발하는 회사."
    }
    ld = '<script type="application/ld+json">%s</script>' % json.dumps(org_ld, ensure_ascii=False)
    if extra_ld: ld += '\n<script type="application/ld+json">%s</script>' % extra_ld
    return """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="하우인터내셔널">
<meta property="og:type" content="website">
<meta property="og:site_name" content="하우인터내셔널">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{domain}/assets/og-cover.png">
<meta property="og:locale" content="ko_KR">
<meta property="og:locale:alternate" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="theme-color" content="#0000FF">
<link rel="icon" href="{domain}/assets/favicon.png">
<link rel="manifest" href="{domain}/site.webmanifest">
<!-- naver-site-verification / google-site-verification: 발급 후 삽입 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
{ld}
</head>
<body data-page="{page}">
""".format(title=title, desc=desc, url=url, domain=DOMAIN, ld=ld, page=page)

def header():
    def n(key, page):
        a,ko = w(None,key); return '<a %s data-nav="%s" href="%s">%s</a>' % (a, page, PAGES[page], ko)
    tag_a,tag_ko = w(None,"brand.tag"); c_a,c_ko = w(None,"cta.header")
    return """<header class="site">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="하우인터내셔널 홈">
      <img src="assets/how-logo.png" alt="HOW International" width="120" height="26">
      <span class="div" {tag_a}>{tag_ko}</span>
    </a>
    <button class="burger" aria-label="메뉴 열기" aria-expanded="false"><span></span></button>
    <nav class="menu" aria-label="주요 메뉴">
      {b}{a}{n}{l}
    </nav>
    <div class="navr">
      <div class="lang" role="group" aria-label="언어 / Language">
        <button data-lang="ko" class="on">KO</button><span>·</span><button data-lang="en">EN</button>
      </div>
      <a class="btn blue" {c_a} href="contact.html">{c_ko}</a>
    </div>
  </div>
</header>
""".format(tag_a=tag_a, tag_ko=tag_ko, c_a=c_a, c_ko=c_ko,
           b=n("nav.business","business"), a=n("nav.about","about"),
           n=n("nav.news","news"), l=n("nav.library","library"))

def footer():
    def L(key): a,ko=w(None,key); return a,ko
    fa,fko = L("foot.tagline"); sa,sko=L("foot.sitemap"); ca,cko=L("foot.company")
    ba,bko=L("foot.bizno"); aa,ako=L("foot.addr"); ada,adko=L("foot.admin")
    def nav(key,page): a,ko=w(None,key); return '<a %s href="%s">%s</a>'%(a,PAGES[page],ko)
    return """<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div class="fbrand">
        <img src="assets/how-logo.png" alt="HOW International">
        <div class="ft">하우인터내셔널 (HOW INTERNATIONAL)<br><span {fa}>{fko}</span></div>
      </div>
      <div class="fcol">
        <h5 {sa}>{sko}</h5>
        {nb}{na}{nn}{nl}{nc}
      </div>
      <div class="fcol">
        <h5 {ca}>{cko}</h5>
        <p {ba}>{bko}</p>
        <p {aa} data-i18n-html>{ako}</p>
        <a href="mailto:howintlsoft@gmail.com">howintlsoft@gmail.com</a>
        <a href="https://howglobal.co.kr">howglobal.co.kr</a>
      </div>
    </div>
    <div class="fbot">
      <span class="cc">© <span id="year">2026</span> HOW INTERNATIONAL. ALL RIGHTS RESERVED.</span>
      <span class="admin"><a {ada} href="admin.html">{adko}</a></span>
    </div>
  </div>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/firebase-config.js"></script>
<script src="assets/i18n.js"></script>
<script type="module" src="assets/firebase.js"></script>
<script src="assets/app.js"></script>
</body></html>""".format(fa=fa,fko=fko,sa=sa,sko=sko,ca=ca,cko=cko,ba=ba,bko=bko,aa=aa,ako=ako,ada=ada,adko=adko,
        nb=nav("nav.business","business"),na=nav("nav.about","about"),nn=nav("nav.news","news"),
        nl=nav("nav.library","library"),nc=nav("nav.contact","contact"))

PAGES = {"business":"business.html","about":"about.html","news":"news.html","library":"library.html","contact":"contact.html"}

def E(key, tag=None, cls=None, html=False):
    a,ko = w(None,key,tag_html=html)
    tag = tag or "span"; cls = (' class="%s"'%cls) if cls else ""
    return "<%s%s %s>%s</%s>" % (tag,cls,a,ko,tag)

# ---------------------------------------------------------------- pages
def home():
    def txt(k): return T[k][0]
    def A(k,html=False):
        a,_=w(None,k,tag_html=html); return a
    row = '''<div class="row">
      <span class="rno">{no}</span>
      <div class="rname">{name}<small>{sub}</small></div>
      <div class="rdesc"><span class="tag" {tga}>{tg}</span><span {da}>{d}</span></div>
      <a class="rlink" href="{href}" target="_blank" rel="noopener">{label} <span class="arw">↗</span></a>
    </div>'''
    def R(no,name,sub,tgk,dk,href,lk):
        tga,tg=w(None,tgk); da,d=w(None,dk); la,ll=w(None,lk) if lk else ("","")
        label = ll if lk else href.replace("https://","").replace("/","")
        lbl = ('<span %s>%s</span>'%(la,ll)) if lk else href.replace("https://","").rstrip("/")
        return row.format(no=no,name=name,sub=sub,tga=tga,tg=tg,da=da,d=d,href=href,label=lbl)
    c = header()
    c += """<main>
  <section class="hero">
    <div class="wrap">
      <span class="eyebrow rv" {eyA}>{eyK}</span>
      <h1 class="rv d1" {h1A}>{h1K}</h1>
      <p class="lead rv d2" {ldA}>{ldK}</p>
      <div class="cta rv d3">
        <a class="btn blue" {c1A} href="contact.html">{c1K}</a>
        <a class="btn ghost" {c2A} href="business.html">{c2K}</a>
      </div>
      <div class="divs rv d4">
        <div class="divcol"><span class="no">DIV. 01</span><h3 {d1tA}>{d1tK}</h3><div class="lt">Distribution</div><p {d1pA}>{d1pK}</p></div>
        <div class="divcol"><span class="no">DIV. 02</span><h3 {d2tA}>{d2tK}</h3><div class="lt">Software</div><p {d2pA}>{d2pK}</p></div>
      </div>
    </div>
  </section>
  <div class="strip">
    <div class="wrap">
      <div class="stat"><div class="k" {k1A}>{k1K}</div><div class="v" {v1A}>{v1K}</div></div>
      <div class="stat"><div class="k" {k2A}>{k2K}</div><div class="v" {v2A}>{v2K}</div></div>
      <div class="stat"><div class="k" {k3A}>{k3K}</div><div class="v" {v3A}>{v3K}</div></div>
      <div class="stat"><div class="k" {k4A}>{k4K}</div><div class="v" {v4A}>{v4K}</div></div>
    </div>
  </div>
  <section class="pad" id="business">
    <div class="wrap">
      <div class="shead">
        <div><span class="eyebrow rv" {beA}>{beK}</span><h2 class="rv d1" {bhA}>{bhK}</h2></div>
        <p class="note rv d2" {bnA}>{bnK}</p>
      </div>
      <div class="division rv">
        <div class="dhead"><span class="dno">DIV.01</span><span class="dttl" {d1tA}>{d1tK}</span><span class="dlt">Distribution</span><span class="ddesc" {dd1A}>{dd1K}</span></div>
        {rbio}{rpf}
      </div>
      <div class="division rv" style="margin-top:56px">
        <div class="dhead"><span class="dno">DIV.02</span><span class="dttl" {d2tA}>{d2tK}</span><span class="dlt">Software</span><span class="ddesc" {dd2A}>{dd2K}</span></div>
        {rms}{rkf}{rfa}
      </div>
    </div>
  </section>
  {part}
</main>""".format(
      eyA=A("home.eyebrow"),eyK=txt("home.eyebrow"),
      h1A=A("home.h1",True),h1K=txt("home.h1"),
      ldA=A("home.lead"),ldK=txt("home.lead"),
      c1A=A("home.cta1"),c1K=txt("home.cta1"),c2A=A("home.cta2"),c2K=txt("home.cta2"),
      d1tA=A("home.div1.t"),d1tK=txt("home.div1.t"),d1pA=A("home.div1.p"),d1pK=txt("home.div1.p"),
      d2tA=A("home.div2.t"),d2tK=txt("home.div2.t"),d2pA=A("home.div2.p"),d2pK=txt("home.div2.p"),
      k1A=A("strip.k1"),k1K=txt("strip.k1"),v1A=A("strip.v1"),v1K=txt("strip.v1"),
      k2A=A("strip.k2"),k2K=txt("strip.k2"),v2A=A("strip.v2"),v2K=txt("strip.v2"),
      k3A=A("strip.k3"),k3K=txt("strip.k3"),v3A=A("strip.v3"),v3K=txt("strip.v3"),
      k4A=A("strip.k4"),k4K=txt("strip.k4"),v4A=A("strip.v4"),v4K=txt("strip.v4"),
      beA=A("home.biz.eye"),beK=txt("home.biz.eye"),bhA=A("home.biz.h2",True),bhK=txt("home.biz.h2"),
      bnA=A("home.biz.note"),bnK=txt("home.biz.note"),
      dd1A=A("d1.ddesc"),dd1K=txt("d1.ddesc"),dd2A=A("d2.ddesc"),dd2K=txt("d2.ddesc"),
      rbio=R("01","바이오타맥스","BiotaMax","bio.tag","bio.desc","https://biotamax.co.kr",None),
      rpf=R("02","Painfree 8800","GM R&amp;D","pf.tag","pf.desc","https://painfree8800.com",None),
      rms=R("01","marketshare","분양몰 솔루션","ms.tag","ms.desc","https://marketshare-2e00c.web.app/","link.view"),
      rkf=R("02","KoreanFlow","한글학습 플랫폼","kf.tag","kf.desc","https://koreanflow.app",None),
      rfa=R("03","우리家 이야기","familya","fa.tag","fa.desc","https://familya.co.kr",None),
      part=partnership())
    return head("하우인터내셔널 — 검증된 유통, 우리가 만든 플랫폼",
                "하우인터내셔널은 미국·국산 우수 제품을 국내에 유통하고, 웹·앱 플랫폼을 자체 개발하는 회사입니다. 바이오타맥스, Painfree8800 유통 및 marketshare·KoreanFlow·familya 개발.",
                "/index.html","home",
                extra_ld=json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"하우인터내셔널","url":DOMAIN},ensure_ascii=False)) + c + footer()

def partnership(anchor=True):
    def txt(k): return T[k][0]
    def A(k,html=False): a,_=w(None,k,tag_html=html); return a
    return """<section class="pad part" id="partner">
    <div class="wrap">
      <div class="shead">
        <div><span class="eyebrow rv" {eA}>{eK}</span><h2 class="rv d1" {hA}>{hK}</h2></div>
        <p class="note rv d2" {nA}>{nK}</p>
      </div>
      <div class="pcards">
        <div class="pcard rv d1"><span class="pno">CH.01</span><h4 {c1A}>{c1K}</h4><div class="plt">Distribution Inquiry</div><p {p1A}>{p1K}</p><a class="go" {g1A} href="contact.html?type=distribution">{g1K}</a></div>
        <div class="pcard rv d2"><span class="pno">CH.02</span><h4 {c2A}>{c2K}</h4><div class="plt">Software Inquiry</div><p {p2A}>{p2K}</p><a class="go" {g2A} href="contact.html?type=software">{g2K}</a></div>
      </div>
      <div class="pcta rv d3"><a class="btn blue lg" {ctA} href="contact.html">{ctK}</a></div>
    </div>
  </section>""".format(
     eA=A("part.eye"),eK=txt("part.eye"),hA=A("part.h2",True),hK=txt("part.h2"),
     nA=A("part.note"),nK=txt("part.note"),
     c1A=A("part.ch1"),c1K=txt("part.ch1"),p1A=A("part.ch1.p"),p1K=txt("part.ch1.p"),g1A=A("part.ch1.go"),g1K=txt("part.ch1.go"),
     c2A=A("part.ch2"),c2K=txt("part.ch2"),p2A=A("part.ch2.p"),p2K=txt("part.ch2.p"),g2A=A("part.ch2.go"),g2K=txt("part.ch2.go"),
     ctA=A("part.cta"),ctK=txt("part.cta"))

def subhero(crumbk, h1k, leadk):
    def txt(k): return T[k][0]
    def A(k,html=False): a,_=w(None,k,tag_html=html); return a
    return """<section class="subhero">
    <div class="wrap">
      <div class="crumb rv" {cA}>{cK}</div>
      <h1 class="rv d1" {hA}>{hK}</h1>
      <p class="rv d2" {lA}>{lK}</p>
    </div>
  </section>""".format(cA=A(crumbk),cK=txt(crumbk),hA=A(h1k,True),hK=txt(h1k),lA=A(leadk),lK=txt(leadk))

def about():
    def txt(k): return T[k][0]
    def A(k,html=False): a,_=w(None,k,tag_html=html); return a
    def val(no,tk,pk):
        return '<div class="v"><span class="vn">V.0%s</span><h5 %s>%s</h5><p %s>%s</p></div>'%(no,A(tk),txt(tk),A(pk),txt(pk))
    def inf(k,vk=None,vtext=None,html=False):
        la,lk=w(None,k)
        if vk: va,vv=w(None,vk,tag_html=html); return '<div><dt %s>%s</dt><dd %s>%s</dd></div>'%(la,lk,va,vv)
        return '<div><dt %s>%s</dt><dd>%s</dd></div>'%(la,lk,vtext)
    body = header() + subhero("about.crumb","about.h1","about.lead")
    body += """<section class="pad"><div class="wrap">
      <div class="cols">
        <div><span class="eyebrow rv" {eA}>{eK}</span><p class="big rv d1" style="margin-top:16px" {bA}>{bK}</p></div>
        <div class="prose rv d2"><p {p1A}>{p1K}</p><p {p2A}>{p2K}</p></div>
      </div>
    </div></section>
    <section class="pad tight" style="background:var(--mist);border-top:1px solid var(--line)"><div class="wrap">
      <span class="eyebrow rv" {e2A}>{e2K}</span>
      <div class="valuegrid rv d1" style="margin-top:24px">{v1}{v2}{v3}</div>
    </div></section>
    <section class="pad"><div class="wrap">
      <span class="eyebrow rv" {e3A}>{e3K}</span>
      <dl class="info rv d1" style="margin-top:24px">
        {i1}{i2}{i3}{i4}{i5}{i6}
      </dl>
    </div></section>""".format(
      eA=A("about.eye"),eK=txt("about.eye"),bA=A("about.big"),bK=txt("about.big"),
      p1A=A("about.p1"),p1K=txt("about.p1"),p2A=A("about.p2"),p2K=txt("about.p2"),
      e2A=A("about.eye2"),e2K=txt("about.eye2"),v1=val(1,"val1.t","val1.p"),v2=val(2,"val2.t","val2.p"),v3=val(3,"val3.t","val3.p"),
      e3A=A("about.eye3"),e3K=txt("about.eye3"),
      i1=inf("info.name",vtext="하우인터내셔널 (HOW INTERNATIONAL)"),
      i2=inf("info.biz","info.biz.v"),
      i3=inf("info.regno",vtext="214-88-51839"),
      i4=inf("info.addr","info.addr.v"),
      i5=inf("info.email",vtext='<a href="mailto:howintlsoft@gmail.com" style="color:var(--blue)">howintlsoft@gmail.com</a>'),
      i6=inf("info.web",vtext='<a href="https://howglobal.co.kr" style="color:var(--blue)">howglobal.co.kr</a>'))
    return head("회사소개 — 하우인터내셔널","검증된 제품을 유통하고 필요한 소프트웨어를 직접 개발하는 하우인터내셔널을 소개합니다. 사업자등록번호 214-88-51839.","/about.html","about") + body + footer()

def business():
    def txt(k): return T[k][0]
    def A(k,html=False): a,_=w(None,k,tag_html=html); return a
    def item(tag,name,sub,pk,l1,l2,l3,href,linkk="link.site"):
        return """<div class="pitem rv">
        <span class="ptag">{tag}</span>
        <h4>{name}</h4><div class="psub">{sub}</div>
        <p {pA}>{pK}</p>
        <ul><li {a1}>{k1}</li><li {a2}>{k2}</li><li {a3}>{k3}</li></ul>
        <a class="plink" href="{href}" target="_blank" rel="noopener"><span {la}>{lk}</span> ↗</a>
      </div>""".format(tag=tag,name=name,sub=sub,pA=A(pk),pK=txt(pk),
                a1=A(l1),k1=txt(l1),a2=A(l2),k2=txt(l2),a3=A(l3),k3=txt(l3),
                href=href,la=A(linkk),lk=txt(linkk))
    prod_ld = json.dumps({"@context":"https://schema.org","@type":"ItemList","itemListElement":[
        {"@type":"Product","position":1,"name":"바이오타맥스","description":"미국 직수입 토양생균제","url":"https://biotamax.co.kr"},
        {"@type":"Product","position":2,"name":"Painfree 8800","description":"KFDA Class III 6-in-1 통증치료 의료기기","url":"https://painfree8800.com"}
    ]},ensure_ascii=False)
    body = header() + subhero("biz.crumb","biz.h1","biz.lead")
    body += """<section class="pad"><div class="wrap">
      <span class="eyebrow rv" {d1A}>{d1K}</span>
      <div class="pdetail">{bio}{pf}</div>
    </div></section>
    <section class="pad tight" style="background:var(--mist);border-top:1px solid var(--line)"><div class="wrap">
      <span class="eyebrow rv" {d2A}>{d2K}</span>
      <div class="pdetail" style="grid-template-columns:1fr 1fr 1fr">{ms}{kf}{fa}</div>
    </div></section>
    {part}""".format(
      d1A=A("biz.d1.eye"),d1K=txt("biz.d1.eye"),
      bio=item("Distribution · Agriculture","바이오타맥스","Imported from USA · Soil probiotic","bio.p","bio.li1","bio.li2","bio.li3","https://biotamax.co.kr"),
      pf=item("Distribution · Medical","Painfree 8800","KFDA Class III · GM R&amp;D","pf.p","pf.li1","pf.li2","pf.li3","https://painfree8800.com"),
      d2A=A("biz.d2.eye"),d2K=txt("biz.d2.eye"),
      ms=item("Software · PropTech","marketshare","분양몰 솔루션","ms.p","ms.li1","ms.li2","ms.li3","https://marketshare-2e00c.web.app/","link.view"),
      kf=item("Software · EdTech","KoreanFlow","koreanflow.app","kf.p","kf.li1","kf.li2","kf.li3","https://koreanflow.app"),
      fa=item("Software · Family","우리家 이야기","familya.co.kr","fa.p","fa.li1","fa.li2","fa.li3","https://familya.co.kr"),
      part=partnership())
    return head("사업분야 — 하우인터내셔널","유통(바이오타맥스·Painfree8800)과 소프트웨어 개발(marketshare·KoreanFlow·familya). 하우인터내셔널의 사업분야를 소개합니다.","/business.html","business",extra_ld=prod_ld) + body + footer()

def listpage(kind):
    def txt(k): return T[k][0]
    def A(k,html=False): a,_=w(None,k,tag_html=html); return a
    crumb,h1,lead = (kind+".crumb",kind+".h1",kind+".lead") if kind=="news" else ("lib.crumb","lib.h1","lib.lead")
    hostid = "news-list" if kind=="news" else "library-list"
    title = "뉴스 — 하우인터내셔널" if kind=="news" else "자료실 — 하우인터내셔널"
    desc = "하우인터내셔널의 새로운 소식과 보도자료." if kind=="news" else "하우인터내셔널 회사소개서·제품 카탈로그·브로슈어 다운로드."
    path = "/news.html" if kind=="news" else "/library.html"
    page = "news" if kind=="news" else "library"
    body = header() + subhero(crumb,h1,lead)
    body += """<section class="pad"><div class="wrap">
      <div id="{hid}" class="rv"><div class="empty"><span class="mono">LOADING</span><p>불러오는 중…</p></div></div>
    </div></section>""".format(hid=hostid)
    return head(title,desc,path,page) + body + footer()

def contact():
    def txt(k): return T[k][0]
    def A(k,html=False): a,_=w(None,k,tag_html=html); return a
    def PH(k): a,_=w(None,k); return 'data-i18n-ph="%s" placeholder="%s"'%(k,txt(k))
    body = header() + subhero("ct.crumb","ct.h1","ct.lead")
    body += """<section class="pad"><div class="wrap">
      <div class="contact-grid">
        <form id="inquiry-form" novalidate>
          <div class="field">
            <label {tlA}>{tlK}</label>
            <div class="seg">
              <label><input type="radio" name="type" value="distribution" checked> <span {tdA}>{tdK}</span></label>
              <label><input type="radio" name="type" value="software"> <span {tsA}>{tsK}</span></label>
            </div>
          </div>
          <div class="two">
            <div class="field"><label {nA}>{nK} <span class="req">*</span></label><input name="name" {phn} required></div>
            <div class="field"><label {coA}>{coK}</label><input name="company" {phc}></div>
          </div>
          <div class="two">
            <div class="field"><label {eA}>{eK} <span class="req">*</span></label><input name="email" type="email" {phe} required></div>
            <div class="field"><label {phA}>{phK}</label><input name="phone" {php}></div>
          </div>
          <div class="field"><label {mA}>{mK} <span class="req">*</span></label><textarea name="message" {phm} required></textarea></div>
          <label class="consent"><input type="checkbox" name="consent"> <span {csA}>{csK}</span></label>
          <button class="btn blue lg" type="submit" {sA}>{sK}</button>
          <p class="formnote" {fnA}>{fnK}</p>
        </form>
        <aside class="aside-card rv d1">
          <h4 {asA}>{asK}</h4>
          <dl class="info">
            <div><dt>Email</dt><dd><a href="mailto:howintlsoft@gmail.com" style="color:var(--blue)">howintlsoft@gmail.com</a></dd></div>
            <div><dt {adA}>{adK}</dt><dd data-i18n="info.addr.v" data-i18n-html>{adv}</dd></div>
            <div><dt {rgA}>{rgK}</dt><dd>214-88-51839</dd></div>
          </dl>
        </aside>
      </div>
    </div></section>""".format(
      tlA=A("ct.type"),tlK=txt("ct.type"),tdA=A("ct.type.d"),tdK=txt("ct.type.d"),tsA=A("ct.type.s"),tsK=txt("ct.type.s"),
      nA=A("ct.name"),nK=txt("ct.name"),phn=PH("ph.name"),
      coA=A("ct.company"),coK=txt("ct.company"),phc=PH("ph.company"),
      eA=A("ct.email"),eK=txt("ct.email"),phe=PH("ph.email"),
      phA=A("ct.phone"),phK=txt("ct.phone"),php=PH("ph.phone"),
      mA=A("ct.msg"),mK=txt("ct.msg"),phm=PH("ph.msg"),
      csA=A("ct.consent"),csK=txt("ct.consent"),sA=A("ct.submit"),sK=txt("ct.submit"),
      fnA=A("ct.formnote"),fnK=txt("ct.formnote"),
      asA=A("ct.aside"),asK=txt("ct.aside"),adA=A("info.addr"),adK=txt("info.addr"),adv=txt("info.addr.v"),
      rgA=A("info.regno"),rgK=txt("info.regno"))
    return head("협력 문의 — 하우인터내셔널","유통 제휴 또는 소프트웨어 개발 의뢰를 문의하세요. howintlsoft@gmail.com","/contact.html","contact") + body + footer()

# ---------------------------------------------------------------- write i18n.js
def write_i18n():
    d = {k:{"ko":v[0],"en":v[1]} for k,v in T.items()}
    js = "window.I18N = " + json.dumps(d, ensure_ascii=False, indent=0) + ";\n"
    open(os.path.join(OUT,"assets","i18n.js"),"w",encoding="utf-8").write(js)

# ---------------------------------------------------------------- SEO/config
def seo_and_config():
    pages = ["index.html","about.html","business.html","news.html","library.html","contact.html"]
    urls = "".join('  <url><loc>%s/%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>\n'
                   %(DOMAIN,p,"1.0" if p=="index.html" else "0.7") for p in pages)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>\n'
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sitemap)
    open(os.path.join(OUT,"robots.txt"),"w").write("User-agent: *\nAllow: /\nDisallow: /admin.html\n\nSitemap: %s/sitemap.xml\n"%DOMAIN)
    manifest = {"name":"하우인터내셔널","short_name":"HOW","start_url":"/","display":"standalone",
                "background_color":"#ffffff","theme_color":"#0000FF",
                "icons":[{"src":"/assets/how-logo.png","sizes":"any","type":"image/png"}]}
    open(os.path.join(OUT,"site.webmanifest"),"w",encoding="utf-8").write(json.dumps(manifest,ensure_ascii=False,indent=2))
    # NOTE: Firebase/설정 파일(firebase.json, .firebaserc, firestore.rules, storage.rules,
    #       firebase-config.js)은 리포지토리 정식 소스로 관리합니다. 여기서 생성하지 않습니다.

# ---------------------------------------------------------------- run
def main():
    write_i18n()
    files = {
      "index.html":home(),
      "about.html":about(),
      "business.html":business(),
      "news.html":listpage("news"),
      "library.html":listpage("library"),
      "contact.html":contact(),
    }
    for name,html in files.items():
        open(os.path.join(OUT,name),"w",encoding="utf-8").write(html)
    seo_and_config()
    print("generated:", ", ".join(sorted(files)))
    print("i18n keys:", len(T))

if __name__=="__main__":
    main()
