# -*- coding: utf-8 -*-
import json, os, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
DOMAIN = "https://howglobal.co.kr"

def asset_ver():
    h = hashlib.md5()
    for p in ("assets/styles.css", "assets/app.js"):
        fp = os.path.join(OUT, p)
        if os.path.exists(fp): h.update(open(fp, "rb").read())
    h.update(json.dumps(T, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    return h.hexdigest()[:8]

# ---------------------------------------------------------------- i18n
T = {
 # nav / cta
 "nav.business":("사업분야","Business"),
 "nav.portfolio":("포트폴리오","Portfolio"),
 "nav.about":("회사소개","About"),
 "nav.news":("뉴스","News"),
 "nav.library":("자료실","Library"),
 "cta.header":("견적 상담 →","Get a quote →"),
 # footer
 "foot.tagline":("검증된 제품을 유통하고, 건강을 지키고, 필요한 플랫폼을 직접 만드는 하나의 팀.",
                 "Distributing proven products, protecting health, and building the platforms you need — from one team."),
 "foot.sitemap":("사이트맵","Sitemap"),
 "foot.brands":("브랜드","Brands"),
 "foot.company":("회사정보","Company"),
 "foot.quote":("견적 상담","Get a quote"),
 "foot.name":("하우인터내셔널","HOW INTERNATIONAL"),
 "foot.bizno":("사업자등록번호 214-88-51839","Biz. Reg. 214-88-51839"),
 "foot.addr":("경기도 화성시 동탄광역환승로73",
              "73 Dongtan-gwangyeokhwanseung-ro,<br>Hwaseong-si, Gyeonggi-do, Korea"),
 "foot.admin":("· 관리자","· Admin"),
 # home hero
 "home.eyebrow":("글로벌 디지털미디어 × 헬스케어 × 유통 × 에너지","Global Digital Media × Healthcare × Distribution × Energy"),
 "home.h1":("필요한 플랫폼을 만들고,<br>건강을 지키고,<br>검증된 제품을 유통합니다.",
            "We build the platforms you need,<br>protect your health,<br>and distribute proven products."),
 "home.lead":("하우인터내셔널은 디지털미디어·헬스케어·유통·에너지 네 영역에서 각기 검증된 결과를 만듭니다.",
              "HOW International delivers proven results across digital media, healthcare, distribution, and energy."),
 "home.cta1":("사업분야 살펴보기 →","Explore our business →"),
 "home.cta2":("견적 상담하기","Get a quote"),
 "legend.hq":("본사 · 화성, 대한민국","HQ · Hwaseong, Korea"),
 "legend.origin":("수입 원산지 · 미국","Import origin · USA"),
 "legend.reach":("플랫폼 도달 · 14개 언어","Platform reach · 14 languages"),
 # 3-division overview (home)
 "ov.eye":("사업분야","What we do"),
 "ov.h2":("사업부는 다르지만,<br>기준은 하나입니다.","Three divisions,<br>one standard."),
 "ov.note":("서로 다른 영역이지만, 좋은 것을 알아보고 끝까지 책임진다는 원칙은 같습니다.",
            "Different domains, same discipline: recognize what's good and stand behind it."),
 "ov.d1.no":("DIV. 01","DIV. 01"),
 "ov.d1.t":("디지털미디어사업부","Digital Media"),
 "ov.d1.lt":("기획 · 개발 · 운영","Plan · Build · Operate"),
 "ov.d1.p":("자체 웹·앱 플랫폼을 기획·개발·운영하고, 고객사의 개발 의뢰도 수행합니다.",
            "We plan, build and operate our own web & app platforms — and also develop custom platforms for clients."),
 "ov.d1.li1":("marketshare · KoreanFlow · familya","marketshare · KoreanFlow · familya"),
 "ov.d1.li2":("고객 맞춤 플랫폼 개발 (수탁)","Custom platform development for clients"),
 "ov.d1.go":("포트폴리오 보기 →","View portfolio →"),
 "ov.d2.no":("DIV. 02","DIV. 02"),
 "ov.d2.t":("헬스케어사업부","Healthcare"),
 "ov.d2.lt":("의료기기 · 인증 · 공급","Medical Device · Certified · Supply"),
 "ov.d2.p":("KFDA 허가 의료기기를 병·의원·재활 네트워크에 공급합니다.",
            "We supply KFDA-approved medical devices to clinics, hospitals, and rehabilitation networks."),
 "ov.d2.li1":("Painfree 8800 · KFDA Class III 의료기기","Painfree 8800 · KFDA Class III medical device"),
 "ov.d2.go":("헬스케어 사업 보기 →","View healthcare →"),
 "ov.d3.no":("DIV. 03","DIV. 03"),
 "ov.d3.t":("유통사업부","Distribution"),
 "ov.d3.lt":("유통 · 총판 · B2B","Distribution · Agency · B2B"),
 "ov.d3.p":("해외에서 검증된 제품을 발굴해 국내 시장에 안정적으로 공급합니다.",
            "We source proven products from overseas and supply them reliably to the domestic market."),
 "ov.d3.li1":("바이오타맥스 · 미국 직수입 토양생균제","BiotaMax · U.S. direct-import soil probiotic"),
 "ov.d3.go":("유통 사업 보기 →","View distribution →"),
 # why HOW (home dark section)
 "std.eye":("왜 HOW인가","Why HOW"),
 "std.h2":("글로벌 기준,<br>로컬 책임.","Global standard,<br>local accountability."),
 "std.note":("유행이 아니라 근거로 판단하고, 공급·출시 이후까지 함께합니다.",
             "We judge by evidence, not trend — and stay involved long after the sale or launch."),
 "std.v1.t":("검증 우선","Verified first"),
 "std.v1.p":("인증·품질·데이터로 확인된 것만 다룹니다. 미국 직수입부터 KFDA 허가까지.",
             "Certifications, quality and data — we only handle what can be proven."),
 "std.v2.t":("끝까지 책임","Accountable to the end"),
 "std.v2.p":("유통·헬스케어는 공급 이후를, 미디어는 출시 이후를 함께합니다.",
             "Distribution and healthcare stay through supply; media stays through launch."),
 "std.v3.t":("직접 만든다","Built in-house"),
 "std.v3.p":("핵심 역량을 회사 안에 둡니다. 외주에 의존하지 않아 더 빠르고 유연합니다.",
             "We keep core capability inside — faster and more flexible without outsourcing risk."),
 # partnership CTA (home + business)
 "part.eye":("협력","Partnership"),
 "part.h2":("언제든 협력할<br>준비가 되어 있습니다.","Ready to work<br>with you anytime."),
 "part.note":("사업부에 맞는 채널로 먼저 이야기를 들려주세요. 빠르게 회신드립니다.",
              "Tell us what you need through the right channel. We'll get back to you quickly."),
 "part.cta":("견적 상담 폼 열기 →","Open the quote form →"),
 # business page
 "biz.crumb":("사업분야","Business"),
 "biz.h1":("사업분야","Business"),
 "biz.lead":("디지털미디어·헬스케어·유통 세 영역에서, 하우인터내셔널은 각기 다른 방식으로 신뢰를 만들어가고 있습니다.",
             "Across digital media, healthcare and distribution, HOW International builds trust in its own way."),
 # business div1 — digital media
 "biz.d1.eye":("DIV. 01 · 디지털미디어사업부","DIV. 01 · Digital Media"),
 "biz.d1.h2":("고객사가 원하는 고객 맞춤형 플랫폼을 제작해 드립니다.",
              "We build the custom platform your clients need."),
 "biz.d1.lead":("자사 플랫폼을 직접 기획·개발·운영하며, 고객이 필요로 하는 웹·앱 플랫폼 개발도 의뢰받아 수행합니다.",
                "We build and operate our own platforms — and also develop custom web & app solutions for clients."),
 # business div2 — healthcare
 "biz.d2.eye":("DIV. 02 · 헬스케어사업부","DIV. 02 · Healthcare"),
 "biz.d2.h2":("인증된 의료기기를 국내에 공급합니다.","We supply certified medical devices domestically."),
 "biz.d2.lead":("KFDA 허가 의료기기 공급 및 병·의원·재활 네트워크 구축.",
                "KFDA-approved device supply and clinic/rehabilitation network development."),
 # business div3 — distribution
 "biz.d3.eye":("DIV. 03 · 유통사업부","DIV. 03 · Distribution"),
 "biz.d3.h2":("검증된 제품, 발굴하고 공급합니다.","Proven products, sourced & supplied."),
 "biz.d3.lead":("해외 우수 제품의 국내 총판 및 B2B 공급.",
                "Distributorship and B2B supply for verified products from overseas."),
 # business channels
 "biz.ch1":("미디어 개발·견적","Media Development & Quote"),
 "biz.ch1.p":("웹·앱 플랫폼 개발, 솔루션 도입, 기존 서비스 고도화 — 견적 상담을 바로 받을 수 있습니다.",
              "Web & app platform builds, solution adoption or service upgrades — request a quote directly."),
 "biz.ch1.go":("견적 상담 신청 →","Request a quote →"),
 "biz.ch2":("헬스케어 제휴","Healthcare Partnership"),
 "biz.ch2.p":("Painfree 8800의 병·의원·재활·요양 도입, 대리점 계약을 논의합니다.",
              "Discuss Painfree 8800 adoption at clinics, rehab facilities, and agency contracts."),
 "biz.ch2.go":("헬스케어 제휴 문의 →","Healthcare inquiry →"),
 "biz.ch3":("유통 제휴","Distribution Partnership"),
 "biz.ch3.p":("바이오타맥스의 총판·대리점·B2B 공급을 논의합니다. 신규 수입 품목 제안도 환영합니다.",
              "Discuss BiotaMax distributorships, agencies and B2B supply. New import proposals welcome."),
 "biz.ch3.go":("유통 제휴 문의 →","Distribution inquiry →"),
 # product data — digital media
 "ms.tag":("Digital Media · PropTech","Digital Media · PropTech"),
 "ms.sub":("분양몰 솔루션","Commerce-mall solution"),
 "ms.dp":("분양 현장을 온라인으로 옮긴 분양·관리 솔루션입니다.",
          "A leasing-style commerce solution that puts a sales floor online."),
 "ms.li1":("온라인 분양 관리","Online store leasing & management"),
 "ms.li2":("실시간 현황 · 정산","Real-time status & settlement"),
 "ms.link":("플랫폼 보기 ↗","View platform ↗"),
 "kf.tag":("Digital Media · EdTech","Digital Media · EdTech"),
 "kf.sub":("한국어 학습 플랫폼","Korean-learning platform"),
 "kf.dp":("외국인 학습자를 위한 한국어 학습 플랫폼입니다. 14개 언어를 지원합니다.",
          "A Korean-learning platform for global learners, supporting 14 languages."),
 "kf.li1":("AI 레슨 · 발음 훈련","AI lessons & pronunciation"),
 "kf.li2":("웹 · 모바일 · 게임형 학습","Web & mobile · gamified"),
 "fa.tag":("Digital Media · Family","Digital Media · Family"),
 "fa.name":("우리家 이야기","familya"),
 "fa.sub":("디지털 족보 플랫폼","Digital family record platform"),
 "fa.dp":("가족의 일상을 한 권의 책으로 엮는 디지털 족보 플랫폼입니다.",
          "A digital family-record platform that binds everyday moments into one book."),
 "fa.li1":("가계도 · 연대기","Family tree · timeline"),
 "fa.li2":("연감 PDF 자동 생성","Auto-generated PDF yearbook"),
 # product data — healthcare
 "pf.tag":("Healthcare · Medical Device","Healthcare · Medical Device"),
 "pf.sub":("KFDA Class III · GM R&D","KFDA Class III · GM R&D"),
 "pf.dp":("KFDA 허가를 받은 6-in-1 통합 통증치료 의료기기입니다. PSC·레이저·양자·초음파·PEMF·온열 6개 모듈을 하나의 콘솔에 담았습니다.",
          "A KFDA-approved 6-in-1 pain-therapy device — six treatment modules in a single console."),
 "pf.li1":("각각 KFDA 허가된 6개 치료 모듈","Six individually KFDA-approved modules"),
 "pf.li2":("비침습 통증 치료","Non-invasive pain therapy"),
 "pf.li3":("병·의원 · 재활 · 요양 도입","For clinics, rehab & care facilities"),
 # product data — distribution
 "bio.tag":("Distribution · Agriculture","Distribution · Agriculture"),
 "bio.sub":("Imported from USA · Soil probiotic","Imported from USA · Soil probiotic"),
 "bio.dp":("미국에서 직수입하는 토양생균제입니다. 10가지 유익한 토양 미생물이 작물의 병해를 예방하고 생육을 돕습니다.",
           "A soil probiotic imported directly from the U.S. Ten beneficial soil microbes prevent crop disease and promote healthy growth."),
 "bio.li1":("10종 유익 토양미생물 배합","Blend of 10 beneficial soil microbes"),
 "bio.li2":("작물 병해 예방 및 생육 촉진","Prevents disease, promotes growth"),
 "bio.li3":("친환경 농업 · 토양 개선","Eco-friendly farming · soil recovery"),
 "link.site":("공식 사이트 →","Official site →"),
 "link.view":("플랫폼 보기 ↗","View platform ↗"),
 # portfolio page
 "pf_page.crumb":("포트폴리오","Portfolio"),
 "pf_page.h1":("직접 만든 플랫폼과<br>함께 만든 프로젝트.","Platforms we built<br>and projects we built together."),
 "pf_page.lead":("자체 운영 중인 플랫폼과, 고객사를 위해 수행한 개발 프로젝트를 한 곳에 모았습니다.",
                 "Our own platforms and client projects — all in one place."),
 "pf_page.own.eye":("자체 플랫폼","Own platforms"),
 "pf_page.own.h2":("직접 기획·개발·운영합니다.","Planned, built and operated in-house."),
 "pf_page.client.eye":("외주 개발 프로젝트","Client projects"),
 "pf_page.client.h2":("고객사와 함께 만들었습니다.","Built together with our clients."),
 "pf_page.client.lead":("웹·앱 플랫폼 개발을 의뢰받아 수행한 프로젝트입니다.",
                         "Projects developed on commission for web & app platform clients."),
 "pf_page.cta.h2":("이런 프로젝트를<br>함께 만들고 싶으신가요?","Want to build<br>a project like this together?"),
 "pf_page.cta.p":("아이디어 단계도 괜찮습니다. 견적 상담으로 먼저 이야기해 보세요.",
                  "Even at the idea stage — let's talk through a quote consultation first."),
 "pf_page.cta.btn":("견적 상담 신청 →","Request a quote →"),
 # quote page
 "qt.crumb":("견적 상담 / 협력 문의","Quote & Inquiry"),
 "qt.h1":("견적 상담 / 협력 문의","Quote & Inquiry"),
 "qt.lead":("사업부와 문의 유형을 선택하면 필요한 정보만 간단히 입력할 수 있습니다. 1~2영업일 내 회신드립니다.",
            "Select a division and inquiry type to fill in only what's needed. We reply within 1–2 business days."),
 "qt.type.label":("문의 유형","Inquiry type"),
 "qt.type.dist":("유통 제휴","Distribution"),
 "qt.type.health":("헬스케어 제휴","Healthcare"),
 "qt.type.media":("미디어 개발·견적","Media Dev & Quote"),
 "qt.type.other":("기타 문의","Other"),
 "qt.quote.label":("견적 정보","Quote info"),
 "qt.budget":("예산 범위","Budget range"),
 "qt.projtype":("프로젝트 유형","Project type"),
 "qt.schedule":("희망 일정 / 마감","Desired timeline"),
 "qt.schedule.ph":("예: 2026년 12월 오픈 목표","e.g., Target launch Dec 2026"),
 "qt.ref":("참고 사이트 / 자료 링크","Reference site / link"),
 "qt.ref.ph":("https://... (선택)","https://... (optional)"),
 "qt.company":("회사명","Company"),
 "qt.company.ph":("주식회사 예시","Company name"),
 "qt.name":("담당자명","Name"),
 "qt.name.ph":("홍길동","Your name"),
 "qt.email":("이메일","Email"),
 "qt.email.ph":("name@company.com","name@company.com"),
 "qt.phone":("연락처","Phone"),
 "qt.phone.ph":("010-0000-0000","010-0000-0000"),
 "qt.msg":("문의 내용","Message"),
 "qt.msg.ph":("어떤 도움이 필요하신지 알려주세요.","Tell us how we can help."),
 "qt.consent":("개인정보 수집·이용에 동의합니다. 문의 처리 목적으로만 사용되며 처리 완료 후 파기됩니다.",
               "I agree to the collection and use of my information for the purpose of this inquiry."),
 "qt.submit":("문의 보내기 →","Send inquiry →"),
 "qt.formnote":('급하신 경우 <a href="mailto:howintlsoft@gmail.com">howintlsoft@gmail.com</a>으로 바로 메일 주셔도 됩니다.',
                'In urgent cases, email us at <a href="mailto:howintlsoft@gmail.com">howintlsoft@gmail.com</a>.'),
 "qt.aside.h":("사업부 직접 연결","Direct channel"),
 "qt.aside.dist":("BiotaMax 총판·B2B 문의","BiotaMax B2B inquiry"),
 "qt.aside.health":("Painfree 8800 도입·대리점","Painfree 8800 adoption"),
 "qt.aside.media":("플랫폼 개발·견적 상담","Platform dev & quote"),
 "qt.resp.l":("응답 시간","Response time"),
 "qt.resp.p":("평균 1~2영업일 내 회신드립니다. 견적 상담은 프로젝트 범위에 따라 조금 더 걸릴 수 있습니다.",
              "We typically reply within 1–2 business days. Quotes may take slightly longer depending on scope."),
 # about page
 "about.crumb":("회사소개","About"),
 "about.h1":("좋은 것을 알아보고,<br>끝까지 책임집니다.","We recognize what's good,<br>and stand behind it."),
 "about.lead":("하우인터내셔널은 검증된 제품을 유통하고, 건강을 지키고, 필요한 플랫폼을 직접 개발하는 회사입니다. 규모보다 신뢰를, 유행보다 지속을 우선합니다.",
               "HOW International distributes proven products, protects health, and builds the platforms it needs — favoring trust over scale, and longevity over trend."),
 "about.who.eye":("우리는","Who we are"),
 "about.who.big":("디지털미디어·헬스케어·유통, 서로 다른 일을 하지만 같은 기준으로 움직입니다.",
                  "Digital media, healthcare, distribution — different domains, one standard."),
 "about.p1":("디지털미디어사업부는 분양(marketshare), 한국어 학습(KoreanFlow), 디지털 족보(우리家 이야기) 등 자사 플랫폼을 직접 기획·개발·운영하고, 고객이 필요로 하는 웹·앱 플랫폼 개발도 함께 수행합니다.",
             "Our digital media division plans, builds and operates its own platforms — commerce (marketshare), Korean learning (KoreanFlow) and digital family records (familya) — and also develops web & app platforms for external clients."),
 "about.p2":("헬스케어사업부는 KFDA 허가를 받은 통증치료 의료기기 Painfree 8800을 병·의원·재활·요양 네트워크에 공급하고, 공급 이후의 사후관리까지 함께합니다.",
             "Our healthcare division supplies Painfree 8800 — a KFDA-approved pain-therapy device — to clinics, hospitals and rehabilitation networks, and stays involved in after-sales support."),
 "about.p3":("유통사업부는 미국에서 직수입한 토양생균제 바이오타맥스를 국내에 공급합니다. 좋은 제품을 발굴하고, 인증과 품질을 지키며, 고객이 신뢰할 수 있는 유통 경로를 만듭니다.",
             "Our distribution division supplies BiotaMax — a soil probiotic imported directly from the U.S. — maintaining certification and quality while building reliable supply channels."),
 "about.work.eye":("일하는 방식","How we work"),
 "av1.t":("검증 우선","Verified first"),
 "av1.p":("유행이 아니라 근거로 판단합니다. 인증·품질·데이터로 확인된 것만 다룹니다.",
          "We judge by evidence, not trend. Only what is confirmed by certification, quality and data."),
 "av2.t":("끝까지 책임","Accountable to the end"),
 "av2.p":("소개로 끝내지 않습니다. 유통·헬스케어는 공급 이후를, 미디어는 출시 이후를 함께합니다.",
          "We don't stop at introduction. Distribution and healthcare stay through supply; media stays through launch."),
 "av3.t":("직접 만든다","Built in-house"),
 "av3.p":("외주에 의존하지 않고 핵심 역량을 안에 둡니다. 그래서 더 빠르고 유연합니다.",
          "We keep core capability inside rather than relying on outsourcing — faster and more flexible."),
 "about.co.eye":("회사 정보","Company"),
 "info.name":("사명","Name"),
 "info.biz":("대표 사업","Business"),
 "info.biz.v":("디지털미디어 · 헬스케어 · 유통 · 에너지(ESCO)","Digital Media · Healthcare · Distribution · Energy (ESCO)"),
 "info.reg":("사업자등록번호","Biz. Reg."),
 "info.addr":("주소","Address"),
 "info.addr.v":("경기도 화성시 동탄광역환승로73",
                "73 Dongtan-gwangyeokhwanseung-ro, Hwaseong-si, Gyeonggi-do, Korea"),
 "info.email":("이메일","Email"),
 "info.web":("웹사이트","Website"),
 "about.cta.btn":("협력 · 견적 상담하기 →","Partner with us →"),
 # news / library
 "news.crumb":("뉴스","News"),
 "news.h1":("뉴스 · 공지","News & notices."),
 "news.lead":("유통 브랜드와 플랫폼, 회사 소식을 전합니다.",
              "Updates on our distribution brands, platforms and the company."),
 "lib.crumb":("자료실","Library"),
 "lib.h1":("자료실","Library."),
 "lib.lead":("브랜드·플랫폼 브로슈어, 스펙 시트 및 자료를 제공합니다.",
             "Brochures, spec sheets and documents for our brands and platforms."),
 # ===== ESCO (DIV.04 에너지사업부) =====
 "nav.esco":("ESCO","ESCO"),
 # home overview card (DIV.04)
 "ov.d4.no":("DIV. 04","DIV. 04"),
 "ov.d4.t":("에너지사업부","Energy"),
 "ov.d4.lt":("ESCO · 조명효율화 · 성과보증","ESCO · Lighting · Guaranteed"),
 "ov.d4.p":("초기비용 0원으로 노후 조명을 고효율 LED로 바꾸고, 절감액으로 상환하는 조명 ESCO 사업을 제안·총괄합니다.",
            "We propose and manage lighting-ESCO projects — upgrading aging lighting to high-efficiency LEDs at zero upfront cost, repaid from the savings."),
 "ov.d4.li1":("조명 ESCO · 무료 절감 진단","Lighting ESCO · free diagnosis"),
 "ov.d4.go":("에너지(ESCO) 보기 →","View energy (ESCO) →"),
 # business section (DIV.04)
 "biz.d4.eye":("DIV. 04 · 에너지사업부","DIV. 04 · Energy Division"),
 "biz.d4.h2":("초기비용 0원, 절감액으로 갚는 조명 ESCO.","Lighting ESCO — zero upfront, paid from savings."),
 "biz.d4.lead":("켑코이에스㈜·㈜투반산업과 함께 조명 ESCO 사업을 제안·총괄합니다. 노후 조명을 3세대 스마트 AI LED로 바꾸고 절감액으로 상환합니다.",
                "With KEPCO ES and Tuban Industry, we propose and manage lighting-ESCO projects — replacing aging lighting with 3rd-gen smart AI LEDs, repaid from savings."),
 "biz.d4.go1":("ESCO 자세히 보기 →","Learn more about ESCO →"),
 "biz.d4.go2":("무료 진단 신청 →","Request a free diagnosis →"),
 # quote type
 "qt.type.esco":("ESCO 진단","ESCO diagnosis"),
 "qt.esco.note":("조명 ESCO 무료 진단은 전용 페이지에서 시설 정보와 함께 신청하면 더 정확합니다.",
                 "For a lighting-ESCO diagnosis, the dedicated page lets you include facility details for a more accurate review."),
 "qt.esco.go":("ESCO 진단 신청 페이지로 →","Go to the ESCO diagnosis page →"),
 # --- esco page: hero ---
 "esco.crumb":("ESCO","ESCO"),
 "esco.eyebrow":("DIV. 04 · 에너지사업부 · ESCO","DIV. 04 · Energy Division · ESCO"),
 "esco.h1":("초기비용 0원,<br>아낀 전기요금으로 갚는 조명 교체",
            "Zero upfront cost,<br>lighting upgrades repaid from the energy you save"),
 "esco.lead":("노후 조명을 3세대 스마트 AI LED로 바꾸고, 공사비는 매달 줄어든 전기요금 안에서만 나누어 갚습니다. 계약이 끝나면 절감액은 전부 고객의 몫입니다.",
              "Replace aging lighting with 3rd-gen smart AI LEDs and repay the cost only from your reduced monthly bills. When the contract ends, all savings are yours."),
 "esco.kpi1.n":("0원","₩0"),
 "esco.kpi1.l":("초기 투자비","Upfront cost"),
 "esco.kpi2.n":("최대 70%대","Up to ~70%"),
 "esco.kpi2.l":("조명 전력 절감 (실측 사례 기준)","Lighting-power savings (measured cases)"),
 "esco.kpi3.n":("5년","5 years"),
 "esco.kpi3.l":("무상 A/S","Free A/S"),
 "esco.cta.apply":("무료 절감 진단 신청 →","Request a free savings diagnosis →"),
 "esco.cta.calc":("예상 절감액 계산하기","Estimate your savings"),
 # --- what is esco ---
 "esco.what.eye":("ESCO란?","What is ESCO?"),
 "esco.what.h2":("자금·기술 부담 없이<br>고효율 설비로.","High-efficiency equipment,<br>without the capital burden."),
 "esco.what.p":("ESCO(Energy Service Company)는 에너지 사용자가 자금·기술 부담 없이 고효율 설비로 바꿀 수 있도록, 전문 기업이 먼저 투자하고 절감액으로 돌려받는 에너지이용합리화법 기반 사업 방식입니다.",
                "ESCO (Energy Service Company) is a model under Korea's Energy Use Rationalization Act: a specialist firm invests first in high-efficiency equipment and recovers the cost from the resulting savings — so the user bears no upfront capital or technical burden."),
 "esco.flow1.t":("① 무료 진단","① Free diagnosis"),
 "esco.flow1.p":("고지서·등기구 조사","Review bills & fixtures"),
 "esco.flow2.t":("② 선투자·시공","② Investment & install"),
 "esco.flow2.p":("사업자가 전액 부담","Fully funded by the provider"),
 "esco.flow3.t":("③ 절감액 상환","③ Repay from savings"),
 "esco.flow3.p":("줄어든 요금 범위 안에서","Within the reduced bill"),
 "esco.flow4.t":("④ 계약 종료","④ Contract ends"),
 "esco.flow4.p":("설비는 고객 소유, 절감액 100% 고객 몫","Equipment yours; 100% of savings yours"),
 "esco.cmp.c0":("구분","Item"),
 "esco.cmp.c1":("자체 예산 교체","Self-funded"),
 "esco.cmp.c2":("ESCO","ESCO"),
 "esco.cmp.r1":("초기 비용","Upfront cost"),
 "esco.cmp.r1a":("수억 원","Hundreds of millions of won"),
 "esco.cmp.r1b":("0원","₩0"),
 "esco.cmp.r2":("재정 영향","Financial impact"),
 "esco.cmp.r2a":("일시 지출","Lump-sum outlay"),
 "esco.cmp.r2b":("절감액 내 분할 상환","Repaid within savings"),
 "esco.cmp.r3":("유지보수","Maintenance"),
 "esco.cmp.r3a":("자체 부담","Self-borne"),
 "esco.cmp.r3b":("5년 무상 A/S","5-yr free A/S"),
 "esco.cmp.r4":("성과 책임","Performance risk"),
 "esco.cmp.r4a":("사용자 부담","On the user"),
 "esco.cmp.r4b":("사업자 성과 보증","Provider-guaranteed"),
 # --- 3rd-gen LED ---
 "esco.led.eye":("3세대 스마트 AI LED","3rd-gen Smart AI LED"),
 "esco.led.h2":("오래 켤수록<br>차이가 커집니다.","The longer it runs,<br>the bigger the gap."),
 "esco.led.c0":("구분","Spec"),
 "esco.led.c1":("1세대 형광등","Gen 1 Fluorescent"),
 "esco.led.c2":("2세대 일체형 LED","Gen 2 Integrated LED"),
 "esco.led.c3":("3세대 스마트 AI LED","Gen 3 Smart AI LED"),
 "esco.led.r1":("1W당 밝기","Lumens per watt"),
 "esco.led.r1c":("160 lm 이상","160 lm+"),
 "esco.led.r2":("수명","Lifespan"),
 "esco.led.r2a":("3,000시간","3,000 hrs"),
 "esco.led.r2b":("20,000시간","20,000 hrs"),
 "esco.led.r2c":("100,000시간","100,000 hrs"),
 "esco.led.r3":("A/S","A/S"),
 "esco.led.r3a":("없음","None"),
 "esco.led.r3b":("1년 전후","~1 year"),
 "esco.led.r3c":("기본 5년 (최대 10년)","5 yrs (up to 10)"),
 "esco.led.r4":("고장 시","On failure"),
 "esco.led.r4ab":("전체 교체","Replace all"),
 "esco.led.r4c":("고장 부품만 교체","Swap faulty part only"),
 "esco.led.f1":("모듈형 구조","Modular structure"),
 "esco.led.f1p":("고장 부품만 교체해 유지비를 낮춥니다.","Swap only the faulty part to cut maintenance cost."),
 "esco.led.f2":("모션 감지 디밍","Motion-sensing dimming"),
 "esco.led.f2p":("사람·차량이 없으면 최저 밝기, 감지 즉시 최대 밝기.","Dims to minimum when empty, full brightness on detection."),
 "esco.led.f3":("채광 연동 조도 제어","Daylight-linked control"),
 "esco.led.f3p":("자연 채광에 맞춰 밝기를 자동 조절합니다.","Auto-adjusts brightness to available daylight."),
 # --- targets ---
 "esco.tg.eye":("대상별 안내","By facility"),
 "esco.tg.h2":("어떤 시설이든<br>자주 켜는 곳부터.","Any facility —<br>starting where lights run most."),
 "esco.tg.ratelbl":("예상 절감률","Est. savings"),
 "esco.tg.speedlbl":("상환 속도","Payback"),
 "esco.tg.btn":("이 시설로 진단 신청 →","Request a diagnosis for this facility →"),
 "esco.tg.slownote":("사용 시간이 짧아 상환 기간이 길어질 수 있어, 자주 켜는 구역부터 적용하거나 여러 시설을 묶어 진행합니다.",
                     "With shorter usage hours, payback can take longer — so we start with the most-used areas or bundle multiple sites."),
 "esco.spd.vfast":("매우 빠름","Very fast"),
 "esco.spd.fast":("빠름","Fast"),
 "esco.spd.normal":("보통","Moderate"),
 "esco.spd.slow":("느림","Slow"),
 "esco.tg.apartment.n":("아파트","Apartments"),
 "esco.tg.apartment.s":("24시간 켜진 지하주차장이 핵심. 관리비 추가 부담 없이 교체합니다.",
                        "The 24/7 underground parking is the key — upgraded with no added maintenance fees."),
 "esco.tg.apartment.r":("약 70%","~70%"),
 "esco.tg.parking.n":("주차장·주차빌딩","Parking lots & garages"),
 "esco.tg.parking.s":("24시간 점등 + 모션 디밍으로 가장 큰 효과를 냅니다.",
                      "24/7 operation plus motion dimming delivers the biggest effect."),
 "esco.tg.parking.r":("약 75%","~75%"),
 "esco.tg.factory.n":("공장·물류센터","Factories & logistics"),
 "esco.tg.factory.s":("긴 점등 시간, 작업장 조도 기준·RE100 대응에 적합합니다.",
                      "Long operating hours; meets workplace lux standards and RE100 goals."),
 "esco.tg.factory.r":("약 65%","~65%"),
 "esco.tg.hospital.n":("병원·요양시설","Hospitals & care facilities"),
 "esco.tg.hospital.s":("24시간 복도·병동, 환자에게 편안한 빛을 제공합니다.",
                       "24/7 corridors and wards with comfortable light for patients."),
 "esco.tg.hospital.r":("약 50%","~50%"),
 "esco.tg.building.n":("일반빌딩","Commercial buildings"),
 "esco.tg.building.s":("운영비를 줄이고 임차인 관리비 경쟁력을 높입니다.",
                       "Lowers operating cost and improves tenant competitiveness."),
 "esco.tg.building.r":("약 60%","~60%"),
 "esco.tg.retail.n":("대형마트·판매시설","Retail & big-box stores"),
 "esco.tg.retail.s":("매장은 더 밝게, 전기요금은 더 적게.","Brighter sales floors, lower electricity bills."),
 "esco.tg.retail.r":("약 60%","~60%"),
 "esco.tg.public.n":("지자체·공공기관","Government & public"),
 "esco.tg.public.s":("본예산 없이 에너지 절감 의무·탄소중립 실적을 달성합니다.",
                     "Meets energy-saving mandates and carbon-neutrality targets without a capital budget."),
 "esco.tg.public.r":("약 60%","~60%"),
 "esco.tg.university.n":("대학교","Universities"),
 "esco.tg.university.s":("도서관·연구동 등 장시간 사용 건물부터 적용합니다.",
                        "Starting with long-use buildings like libraries and research halls."),
 "esco.tg.university.r":("약 55%","~55%"),
 "esco.tg.school.n":("학교·유치원","Schools & kindergartens"),
 "esco.tg.school.s":("교실 조도 기준(책상면 300럭스)과 학생 눈 건강을 지킵니다.",
                     "Keeps classroom lux standards (300 lx at the desk) and protects students' eyes."),
 "esco.tg.school.r":("약 65%","~65%"),
 "esco.tg.church.n":("교회·종교시설","Churches & religious"),
 "esco.tg.church.s":("헌금의 청지기적 사용, 영상 예배에 깜빡임 없는 조명.",
                     "Faithful stewardship of giving, with flicker-free light for recorded worship."),
 "esco.tg.church.r":("약 55%","~55%"),
 "esco.tg.welfare.n":("사회복지시설","Welfare facilities"),
 "esco.tg.welfare.s":("운영비를 복지 서비스로, 어르신 낙상 예방에도 도움.",
                      "Turns operating cost into welfare service and helps prevent falls among seniors."),
 "esco.tg.welfare.r":("약 45%","~45%"),
 # --- calculator ---
 "esco.calc.eye":("간이 절감 계산기","Quick savings estimator"),
 "esco.calc.h2":("1분이면<br>대략 가늠해 볼 수 있습니다.","A rough estimate<br>in about a minute."),
 "esco.calc.flbl":("시설 유형","Facility type"),
 "esco.calc.blbl":("월평균 전기요금 (원)","Avg. monthly electricity bill (KRW)"),
 "esco.calc.blbl.apt":("월평균 공용 전기요금 (원)","Avg. monthly common-area bill (KRW)"),
 "esco.calc.bph":("예: 2,000,000","e.g., 2,000,000"),
 "esco.calc.btn":("예상 절감액 보기","See estimated savings"),
 "esco.calc.applybtn":("이 조건으로 진단 신청 →","Apply with these details →"),
 "esco.calc.resultpre":("예상 절감","Estimated savings"),
 "esco.calc.month":("월","month"),
 "esco.calc.year":("연","year"),
 "esco.calc.unit":("만원","0k KRW"),
 "esco.calc.disclaimer":("이 결과는 업종 평균을 가정한 대략적인 범위입니다. 실제 절감액은 고지서와 현장 조사를 바탕으로 한 무료 진단 후 확정됩니다.",
                         "This is a rough range based on industry averages. Actual savings are confirmed after a free on-site diagnosis using your bills."),
 # --- cases ---
 "esco.case.eye":("실증 사례","Proven cases"),
 "esco.case.h2":("숫자로 증명된<br>절감입니다.","Savings proven<br>in numbers."),
 "esco.case.c0":("현장","Site"),
 "esco.case.c1":("내용","Scope"),
 "esco.case.c2":("결과","Result"),
 "esco.case.r1s":("천안 지하주차장","Cheonan underground parking"),
 "esco.case.r1c":("938개 교체, 10~60 lx → 50~150 lx","938 fixtures, 10–60 lx → 50–150 lx"),
 "esco.case.r1r":("일 720 → 202 kWh (72% 절감)","720 → 202 kWh/day (−72%)"),
 "esco.case.r2s":("서울시설공단 영남주차장","Seoul Facilities Corp. Yeongnam parking"),
 "esco.case.r2c":("160개 (40W→18W)","160 fixtures (40W→18W)"),
 "esco.case.r2r":("일 154 → 50 kWh (60% 절감)","154 → 50 kWh/day (−60%)"),
 "esco.case.r3s":("울산 상북 하나로마트","Ulsan Sangbuk Hanaro Mart"),
 "esco.case.r3c":("실내등 200개, 680~800 lx → 1,200~1,400 lx","200 indoor fixtures, 680–800 lx → 1,200–1,400 lx"),
 "esco.case.r3r":("일 120 → 72 kWh (40% 절감)","120 → 72 kWh/day (−40%)"),
 "esco.case.r4s":("산업 현장 계약","Industrial site contract"),
 "esco.case.r4c":("2025년 10월 대형 타이어 제조공장 LED 에너지효율화사업 계약","Oct 2025 — LED efficiency contract, large tire plant"),
 "esco.case.r4r":("사업금액 약 8.4억 원","Contract value ≈ ₩840M"),
 # --- structure ---
 "esco.str.eye":("사업 구조","Structure"),
 "esco.str.h2":("네 주체가<br>함께 책임집니다.","Four parties,<br>shared accountability."),
 "esco.str.user.t":("에너지사용자","Energy user"),
 "esco.str.user.p":("고객 — 의사결정·계약·절감액 내 상환","Customer — decisions, contract, repayment within savings"),
 "esco.str.esco.t":("에너지효율화사업자","Energy-efficiency provider"),
 "esco.str.esco.p":("켑코이에스㈜ — 사업 주관·금융·절감량 확인·성과 보증","KEPCO ES — project lead, financing, savings verification, performance guarantee"),
 "esco.str.epc.t":("EPC","EPC"),
 "esco.str.epc.p":("㈜투반산업 — 제조·시공·하자보증 60개월·A/S","Tuban Industry — manufacturing, installation, 60-mo warranty, A/S"),
 "esco.str.how.t":("하우인터내셔널 — 제안·사업 총괄","HOW International — proposal & program management"),
 "esco.str.how.p":("상담 창구, 무료 진단 연결, 의사결정 기구 설명 지원, 계약~준공 관리","Consultation desk, diagnosis coordination, decision-body support, contract-to-completion management"),
 "esco.str.steps.l":("진행 절차","Process"),
 "esco.str.step1":("상담·자료 접수","Intake & consultation"),
 "esco.str.step2":("현장 조사·진단 보고서","Site survey & diagnosis report"),
 "esco.str.step3":("내부 의결 (입대의·당회·운영위 등)","Internal approval (board/committee)"),
 "esco.str.step4":("3자 계약","Tripartite contract"),
 "esco.str.step5":("시공","Installation"),
 "esco.str.step6":("준공 실사·절감량 확인","Completion audit & savings check"),
 "esco.str.step7":("상환·사후관리","Repayment & after-care"),
 # --- faq ---
 "esco.faq.eye":("자주 묻는 질문","FAQ"),
 "esco.faq.h2":("궁금한 점,<br>먼저 답해 드립니다.","Answers,<br>before you ask."),
 "esco.faq.q1":("정말 초기 비용이 없나요?","Is there really no upfront cost?"),
 "esco.faq.a1":("공사비는 사업자가 먼저 부담하고, 줄어든 전기요금 범위 안에서만 상환합니다.",
                "The provider funds the work first, and you repay only within your reduced electricity bill."),
 "esco.faq.q2":("절감이 예상보다 적으면요?","What if savings fall short?"),
 "esco.faq.a2":("준공 후 실사로 절감량을 확인하며, 에너지 효율 보증서에 따라 성과 미달 책임은 사업자가 집니다.",
                "Savings are verified by a post-completion audit, and under the energy-efficiency guarantee the provider bears the risk of any shortfall."),
 "esco.faq.q3":("센서등이라 어둡지 않나요?","Won't sensor lighting be too dark?"),
 "esco.faq.a3":("사람·차량이 없을 때만 최저 밝기로 낮추고 감지 즉시 최대 밝기로 켜집니다. 실측 사례에서 평균 밝기는 오히려 높아졌습니다.",
                "It dims to minimum only when the area is empty and jumps to full brightness on detection. In measured cases, average brightness actually increased."),
 "esco.faq.q4":("계약 기간 중 고장 나면요?","What if something breaks during the contract?"),
 "esco.faq.a4":("5년 무상 A/S로, 고장 부품만 교체합니다.","Five years of free A/S — only the faulty part is replaced."),
 "esco.faq.q5":("계약이 끝나면 설비는 누구 것인가요?","Who owns the equipment after the contract?"),
 "esco.faq.a5":("고객 소유가 되고, 이후 절감액은 전부 고객 몫입니다.","It becomes yours, and all savings thereafter are entirely yours."),
 "esco.faq.q6":("진단에 비용이 드나요?","Does the diagnosis cost anything?"),
 "esco.faq.a6":("무료이며 계약 의무가 없습니다.","It's free and comes with no obligation to contract."),
 "esco.faq.q7":("어떤 자료가 필요한가요?","What documents are needed?"),
 "esco.faq.a7":("최근 1년분 전기요금 고지서(또는 한전 파워플래너 ID)와 사업자(고유번호)등록증이 필요합니다. 등기구 현황은 현장 조사로 파악합니다.",
                "The last 12 months of electricity bills (or your KEPCO PowerPlanner ID) and a business/registration certificate. Fixture details are captured during the site survey."),
 # --- apply form ---
 "esco.apply.eye":("무료 진단 신청","Free diagnosis"),
 "esco.apply.h2":("고지서만 있으면<br>시작할 수 있습니다.","If you have your bill,<br>we can start."),
 "esco.f.facility":("시설 유형","Facility type"),
 "esco.f.other":("기타","Other"),
 "esco.f.fname":("시설명","Facility name"),
 "esco.f.fname.ph":("예: ○○아파트, ○○교회","e.g., ○○ Apartments, ○○ Church"),
 "esco.f.region":("지역","Region"),
 "esco.f.region.ph":("예: 대전 서구","e.g., Seo-gu, Daejeon"),
 "esco.f.scale":("규모","Size"),
 "esco.f.scale.ph":("예: 1,500세대 / 연면적 5,000㎡ / 등기구 약 800개 (아는 만큼)",
                    "e.g., 1,500 units / 5,000㎡ / ~800 fixtures (as known)"),
 "esco.f.bill":("월평균 전기요금","Avg. monthly bill"),
 "esco.f.bill.0":("모름","Not sure"),
 "esco.f.bill.1":("100만원 미만","Under ₩1M"),
 "esco.f.bill.2":("100~300만원","₩1–3M"),
 "esco.f.bill.3":("300~1,000만원","₩3–10M"),
 "esco.f.bill.4":("1,000만원 이상","Over ₩10M"),
 "esco.f.role":("신청인 구분","Your role"),
 "esco.f.role.0":("선택","Select"),
 "esco.f.role.1":("관리사무소","Management office"),
 "esco.f.role.2":("입주자대표회의","Residents' council"),
 "esco.f.role.3":("시설·행정 담당","Facility / admin staff"),
 "esco.f.role.4":("대표·임원","Owner / executive"),
 "esco.f.role.5":("기타","Other"),
 "esco.f.name":("담당자명","Contact name"),
 "esco.f.name.ph":("홍길동","Your name"),
 "esco.f.phone":("연락처","Phone"),
 "esco.f.phone.ph":("010-0000-0000","010-0000-0000"),
 "esco.f.email":("이메일","Email"),
 "esco.f.email.ph":("name@company.com","name@company.com"),
 "esco.f.ctime":("연락 가능 시간","Best time to contact"),
 "esco.f.ctime.0":("언제든","Anytime"),
 "esco.f.ctime.1":("오전","Morning"),
 "esco.f.ctime.2":("오후","Afternoon"),
 "esco.f.note":("추가 요청사항","Notes"),
 "esco.f.note.ph":("현장 상황이나 궁금한 점을 적어주세요.","Tell us about your site or any questions."),
 "esco.f.consent":("개인정보 수집·이용에 동의합니다. 진단 상담 목적으로만 사용하며 상담 종료 후 파기합니다.",
                   "I agree to the collection and use of my information for diagnosis consultation only; it is discarded afterward."),
 "esco.f.submit":("무료 진단 신청하기 →","Request free diagnosis →"),
 "esco.f.formnote":('급하신 경우 <a href="mailto:howintlsoft@gmail.com">howintlsoft@gmail.com</a>으로 바로 메일 주셔도 됩니다.',
                    'In urgent cases, email us at <a href="mailto:howintlsoft@gmail.com">howintlsoft@gmail.com</a>.'),
 "esco.done.tag":("접수 완료","Received"),
 "esco.done.h":("진단 신청이 접수되었습니다.","Your diagnosis request has been received."),
 "esco.done.p":("담당자가 1~2영업일 안에 연락드립니다. 시설 유형에 맞는 제안서도 함께 보내드립니다. 빠른 진행을 원하시면 최근 1년분 전기요금 고지서를 준비해 주세요.",
                "We'll contact you within 1–2 business days and send a proposal matched to your facility. To move faster, please have the last 12 months of electricity bills ready."),
 "esco.done.reset":("새 신청 작성하기","Start a new request"),
}

PAGES = {
    "business":"business.html","portfolio":"portfolio.html","esco":"esco.html","about":"about.html",
    "news":"news.html","library":"library.html","quote":"quote.html",
}
VER = "0"

# ---------------------------------------------------------------- i18n helpers
def w(key, html=False):
    a = 'data-i18n="%s"' % key
    if html: a += ' data-i18n-html'
    return a, T[key][0]

def S(key, cls=None, tag="span", html=False):
    a, ko = w(key, html)
    c = ' class="%s"' % cls if cls else ""
    return "<%s%s %s>%s</%s>" % (tag, c, a, ko, tag)

def eyebrow(key, light=False):
    return S(key, cls="eyebrow light" if light else "eyebrow")

# ---------------------------------------------------------------- chrome
def head(title, desc, path, page, extra_ld=None, keywords=""):
    url = DOMAIN + path
    org_ld = {
      "@context":"https://schema.org","@type":"Organization",
      "name":"하우인터내셔널","alternateName":"HOW INTERNATIONAL","url":DOMAIN,
      "logo":DOMAIN+"/assets/how-logo.png","email":"howintlsoft@gmail.com",
      "address":{"@type":"PostalAddress","streetAddress":"동탄광역환승로73",
                 "addressLocality":"화성시","addressRegion":"경기도","addressCountry":"KR"},
      "taxID":"214-88-51839",
      "description":"디지털미디어·헬스케어·유통·에너지(ESCO) 네 사업부로 검증된 결과를 만드는 회사."
    }
    ld = '<script type="application/ld+json">%s</script>' % json.dumps(org_ld, ensure_ascii=False)
    if extra_ld:
        for e in (extra_ld if isinstance(extra_ld, list) else [extra_ld]):
            ld += '\n<script type="application/ld+json">%s</script>' % e
    kw_tag = '<meta name="keywords" content="%s">\n' % keywords if keywords else ""
    return """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{kw_tag}<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ko" href="{url}">
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Gowun+Batang:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={ver}">
{ld}
</head>
<body data-page="{page}">
""".format(title=title, desc=desc, url=url, kw_tag=kw_tag, domain=DOMAIN, ld=ld, page=page, ver=VER)

def breadcrumb_ld(crumbs):
    return json.dumps({
        "@context":"https://schema.org","@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":i+1,"name":n,"item":DOMAIN+"/"+u}
            for i,(n,u) in enumerate(crumbs)
        ]
    }, ensure_ascii=False)

def header(active=""):
    def nav(key, page):
        a, ko = w(key)
        return '<a %s data-nav="%s" href="%s">%s</a>' % (a, page, PAGES[page], ko)
    c_a, c_ko = w("cta.header")
    menu = "".join([
        nav("nav.business","business"),
        nav("nav.portfolio","portfolio"),
        nav("nav.esco","esco"),
        nav("nav.about","about"),
        nav("nav.news","news"),
        nav("nav.library","library"),
    ])
    return """<div class="topstrip">
  <div class="wrap">
    <span class="ts-main">HOW INTERNATIONAL<span class="ts-sub"> — 디지털미디어 × 헬스케어 × 유통 × 에너지</span></span>
    <span class="loc">Hwaseong · Republic of Korea</span>
  </div>
</div>
<header class="site">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="하우인터내셔널 홈">
      <img src="assets/how-logo.png" alt="HOW International" width="120" height="24">
      <span class="lbl">Global Distribution · Energy<br>Healthcare · Digital Media</span>
    </a>
    <button class="burger" aria-label="메뉴 열기" aria-expanded="false"><span></span></button>
    <nav class="menu" aria-label="주요 메뉴">
      {menu}
    </nav>
    <div class="navr">
      <div class="lang" role="group" aria-label="언어 / Language">
        <button data-lang="en">EN</button><span>·</span><button data-lang="ko" class="on">KO</button>
      </div>
      <a class="btn blue" {c_a} href="quote.html">{c_ko}</a>
    </div>
  </div>
</header>
""".format(menu=menu, c_a=c_a, c_ko=c_ko)

def footer():
    def flink(key, page): a,ko = w(key); return '<a %s href="%s">%s</a>' % (a, PAGES[page], ko)
    return """<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div class="fbrand">
        <span class="flogo-badge"><img src="assets/how-logo.png" alt="HOW International"></span>
        <div class="ft">Global Distribution · Energy<br>Healthcare · Digital Media</div>
        <p class="tagline">{tag}</p>
      </div>
      <div class="fcol">
        <h5>{sitemap}</h5>
        <div class="flist">{s_biz}{s_pf}{s_esco}{s_about}{s_news}{s_quote}</div>
      </div>
      <div class="fcol">
        <h5>{brands}</h5>
        <div class="flist">
          <a href="https://biotamax.co.kr" target="_blank" rel="noopener">BiotaMax ↗</a>
          <a href="https://painfree8800.com" target="_blank" rel="noopener">Painfree 8800 ↗</a>
          <a href="https://marketshare-2e00c.web.app/" target="_blank" rel="noopener">marketshare ↗</a>
          <a href="https://koreanflow.app" target="_blank" rel="noopener">KoreanFlow ↗</a>
          <a href="https://familya.co.kr" target="_blank" rel="noopener">familya ↗</a>
        </div>
      </div>
      <div class="fcol">
        <h5>{company}</h5>
        <div class="company">
          <span {name_a}>{name_ko}</span>
          <span {biz_a}>{biz_ko}</span>
          <span {addr_a} data-i18n-html>{addr_ko}</span>
          <a href="mailto:howintlsoft@gmail.com">howintlsoft@gmail.com</a>
          <a href="https://howglobal.co.kr">howglobal.co.kr</a>
        </div>
      </div>
    </div>
    <div class="fbot">
      <span class="cc">© <span id="year">2026</span> HOW INTERNATIONAL. ALL RIGHTS RESERVED.</span>
      <span class="admin"><a {admin_a} href="admin.html">{admin_ko}</a></span>
    </div>
  </div>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/firebase-config.js"></script>
<script src="assets/i18n.js?v={ver}"></script>
<script type="module" src="assets/firebase.js"></script>
<script src="assets/app.js?v={ver}"></script>
</body></html>""".format(
        ver=VER,
        tag=S("foot.tagline"), sitemap=T["foot.sitemap"][0], brands=T["foot.brands"][0], company=T["foot.company"][0],
        s_biz=flink("nav.business","business"), s_pf=flink("nav.portfolio","portfolio"),
        s_esco=flink("nav.esco","esco"),
        s_about=flink("nav.about","about"), s_news=flink("nav.news","news"),
        s_quote=flink("foot.quote","quote"),
        name_a=w("foot.name")[0], name_ko=T["foot.name"][0],
        biz_a=w("foot.bizno")[0], biz_ko=T["foot.bizno"][0],
        addr_a=w("foot.addr",True)[0], addr_ko=T["foot.addr"][0],
        admin_a=w("foot.admin")[0], admin_ko=T["foot.admin"][0])

def subhero(crumbk, h1k, leadk, crumb_extra=""):
    crumb_html = '<a href="index.html">HOME</a> / %s' % (crumb_extra + S(crumbk) if crumb_extra else S(crumbk))
    return """<section class="subhero">
    <div class="wrap">
      <div class="crumb rv">{crumb}</div>
      <h1 class="rv d1">{h1}</h1>
      <p class="rv d2">{lead}</p>
    </div>
  </section>""".format(crumb=crumb_html, h1=S(h1k,tag="span",html=True), lead=S(leadk))

# ---------------------------------------------------------------- components
def dashlist(keys):
    return '<div class="dashlist">' + "".join(S(k) for k in keys) + '</div>'

def bullets(keys):
    return '<div class="bullets">' + "".join(S(k) for k in keys) + '</div>'

def scard(simg, tag_html, name_html, sub, p_key, link, bl=None, three=False, tag_alt=False):
    href, lkey, ext = link
    tgt = ' target="_blank" rel="noopener"' if ext else ''
    if lkey:
        link_html = '<a class="slink" href="%s"%s>%s</a>' % (href, tgt, S(lkey))
    else:
        link_html = '<a class="slink" href="%s"%s>%s ↗</a>' % (href, tgt, href.replace("https://","").rstrip("/"))
    stag_cls = "stag alt" if tag_alt else "stag"
    parts = ['<span class="%s">%s</span>' % (stag_cls, tag_html),
             '<h3>%s</h3>' % name_html]
    if sub: parts.append('<div class="ssub">%s</div>' % sub)
    parts.append('<p %s>%s</p>' % (w(p_key)[0], T[p_key][0]))
    if bl: parts.append(bullets(bl))
    parts.append(link_html)
    return ('<div class="scard rv">%s<div class="sbody">%s</div></div>'
            % (simg, "".join(parts)))

def channel_cards():
    def ch(no, tk, pk, gk, href_type):
        return ('<div class="pcard rv"><span class="pno">%s</span><h4>%s</h4>'
                '<div class="plt">%s</div><p>%s</p>'
                '<a class="go" href="quote.html?type=%s">%s</a></div>'
                % (no, S(tk), T[tk.replace("biz.","biz.")+""][0] if False else
                   ("Media Dev &amp; Quote" if "ch1" in tk else
                    ("Healthcare Inquiry" if "ch2" in tk else "Distribution Inquiry")),
                   S(pk), href_type, S(gk)))
    return """<section class="pad part">
    <div class="wrap">
      <div class="shead">
        <div>{eye}<h2 class="rv d1">{h2}</h2></div>
        <p class="note rv d2">{note}</p>
      </div>
      <div class="pcards three">
        <div class="pcard rv d1"><span class="pno">CH.01</span><h4>{ch1}</h4><div class="plt">Digital Media Inquiry</div><p>{ch1p}</p><a class="go" href="quote.html?type=media">{ch1go}</a></div>
        <div class="pcard rv d2"><span class="pno">CH.02</span><h4>{ch2}</h4><div class="plt">Healthcare Inquiry</div><p>{ch2p}</p><a class="go" href="quote.html?type=healthcare">{ch2go}</a></div>
        <div class="pcard rv d3"><span class="pno">CH.03</span><h4>{ch3}</h4><div class="plt">Distribution Inquiry</div><p>{ch3p}</p><a class="go" href="quote.html?type=distribution">{ch3go}</a></div>
      </div>
      <div class="pcta rv d3"><a class="btn blue lg" href="quote.html">{cta}</a></div>
    </div>
  </section>""".format(
        eye=eyebrow("part.eye"), h2=S("part.h2",html=True), note=S("part.note"),
        ch1=S("biz.ch1"), ch1p=S("biz.ch1.p"), ch1go=S("biz.ch1.go"),
        ch2=S("biz.ch2"), ch2p=S("biz.ch2.p"), ch2go=S("biz.ch2.go"),
        ch3=S("biz.ch3"), ch3p=S("biz.ch3.p"), ch3go=S("biz.ch3.go"),
        cta=S("part.cta"))

# ---------------------------------------------------------------- pages
def home():
    hero = """<section class="hero">
    <div class="heromap"></div>
    <div class="heroveil"></div>
    <div class="wrap">
      <div class="inner">
        {eye}
        <h1 class="rv d1">{h1}</h1>
        <p class="lead rv d2">{lead}</p>
        <div class="cta rv d3">
          <a class="btn blue" href="business.html">{cta1}</a>
          <a class="btn ghost" href="quote.html">{cta2}</a>
        </div>
        <div class="legend rv d4">
          <span><span class="dot w"></span>{hq}</span>
          <span><span class="dot v2"></span>{origin}</span>
          <span><span class="dot v3"></span>{reach}</span>
        </div>
      </div>
    </div>
  </section>""".format(
        eye=S("home.eyebrow",cls="eyebrow light rv"), h1=S("home.h1",html=True), lead=S("home.lead"),
        cta1=S("home.cta1"), cta2=S("home.cta2"),
        hq=S("legend.hq"), origin=S("legend.origin"), reach=S("legend.reach"))

    overview = """<section class="pad">
    <div class="wrap">
      <div class="shead">
        <div>{eye}<h2 class="rv d1">{h2}</h2></div>
        <p class="note rv d2">{note}</p>
      </div>
      <div class="ovgrid four">
        <div class="ovcard rv d1">
          <span class="no">{d1no}</span>
          <h3>{d1t}</h3><div class="lt">{d1lt}</div>
          <p>{d1p}</p>
          {d1list}
          <a class="golink" href="portfolio.html">{d1go}</a>
        </div>
        <div class="ovcard rv d2">
          <span class="no">{d2no}</span>
          <h3>{d2t}</h3><div class="lt">{d2lt}</div>
          <p>{d2p}</p>
          {d2list}
          <a class="golink" href="business.html">{d2go}</a>
        </div>
        <div class="ovcard rv d3">
          <span class="no">{d3no}</span>
          <h3>{d3t}</h3><div class="lt">{d3lt}</div>
          <p>{d3p}</p>
          {d3list}
          <a class="golink" href="business.html">{d3go}</a>
        </div>
        <div class="ovcard rv d4">
          <span class="no">{d4no}</span>
          <h3>{d4t}</h3><div class="lt">{d4lt}</div>
          <p>{d4p}</p>
          {d4list}
          <a class="golink" href="esco.html">{d4go}</a>
        </div>
      </div>
    </div>
  </section>""".format(
        eye=eyebrow("ov.eye"), h2=S("ov.h2",html=True), note=S("ov.note"),
        d1no=S("ov.d1.no"), d1t=S("ov.d1.t"), d1lt=S("ov.d1.lt"),
        d1p=S("ov.d1.p"), d1list=dashlist(["ov.d1.li1","ov.d1.li2"]), d1go=S("ov.d1.go"),
        d2no=S("ov.d2.no"), d2t=S("ov.d2.t"), d2lt=S("ov.d2.lt"),
        d2p=S("ov.d2.p"), d2list=dashlist(["ov.d2.li1"]), d2go=S("ov.d2.go"),
        d3no=S("ov.d3.no"), d3t=S("ov.d3.t"), d3lt=S("ov.d3.lt"),
        d3p=S("ov.d3.p"), d3list=dashlist(["ov.d3.li1"]), d3go=S("ov.d3.go"),
        d4no=S("ov.d4.no"), d4t=S("ov.d4.t"), d4lt=S("ov.d4.lt"),
        d4p=S("ov.d4.p"), d4list=dashlist(["ov.d4.li1"]), d4go=S("ov.d4.go"))

    standards = """<section class="pad s96 standards">
    <div class="wrap">
      <div class="shead">
        <div>{eye}<h2 class="rv d1">{h2}</h2></div>
        <p class="note light rv d2">{note}</p>
      </div>
      <div class="stdgrid">
        <div class="stdcard rv d1"><span class="vn">V.01</span><h4>{v1t}</h4><p>{v1p}</p></div>
        <div class="stdcard rv d2"><span class="vn">V.02</span><h4>{v2t}</h4><p>{v2p}</p></div>
        <div class="stdcard rv d3"><span class="vn">V.03</span><h4>{v3t}</h4><p>{v3p}</p></div>
      </div>
    </div>
  </section>""".format(
        eye=eyebrow("std.eye",light=True), h2=S("std.h2",html=True), note=S("std.note"),
        v1t=S("std.v1.t"), v1p=S("std.v1.p"),
        v2t=S("std.v2.t"), v2p=S("std.v2.p"),
        v3t=S("std.v3.t"), v3p=S("std.v3.p"))

    cta_section = """<section class="pad part">
    <div class="wrap">
      <div class="shead">
        <div>{eye}<h2 class="rv d1">{h2}</h2></div>
        <p class="note rv d2">{note}</p>
      </div>
      <div class="pcta rv"><a class="btn blue lg" href="quote.html">{cta}</a></div>
    </div>
  </section>""".format(
        eye=eyebrow("part.eye"), h2=S("part.h2",html=True), note=S("part.note"),
        cta=S("part.cta"))

    seo_row = '<div class="seo-kw wrap">#웹사이트개발 #웹사이트제작 #홈페이지제작 #앱개발 #플랫폼개발 #디지털미디어사업부 #헬스케어사업부 #유통사업부 #견적상담</div>'

    body = header("home") + "<main>" + hero + overview + standards + cta_section + "</main>" + seo_row
    local_biz = json.dumps({
        "@context":"https://schema.org","@type":"LocalBusiness",
        "name":"하우인터내셔널","alternateName":"HOW INTERNATIONAL",
        "url":DOMAIN,"logo":DOMAIN+"/assets/how-logo.png",
        "image":DOMAIN+"/assets/og-cover.png","email":"howintlsoft@gmail.com",
        "address":{"@type":"PostalAddress","streetAddress":"동탄광역환승로73",
                   "addressLocality":"화성시","addressRegion":"경기도","addressCountry":"KR"},
        "taxID":"214-88-51839",
        "description":"디지털미디어·헬스케어·유통·에너지(ESCO) 네 사업부로 검증된 결과를 만드는 회사."
    }, ensure_ascii=False)
    website = json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"하우인터내셔널","url":DOMAIN}, ensure_ascii=False)
    return head(
        "하우인터내셔널 — 유통 · 헬스케어 · 디지털미디어 · 에너지(ESCO)",
        "하우인터내셔널은 디지털미디어(웹사이트개발·앱개발), 헬스케어 의료기기, 유통, 에너지(조명 ESCO) 네 사업부로 검증된 결과를 만드는 회사입니다.",
        "/index.html","home",
        extra_ld=[website, local_biz],
        keywords="하우인터내셔널,웹사이트개발,웹사이트제작,홈페이지제작,앱개발,플랫폼개발,디지털미디어사업부,헬스케어사업부,유통사업부,에너지사업부,ESCO,조명ESCO,견적상담"
    ) + body + footer()

def business():
    # DIV.01 — 디지털미디어
    ms_img = '<div class="simg sm ms"><img src="https://marketshare-2e00c.web.app/images/redesign/store-featured.png" alt="marketshare" loading="lazy"></div>'
    kf_img = '<div class="simg sm kf"><img src="https://koreanflow.app/og-image.png" alt="KoreanFlow" loading="lazy"></div>'
    fa_img = '<div class="simg sm familya"><span class="ph">familya</span></div>'
    media_cards = (
        scard(ms_img, S("ms.tag"), "marketshare", T["ms.sub"][0], "ms.dp",
              ("https://marketshare-2e00c.web.app/","ms.link",True), bl=["ms.li1","ms.li2"], three=True)
        + scard(kf_img, S("kf.tag"), "KoreanFlow", T["kf.sub"][0], "kf.dp",
                ("https://koreanflow.app",None,True), bl=["kf.li1","kf.li2"], three=True)
        + scard(fa_img, S("fa.tag"), S("fa.name"), T["fa.sub"][0], "fa.dp",
                ("https://familya.co.kr",None,True), bl=["fa.li1","fa.li2"], three=True))

    portfolio_cta = """<div class="portfolio-cta rv">
      <div>
        <div class="ptag">외주 개발 프로젝트 포함</div>
        <p>자체 플랫폼뿐 아니라 고객사를 위해 수행한 개발 프로젝트도 포트폴리오에서 확인할 수 있습니다.</p>
      </div>
      <a class="btn blue" href="portfolio.html">포트폴리오 전체보기 →</a>
    </div>"""

    # DIV.02 — 헬스케어
    pf_img = '<div class="simg tall dark contain"><img src="https://painfree8800.com/images/product/painfree-s8800-main.png" alt="Painfree 8800" loading="lazy"></div>'
    health_cards = scard(pf_img, S("pf.tag"), "Painfree 8800", T["pf.sub"][0], "pf.dp",
                         ("https://painfree8800.com","link.site",True), bl=["pf.li1","pf.li2","pf.li3"])

    # DIV.03 — 유통
    bio_img = '<div class="simg tall biotamax contain"><img src="assets/biotamax.jpg" alt="BiotaMax 바이오타맥스 토양생균제" loading="lazy"></div>'
    dist_cards = scard(bio_img, S("bio.tag"), 'BiotaMax <small>바이오타맥스</small>',
                       T["bio.sub"][0], "bio.dp",
                       ("https://biotamax.co.kr","link.site",True), bl=["bio.li1","bio.li2","bio.li3"], tag_alt=True)

    body = header("business") + subhero("biz.crumb","biz.h1","biz.lead")
    body += """<section class="pad s96">
    <div class="wrap sectlabel">
      {d1eye}
      <h2 class="rv small">{d1h2}</h2>
      <p class="sublead rv">{d1lead}</p>
      <div class="scards three">{media}</div>
      {pf_cta}
    </div>
  </section>
  <section class="pad s96" data-bg="mist">
    <div class="wrap sectlabel">
      {d2eye}
      <h2 class="rv small">{d2h2}</h2>
      <p class="sublead rv">{d2lead}</p>
      <div class="scards">{health}</div>
    </div>
  </section>
  <section class="pad s96" data-bg="line">
    <div class="wrap sectlabel">
      {d3eye}
      <h2 class="rv small">{d3h2}</h2>
      <p class="sublead rv">{d3lead}</p>
      <div class="scards">{dist}</div>
    </div>
  </section>
  <section class="pad s96" data-bg="mist">
    <div class="wrap sectlabel">
      {d4eye}
      <h2 class="rv small">{d4h2}</h2>
      <p class="sublead rv">{d4lead}</p>
      <div class="biz-d4-cta rv">
        <a class="btn blue" href="esco.html">{d4go1}</a>
        <a class="btn ghost" href="esco.html#apply">{d4go2}</a>
      </div>
    </div>
  </section>
  {channels}
  <div class="seo-kw wrap">#사업분야 #유통사업부 #헬스케어사업부 #디지털미디어사업부 #에너지사업부 #ESCO #조명ESCO #웹사이트개발 #앱개발</div>""".format(
        d1eye=S("biz.d1.eye",cls="eyebrow rv"), d1h2=S("biz.d1.h2",html=True), d1lead=S("biz.d1.lead"),
        media=media_cards, pf_cta=portfolio_cta,
        d2eye=S("biz.d2.eye",cls="eyebrow rv"), d2h2=S("biz.d2.h2",html=True), d2lead=S("biz.d2.lead"),
        health=health_cards,
        d3eye=S("biz.d3.eye",cls="eyebrow rv"), d3h2=S("biz.d3.h2",html=True), d3lead=S("biz.d3.lead"),
        dist=dist_cards,
        d4eye=S("biz.d4.eye",cls="eyebrow rv"), d4h2=S("biz.d4.h2",html=True), d4lead=S("biz.d4.lead"),
        d4go1=S("biz.d4.go1"), d4go2=S("biz.d4.go2"),
        channels=channel_cards())
    biz_items = json.dumps({
        "@context":"https://schema.org","@type":"ItemList",
        "name":"하우인터내셔널 사업분야","url":DOMAIN+"/business.html",
        "itemListElement":[
            {"@type":"ListItem","position":1,"item":{"@type":"Service","name":"디지털미디어사업부","description":"웹사이트·앱 플랫폼 개발 및 자체 플랫폼 운영","provider":{"@type":"Organization","name":"하우인터내셔널"}}},
            {"@type":"ListItem","position":2,"item":{"@type":"Service","name":"헬스케어사업부","description":"KFDA 허가 의료기기 Painfree 8800 공급","provider":{"@type":"Organization","name":"하우인터내셔널"}}},
            {"@type":"ListItem","position":3,"item":{"@type":"Service","name":"유통사업부","description":"바이오타맥스(BiotaMax) 토양생균제 국내 총판","provider":{"@type":"Organization","name":"하우인터내셔널"}}},
            {"@type":"ListItem","position":4,"item":{"@type":"Service","name":"에너지사업부","description":"초기비용 0원 조명 ESCO — 노후 조명을 3세대 스마트 AI LED로 교체, 절감액으로 상환","provider":{"@type":"Organization","name":"하우인터내셔널"}}}
        ]
    }, ensure_ascii=False)
    return head(
        "사업분야 — 유통 · 헬스케어 · 디지털미디어 · 에너지(ESCO) | 하우인터내셔널",
        "하우인터내셔널의 유통사업부(바이오타맥스), 헬스케어사업부(Painfree 8800), 디지털미디어사업부(웹사이트개발·앱개발), 에너지사업부(조명 ESCO)를 소개합니다.",
        "/business.html","business",
        extra_ld=[breadcrumb_ld([("홈","index.html"),("사업분야","business.html")]), biz_items],
        keywords="사업분야,유통사업부,헬스케어사업부,디지털미디어사업부,에너지사업부,ESCO,조명ESCO,웹사이트개발,앱개발,바이오타맥스,Painfree8800"
    ) + body + footer()

def portfolio():
    own_platforms = """<section class="pad s96">
    <div class="wrap">
      {eye}
      <h2 class="rv pf-h2">{h2}</h2>
      <div class="scards three">
        <a class="scard pf-card rv d1" href="https://marketshare-2e00c.web.app/" target="_blank" rel="noopener">
          <div class="simg sm ms"><img src="https://marketshare-2e00c.web.app/images/redesign/store-featured.png" alt="marketshare" loading="lazy"></div>
          <div class="sbody">
            <span class="stag">PropTech</span>
            <h3>marketshare</h3>
            <div class="ssub">분양몰 솔루션</div>
            <p {p_ms}>상가를 분양받듯 온라인 점포 한 칸을 분양받는 커머스 솔루션.</p>
            <div class="slink">플랫폼 보기 ↗</div>
          </div>
        </a>
        <a class="scard pf-card rv d2" href="https://koreanflow.app" target="_blank" rel="noopener">
          <div class="simg sm kf"><img src="https://koreanflow.app/og-image.png" alt="KoreanFlow" loading="lazy"></div>
          <div class="sbody">
            <span class="stag">EdTech</span>
            <h3>KoreanFlow</h3>
            <div class="ssub">한국어 학습 플랫폼</div>
            <p {p_kf}>AI 레슨·발음 훈련·게임형 학습을 전 세계 학습자에게 제공합니다.</p>
            <div class="slink">koreanflow.app ↗</div>
          </div>
        </a>
        <a class="scard pf-card rv d3" href="https://familya.co.kr" target="_blank" rel="noopener">
          <div class="simg sm familya"><span class="ph">familya</span></div>
          <div class="sbody">
            <span class="stag">Family</span>
            <h3>{fa_name}</h3>
            <div class="ssub">디지털 족보 플랫폼</div>
            <p {p_fa}>가계도·연대기·사진첩과 자동 생성 연감으로 가족의 일상을 엮습니다.</p>
            <div class="slink">familya.co.kr ↗</div>
          </div>
        </a>
      </div>
    </div>
  </section>""".format(
        eye=eyebrow("pf_page.own.eye"),
        h2=S("pf_page.own.h2"),
        fa_name=S("fa.name"),
        p_ms=w("ms.dp")[0], p_kf=w("kf.dp")[0], p_fa=w("fa.dp")[0])

    clients = [
        ("엘로힘바이오","elohimbio.com","https://elohimbio.com","#1F5D46","client-elohimbio.png"),
        ("제라바이오","zerabio.com","https://zerabio.com","#2A5FA8","client-zerabio.png"),
        ("글로벌그룹코리아","globalgroupkorea.com","https://globalgroupkorea.com","#0A0C14","client-globalgroupkorea.png"),
        ("교회학교 아동부 강남협의회","pckgangnam.org","https://pckgangnam.org","#0170B9","client-pckgangnam.png"),
        ("기독교식작명사이트","blessedname.net","https://blessedname.net","#b8333a","client-blessedname.png"),
        ("두릅음나무재배기술","greenroot-pwa.web.app","https://greenroot-pwa.web.app/","#2f7a3f","client-duroop.png"),
        ("스칼리온홀딩스","allcare365.net","https://allcare365.net/","#0000FF","client-allcare365.png"),
    ]
    client_cards = "".join(
        '<a class="pf-client-card" href="%s" target="_blank" rel="noopener">'
        '<div class="pf-thumb" style="background:%s"><img src="assets/%s" alt="%s" loading="lazy"></div>'
        '<div class="pf-client-body"><span class="pf-domain">%s ↗</span></div>'
        '</a>' % (href, bg, img, name, domain)
        for name, domain, href, bg, img in clients)

    client_section = """<section class="pad s96" data-bg="mist">
    <div class="wrap">
      {eye}
      <h2 class="rv pf-h2">{h2}</h2>
      <p class="rv sublead">{lead}</p>
      <div class="pf-client-grid">{cards}</div>
    </div>
  </section>""".format(
        eye=eyebrow("pf_page.client.eye"),
        h2=S("pf_page.client.h2"), lead=S("pf_page.client.lead"),
        cards=client_cards)

    cta_section = """<section class="pad s96" style="text-align:center">
    <div class="wrap">
      <h2 class="rv pf-cta-h2">{h2}</h2>
      <p class="rv" style="font-size:1rem;color:var(--muted);margin:0 0 32px;line-height:1.7">{p}</p>
      <a class="btn blue lg rv" href="quote.html">{btn}</a>
    </div>
  </section>""".format(
        h2=S("pf_page.cta.h2",html=True), p=S("pf_page.cta.p"), btn=S("pf_page.cta.btn"))

    seo_row = '<div class="seo-kw wrap">#웹사이트개발 #웹사이트제작 #홈페이지제작 #앱개발 #모바일앱개발 #플랫폼개발 #외주개발 #포트폴리오</div>'

    crumb = '<a href="index.html">HOME</a> / <a href="business.html">%s</a> / %s' % (
        T["biz.crumb"][0], S("pf_page.crumb"))
    subhero_html = """<section class="subhero">
    <div class="wrap">
      <div class="crumb rv">{crumb}</div>
      <span class="eyebrow light rv" style="margin-bottom:18px">DIV. 01 · 디지털미디어사업부</span>
      <h1 class="rv d1">{h1}</h1>
      <p class="rv d2">{lead}</p>
    </div>
  </section>""".format(crumb=crumb, h1=S("pf_page.h1",tag="span",html=True), lead=S("pf_page.lead"))

    body = header("portfolio") + subhero_html + own_platforms + client_section + cta_section + seo_row
    pf_items = json.dumps({
        "@context":"https://schema.org","@type":"ItemList",
        "name":"하우인터내셔널 디지털미디어 개발 포트폴리오","url":DOMAIN+"/portfolio.html",
        "itemListElement":[
            {"@type":"ListItem","position":1,"item":{"@type":"SoftwareApplication","name":"marketshare","url":"https://marketshare-2e00c.web.app/","description":"분양몰 솔루션"}},
            {"@type":"ListItem","position":2,"item":{"@type":"SoftwareApplication","name":"KoreanFlow","url":"https://koreanflow.app","description":"한국어 학습 플랫폼"}},
            {"@type":"ListItem","position":3,"item":{"@type":"SoftwareApplication","name":"우리家 이야기","url":"https://familya.co.kr","description":"디지털 족보 플랫폼"}},
            {"@type":"ListItem","position":4,"item":{"@type":"WebSite","name":"엘로힘바이오","url":"https://elohimbio.com"}},
            {"@type":"ListItem","position":5,"item":{"@type":"WebSite","name":"제라바이오","url":"https://zerabio.com"}},
            {"@type":"ListItem","position":6,"item":{"@type":"WebSite","name":"글로벌그룹코리아","url":"https://globalgroupkorea.com"}},
            {"@type":"ListItem","position":7,"item":{"@type":"WebSite","name":"교회학교 아동부 강남협의회","url":"https://pckgangnam.org"}},
            {"@type":"ListItem","position":8,"item":{"@type":"WebSite","name":"기독교식작명","url":"https://blessedname.net"}},
            {"@type":"ListItem","position":9,"item":{"@type":"WebSite","name":"두릅음나무재배기술","url":"https://greenroot-pwa.web.app/"}},
            {"@type":"ListItem","position":10,"item":{"@type":"WebSite","name":"스칼리온홀딩스","url":"https://allcare365.net/"}}
        ]
    }, ensure_ascii=False)
    return head(
        "포트폴리오 — 디지털미디어사업부 | 하우인터내셔널",
        "하우인터내셔널 디지털미디어사업부의 웹사이트개발·앱개발 포트폴리오. 자체 플랫폼과 외주 개발 프로젝트 사례를 확인하세요.",
        "/portfolio.html","portfolio",
        extra_ld=[breadcrumb_ld([("홈","index.html"),("사업분야","business.html"),("포트폴리오","portfolio.html")]), pf_items],
        keywords="웹사이트개발,웹사이트제작,홈페이지제작,앱개발,플랫폼개발,외주개발,포트폴리오,디지털미디어사업부,하우인터내셔널"
    ) + body + footer()

def quote():
    form_html = """<form id="quote-form" class="rv" novalidate>
          <div class="field">
            <label>{type_lbl} <span class="req">*</span></label>
            <div class="seg">
              <label class="qtype-card" data-type="distribution"><input type="radio" name="qtype" value="distribution"> {t_dist}</label>
              <label class="qtype-card" data-type="healthcare"><input type="radio" name="qtype" value="healthcare"> {t_health}</label>
              <label class="qtype-card active" data-type="media"><input type="radio" name="qtype" value="media" checked> {t_media}</label>
              <label class="qtype-card" data-type="esco"><input type="radio" name="qtype" value="esco"> {t_esco}</label>
              <label class="qtype-card" data-type="other"><input type="radio" name="qtype" value="other"> {t_other}</label>
            </div>
            <div class="qesco-note" id="qesco-note" style="display:none">
              <p {en_a}>{esco_note}</p>
              <a class="go" href="esco.html#apply">{esco_go}</a>
            </div>
          </div>
          <div class="quote-fields" id="quote-fields">
            <div class="quote-block">
              <div class="qlabel">{ql}</div>
              <div class="two">
                <div class="field">
                  <label>{budget_l}</label>
                  <select name="budget">
                    <option>미정 / 상담 후 결정</option>
                    <option>500만원 이하</option>
                    <option>500~1,500만원</option>
                    <option>1,500~5,000만원</option>
                    <option>5,000만원 이상</option>
                  </select>
                </div>
                <div class="field">
                  <label>{projtype_l}</label>
                  <select name="projtype">
                    <option>신규 개발</option>
                    <option>기존 서비스 고도화</option>
                    <option>유지보수 / 운영</option>
                  </select>
                </div>
              </div>
              <div class="two">
                <div class="field">
                  <label>{sched_l}</label>
                  <input type="text" name="schedule" {sched_ph}>
                </div>
                <div class="field">
                  <label>{ref_l}</label>
                  <input type="text" name="ref" {ref_ph}>
                </div>
              </div>
            </div>
          </div>
          <div class="two">
            <div class="field"><label>{company_l}</label><input name="company" {company_ph}></div>
            <div class="field"><label>{name_l} <span class="req">*</span></label><input name="name" required {name_ph}></div>
          </div>
          <div class="two">
            <div class="field"><label>{email_l} <span class="req">*</span></label><input name="email" type="email" required {email_ph}></div>
            <div class="field"><label>{phone_l}</label><input name="phone" {phone_ph}></div>
          </div>
          <div class="field"><label>{msg_l} <span class="req">*</span></label><textarea name="message" required {msg_ph}></textarea></div>
          <label class="consent"><input type="checkbox" name="consent" required> {consent}</label>
          <button class="btn blue lg" type="submit">{submit}</button>
          <p class="formnote" {fn_a} data-i18n-html>{fn}</p>
        </form>""".format(
        type_lbl=S("qt.type.label"), t_dist=S("qt.type.dist"), t_health=S("qt.type.health"),
        t_media=S("qt.type.media"), t_esco=S("qt.type.esco"), t_other=S("qt.type.other"),
        en_a=w("qt.esco.note")[0], esco_note=T["qt.esco.note"][0], esco_go=S("qt.esco.go"),
        ql=S("qt.quote.label"),
        budget_l=S("qt.budget"), projtype_l=S("qt.projtype"),
        sched_l=S("qt.schedule"), sched_ph='data-i18n-ph="qt.schedule.ph" placeholder="%s"' % T["qt.schedule.ph"][0],
        ref_l=S("qt.ref"), ref_ph='data-i18n-ph="qt.ref.ph" placeholder="%s"' % T["qt.ref.ph"][0],
        company_l=S("qt.company"), company_ph='data-i18n-ph="qt.company.ph" placeholder="%s"' % T["qt.company.ph"][0],
        name_l=S("qt.name"), name_ph='data-i18n-ph="qt.name.ph" placeholder="%s"' % T["qt.name.ph"][0],
        email_l=S("qt.email"), email_ph='data-i18n-ph="qt.email.ph" placeholder="%s"' % T["qt.email.ph"][0],
        phone_l=S("qt.phone"), phone_ph='data-i18n-ph="qt.phone.ph" placeholder="%s"' % T["qt.phone.ph"][0],
        msg_l=S("qt.msg"), msg_ph='data-i18n-ph="qt.msg.ph" placeholder="%s"' % T["qt.msg.ph"][0],
        consent=S("qt.consent"), submit=S("qt.submit"),
        fn_a=w("qt.formnote",True)[0], fn=T["qt.formnote"][0])

    aside_html = """<div class="aside-card rv d1">
          <h4>{ah}</h4>
          <div class="info">
            <div><dt>유통</dt><dd>{a_dist}</dd></div>
            <div><dt>헬스케어</dt><dd>{a_health}</dd></div>
            <div><dt>미디어</dt><dd>{a_media}</dd></div>
          </div>
          <div class="resp">
            <div class="rl">{rl}</div>
            <p>{rp}</p>
          </div>
        </div>""".format(
        ah=S("qt.aside.h"),
        a_dist=S("qt.aside.dist"), a_health=S("qt.aside.health"), a_media=S("qt.aside.media"),
        rl=S("qt.resp.l"), rp=S("qt.resp.p"))

    body = header("quote") + subhero("qt.crumb","qt.h1","qt.lead")
    body += """<section class="pad s96">
    <div class="wrap">
      <div class="contact-grid">
        <div id="quote-success" class="quote-success" style="display:none">
          <div class="success-tag">접수 완료</div>
          <h2>문의가 접수되었습니다.</h2>
          <p>담당자가 확인 후 1~2영업일 내 회신드립니다.</p>
          <button class="btn" id="quote-reset">새 문의 작성하기</button>
        </div>
        {form}
        {aside}
      </div>
    </div>
  </section>
  <div class="seo-kw wrap">#웹사이트개발견적 #앱개발견적 #홈페이지제작문의 #견적상담 #협력문의</div>""".format(
        form=form_html, aside=aside_html)
    contact_ld = json.dumps({
        "@context":"https://schema.org","@type":"ContactPage",
        "name":"견적 상담 / 협력 문의","url":DOMAIN+"/quote.html",
        "description":"웹사이트개발·앱개발 견적 상담, 유통·헬스케어 제휴 문의"
    }, ensure_ascii=False)
    return head(
        "견적 상담 / 협력 문의 | 하우인터내셔널",
        "웹사이트개발·앱개발 견적 상담부터 유통·헬스케어 제휴 문의까지, 하우인터내셔널에 온라인으로 바로 문의하세요.",
        "/quote.html","quote",
        extra_ld=[breadcrumb_ld([("홈","index.html"),("견적 상담","quote.html")]), contact_ld],
        keywords="웹사이트개발 견적,앱개발 견적,홈페이지제작 문의,견적상담,협력문의,하우인터내셔널"
    ) + body + footer()

def about():
    def val(no, tk, pk):
        return '<div class="v"><span class="vn">V.0%s</span><h5>%s</h5><p>%s</p></div>' % (no, S(tk), S(pk))
    def inforow(labelk, val_html):
        return '<div><dt>%s</dt><dd>%s</dd></div>' % (S(labelk), val_html)
    body = header("about") + subhero("about.crumb","about.h1","about.lead")
    body += """<section class="pad s96">
    <div class="wrap">
      <div class="cols">
        <div>{eye}<p class="big rv d1">{big}</p></div>
        <div class="prose rv d2"><p {p1a}>{p1}</p><p {p2a}>{p2}</p><p {p3a}>{p3}</p></div>
      </div>
    </div>
  </section>
  <section class="pad" data-bg="mist" style="padding-top:88px;padding-bottom:88px">
    <div class="wrap">
      {eye2}
      <div class="valuegrid rv d1">{v1}{v2}{v3}</div>
    </div>
  </section>
  <section class="pad s96">
    <div class="wrap">
      {eye3}
      <dl class="info rv d1">{rows}</dl>
    </div>
  </section>
  <section style="padding:0 0 104px">
    <div class="wrap" style="display:flex;justify-content:center">
      <a class="btn blue lg" href="quote.html">{cta}</a>
    </div>
  </section>
  <div class="seo-kw wrap">#하우인터내셔널 #회사소개 #웹사이트개발 #앱개발 #디지털미디어사업부 #헬스케어사업부 #유통사업부</div>""".format(
        eye=eyebrow("about.who.eye"), big=S("about.who.big"),
        p1a=w("about.p1")[0], p1=T["about.p1"][0],
        p2a=w("about.p2")[0], p2=T["about.p2"][0],
        p3a=w("about.p3")[0], p3=T["about.p3"][0],
        eye2=S("about.work.eye",cls="eyebrow rv"),
        v1=val(1,"av1.t","av1.p"), v2=val(2,"av2.t","av2.p"), v3=val(3,"av3.t","av3.p"),
        eye3=S("about.co.eye",cls="eyebrow rv"),
        rows="".join([
            inforow("info.name","HOW INTERNATIONAL · 하우인터내셔널"),
            inforow("info.biz", S("info.biz.v")),
            inforow("info.reg","214-88-51839"),
            inforow("info.addr", S("info.addr.v")),
            inforow("info.email",'<a href="mailto:howintlsoft@gmail.com">howintlsoft@gmail.com</a>'),
            inforow("info.web",'<a href="https://howglobal.co.kr">howglobal.co.kr</a>'),
        ]),
        cta=S("about.cta.btn"))
    about_org = json.dumps({
        "@context":"https://schema.org","@type":"Organization",
        "name":"하우인터내셔널","alternateName":"HOW INTERNATIONAL",
        "url":DOMAIN,"email":"howintlsoft@gmail.com","taxID":"214-88-51839",
        "address":{"@type":"PostalAddress","streetAddress":"동탄광역환승로73",
                   "addressLocality":"화성시","addressRegion":"경기도","addressCountry":"KR"},
        "foundingLocation":{"@type":"Place","name":"화성시, 경기도, 대한민국"},
        "knowsAbout":["디지털미디어","웹사이트개발","앱개발","헬스케어","의료기기","유통","토양생균제","에너지효율화","ESCO","조명 ESCO","LED 교체사업"]
    }, ensure_ascii=False)
    return head(
        "회사소개 | 하우인터내셔널",
        "검증된 제품을 유통하고, 건강을 지키고, 웹사이트개발·앱개발 플랫폼을 직접 만드는 하우인터내셔널을 소개합니다.",
        "/about.html","about",
        extra_ld=[breadcrumb_ld([("홈","index.html"),("회사소개","about.html")]), about_org],
        keywords="하우인터내셔널,회사소개,웹사이트개발,앱개발,디지털미디어사업부,헬스케어사업부,유통사업부"
    ) + body + footer()

def listpage(kind):
    crumb,h1,lead = (("news.crumb","news.h1","news.lead") if kind=="news" else ("lib.crumb","lib.h1","lib.lead"))
    hostid = "news-list" if kind=="news" else "library-list"
    title = "뉴스 — 하우인터내셔널" if kind=="news" else "자료실 — 하우인터내셔널"
    desc = "하우인터내셔널의 새로운 소식과 보도자료." if kind=="news" else "하우인터내셔널 회사소개서·제품 카탈로그·브로슈어 다운로드."
    path = "/news.html" if kind=="news" else "/library.html"
    page = "news" if kind=="news" else "library"
    body = header(page) + subhero(crumb,h1,lead)
    body += """<section class="pad s96"><div class="wrap">
      <div id="{hid}" class="rv"><div class="empty"><span class="mono">LOADING</span><p>불러오는 중…</p></div></div>
    </div></section>""".format(hid=hostid)
    kw = ("하우인터내셔널뉴스,보도자료,디지털미디어뉴스,유통뉴스,플랫폼뉴스" if kind=="news"
          else "하우인터내셔널자료,브로슈어다운로드,카탈로그,제품자료")
    crumb_name = "뉴스" if kind=="news" else "자료실"
    return head(title, desc, path, page,
        extra_ld=[breadcrumb_ld([("홈","index.html"),(crumb_name,path.lstrip("/"))])],
        keywords=kw) + body + footer()

# ---------------------------------------------------------------- esco page
ESCO_TARGETS = ["apartment","parking","factory","hospital","building","retail",
                "public","university","school","church","welfare"]
ESCO_SLOW = {"school","church","welfare"}
ESCO_SPEED = {"apartment":"esco.spd.fast","parking":"esco.spd.vfast","factory":"esco.spd.vfast",
              "hospital":"esco.spd.fast","building":"esco.spd.normal","retail":"esco.spd.normal",
              "public":"esco.spd.normal","university":"esco.spd.normal","school":"esco.spd.slow",
              "church":"esco.spd.slow","welfare":"esco.spd.slow"}

def esco():
    def opt(key):
        a, ko = w(key); return '<option value="%s" %s>%s</option>' % (ko, a, ko)
    def fopt(key, val):
        a, ko = w(key); return '<option value="%s" %s>%s</option>' % (val, a, ko)

    # --- hero ---
    crumb = '<a href="index.html">HOME</a> / %s' % S("esco.crumb")
    hero = """<section class="esco-hero">
    <div class="wrap">
      <div class="crumb rv">{crumb}</div>
      <span class="eyebrow light rv">{eye}</span>
      <h1 class="rv d1">{h1}</h1>
      <p class="esco-lead rv d2">{lead}</p>
      <div class="esco-kpis rv d3">
        <div class="esco-kpi"><span class="n">{k1n}</span><span class="l">{k1l}</span></div>
        <div class="esco-kpi"><span class="n">{k2n}</span><span class="l">{k2l}</span></div>
        <div class="esco-kpi"><span class="n">{k3n}</span><span class="l">{k3l}</span></div>
      </div>
      <div class="cta rv d4">
        <a class="btn blue" href="#apply">{apply}</a>
        <a class="btn ghost" href="#calc">{calc}</a>
      </div>
    </div>
  </section>""".format(
        crumb=crumb, eye=T["esco.eyebrow"][0], h1=S("esco.h1",tag="span",html=True), lead=S("esco.lead"),
        k1n=S("esco.kpi1.n"), k1l=S("esco.kpi1.l"), k2n=S("esco.kpi2.n"), k2l=S("esco.kpi2.l"),
        k3n=S("esco.kpi3.n"), k3l=S("esco.kpi3.l"),
        apply=S("esco.cta.apply"), calc=S("esco.cta.calc"))

    # --- what is esco ---
    flow = "".join('<div class="esco-step rv"><h4>%s</h4><p>%s</p></div>'
                   % (S("esco.flow%d.t"%i), S("esco.flow%d.p"%i)) for i in (1,2,3,4))
    cmp_rows = "".join('<tr><th>%s</th><td>%s</td><td class="hi">%s</td></tr>'
                       % (S("esco.cmp.r%d"%i), S("esco.cmp.r%da"%i), S("esco.cmp.r%db"%i)) for i in (1,2,3,4))
    what = """<section class="pad s96">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <p class="sublead rv">{p}</p>
      <div class="esco-flow rv">{flow}</div>
      <div class="esco-tablewrap rv">
        <table class="esco-table cmp">
          <thead><tr><th>{c0}</th><th>{c1}</th><th class="hi">{c2}</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    </div>
  </section>""".format(
        eye=S("esco.what.eye",cls="eyebrow rv"), h2=S("esco.what.h2",html=True), p=S("esco.what.p"),
        flow=flow, c0=S("esco.cmp.c0"), c1=S("esco.cmp.c1"), c2=S("esco.cmp.c2"), rows=cmp_rows)

    # --- 3rd-gen LED ---
    led_feats = "".join('<div class="esco-feat rv"><h4>%s</h4><p>%s</p></div>'
                        % (S("esco.led.f%d"%i), S("esco.led.f%dp"%i)) for i in (1,2,3))
    led = """<section class="pad s96" data-bg="mist">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <div class="esco-tablewrap rv">
        <table class="esco-table led">
          <thead><tr><th>{c0}</th><th>{c1}</th><th>{c2}</th><th class="hi">{c3}</th></tr></thead>
          <tbody>
            <tr><th>{r1}</th><td>60 lm</td><td>110 lm</td><td class="hi">{r1c}</td></tr>
            <tr><th>{r2}</th><td>{r2a}</td><td>{r2b}</td><td class="hi">{r2c}</td></tr>
            <tr><th>{r3}</th><td>{r3a}</td><td>{r3b}</td><td class="hi">{r3c}</td></tr>
            <tr><th>{r4}</th><td>{r4ab}</td><td>{r4ab2}</td><td class="hi">{r4c}</td></tr>
          </tbody>
        </table>
      </div>
      <div class="esco-feats rv">{feats}</div>
    </div>
  </section>""".format(
        eye=S("esco.led.eye",cls="eyebrow rv"), h2=S("esco.led.h2",html=True),
        c0=S("esco.led.c0"), c1=S("esco.led.c1"), c2=S("esco.led.c2"), c3=S("esco.led.c3"),
        r1=S("esco.led.r1"), r1c=S("esco.led.r1c"),
        r2=S("esco.led.r2"), r2a=S("esco.led.r2a"), r2b=S("esco.led.r2b"), r2c=S("esco.led.r2c"),
        r3=S("esco.led.r3"), r3a=S("esco.led.r3a"), r3b=S("esco.led.r3b"), r3c=S("esco.led.r3c"),
        r4=S("esco.led.r4"), r4ab=S("esco.led.r4ab"), r4ab2=S("esco.led.r4ab"), r4c=S("esco.led.r4c"),
        feats=led_feats)

    # --- targets (11 details) ---
    def target_card(k):
        slownote = ('<p class="esco-slownote">%s</p>' % S("esco.tg.slownote")) if k in ESCO_SLOW else ""
        return """<details class="esco-target rv">
          <summary><span class="et-name">{n}</span><span class="et-rate"><em>{rl}</em> {r}</span></summary>
          <div class="et-body">
            <p>{s}</p>
            <div class="et-meta"><span class="et-speed"><em>{sl}</em> {sp}</span></div>
            {slow}
            <a class="go" href="esco.html?facility={k}#apply">{btn}</a>
          </div>
        </details>""".format(
            n=S("esco.tg.%s.n"%k), rl=S("esco.tg.ratelbl"), r=S("esco.tg.%s.r"%k),
            s=S("esco.tg.%s.s"%k), sl=S("esco.tg.speedlbl"), sp=S(ESCO_SPEED[k]),
            slow=slownote, k=k, btn=S("esco.tg.btn"))
    targets = """<section class="pad s96">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <div class="esco-targets">{cards}</div>
    </div>
  </section>""".format(
        eye=S("esco.tg.eye",cls="eyebrow rv"), h2=S("esco.tg.h2",html=True),
        cards="".join(target_card(k) for k in ESCO_TARGETS))

    # --- calculator ---
    calc_fopts = "".join(fopt("esco.tg.%s.n"%k, k) for k in ESCO_TARGETS)
    calc = """<section class="pad s96" data-bg="blue" id="calc">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <div class="esco-calc rv">
        <div class="esco-calc-in">
          <div class="field">
            <label data-i18n="esco.calc.flbl">{flbl}</label>
            <select id="calc-facility">{opts}</select>
          </div>
          <div class="field">
            <label id="calc-bill-label" data-i18n="esco.calc.blbl">{blbl}</label>
            <input id="calc-bill" type="text" inputmode="numeric" data-i18n-ph="esco.calc.bph" placeholder="{bph}">
          </div>
          <button class="btn blue" id="calc-run" type="button">{btn}</button>
        </div>
        <div class="esco-calc-out" id="calc-out" style="display:none">
          <div class="esco-calc-result"><span class="pre" data-i18n="esco.calc.resultpre">{pre}</span>
            <strong id="calc-amount"></strong></div>
          <a class="btn ghost" id="calc-apply" href="#apply">{applybtn}</a>
          <p class="esco-disclaimer">{disc}</p>
        </div>
      </div>
    </div>
  </section>""".format(
        eye=S("esco.calc.eye",cls="eyebrow light rv"), h2=S("esco.calc.h2",html=True),
        flbl=T["esco.calc.flbl"][0], opts=calc_fopts,
        blbl=T["esco.calc.blbl"][0], bph=T["esco.calc.bph"][0],
        btn=S("esco.calc.btn"), pre=T["esco.calc.resultpre"][0],
        applybtn=S("esco.calc.applybtn"), disc=S("esco.calc.disclaimer"))

    # --- cases ---
    case_rows = "".join('<tr><th>%s</th><td>%s</td><td class="hi">%s</td></tr>'
                        % (S("esco.case.r%ds"%i), S("esco.case.r%dc"%i), S("esco.case.r%dr"%i)) for i in (1,2,3,4))
    cases = """<section class="pad s96">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <div class="esco-tablewrap rv">
        <table class="esco-table cases">
          <thead><tr><th>{c0}</th><th>{c1}</th><th class="hi">{c2}</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    </div>
  </section>""".format(
        eye=S("esco.case.eye",cls="eyebrow rv"), h2=S("esco.case.h2",html=True),
        c0=S("esco.case.c0"), c1=S("esco.case.c1"), c2=S("esco.case.c2"), rows=case_rows)

    # --- structure ---
    roles = "".join('<div class="esco-role rv"><h4>%s</h4><p>%s</p></div>'
                    % (S("esco.str.%s.t"%r), S("esco.str.%s.p"%r)) for r in ("user","esco","epc"))
    steps = "".join('<li class="rv">%s</li>' % S("esco.str.step%d"%i) for i in range(1,8))
    structure = """<section class="pad s96" data-bg="mist">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <div class="esco-roles">{roles}</div>
      <div class="esco-how rv"><h4>{how_t}</h4><p>{how_p}</p></div>
      <div class="esco-steps-wrap rv">
        <div class="esco-steps-label">{stepsl}</div>
        <ol class="esco-steps">{steps}</ol>
      </div>
    </div>
  </section>""".format(
        eye=S("esco.str.eye",cls="eyebrow rv"), h2=S("esco.str.h2",html=True),
        roles=roles, how_t=S("esco.str.how.t"), how_p=S("esco.str.how.p"),
        stepsl=S("esco.str.steps.l"), steps=steps)

    # --- faq ---
    faq_items = "".join("""<details class="esco-faq rv">
          <summary>{q}</summary><div class="esco-faq-a"><p>{a}</p></div>
        </details>""".format(q=S("esco.faq.q%d"%i), a=S("esco.faq.a%d"%i)) for i in range(1,8))
    faq = """<section class="pad s96" id="faq">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <div class="esco-faqs">{items}</div>
    </div>
  </section>""".format(
        eye=S("esco.faq.eye",cls="eyebrow rv"), h2=S("esco.faq.h2",html=True), items=faq_items)

    # --- apply form ---
    facility_opts = ('<option value="" disabled selected %s>%s</option>'
                     % (w("esco.f.role.0")[0], T["esco.f.role.0"][0])) \
                    + "".join(fopt("esco.tg.%s.n"%k, k) for k in ESCO_TARGETS) \
                    + fopt("esco.f.other","other")
    bill_opts = "".join(opt("esco.f.bill.%d"%i) for i in range(0,5))
    role_opts = ('<option value="" selected %s>%s</option>' % (w("esco.f.role.0")[0], T["esco.f.role.0"][0])) \
                + "".join(opt("esco.f.role.%d"%i) for i in range(1,6))
    ctime_opts = "".join(opt("esco.f.ctime.%d"%i) for i in range(0,3))
    apply_form = """<form id="esco-form" class="esco-form rv" novalidate>
          <div class="hp" aria-hidden="true"><label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
          <div class="two">
            <div class="field"><label>{facility_l} <span class="req">*</span></label>
              <select name="facility" id="esco-facility" required>{facility_opts}</select></div>
            <div class="field"><label>{fname_l} <span class="req">*</span></label>
              <input name="facility_name" required data-i18n-ph="esco.f.fname.ph" placeholder="{fname_ph}"></div>
          </div>
          <div class="two">
            <div class="field"><label>{region_l} <span class="req">*</span></label>
              <input name="region" required data-i18n-ph="esco.f.region.ph" placeholder="{region_ph}"></div>
            <div class="field"><label>{scale_l}</label>
              <input name="scale" data-i18n-ph="esco.f.scale.ph" placeholder="{scale_ph}"></div>
          </div>
          <div class="two">
            <div class="field"><label>{bill_l}</label><select name="monthly_bill">{bill_opts}</select></div>
            <div class="field"><label>{role_l}</label><select name="role">{role_opts}</select></div>
          </div>
          <div class="two">
            <div class="field"><label>{name_l} <span class="req">*</span></label>
              <input name="name" required data-i18n-ph="esco.f.name.ph" placeholder="{name_ph}"></div>
            <div class="field"><label>{phone_l} <span class="req">*</span></label>
              <input name="phone" type="tel" required data-i18n-ph="esco.f.phone.ph" placeholder="{phone_ph}"></div>
          </div>
          <div class="two">
            <div class="field"><label>{email_l} <span class="req">*</span></label>
              <input name="email" type="email" required data-i18n-ph="esco.f.email.ph" placeholder="{email_ph}"></div>
            <div class="field"><label>{ctime_l}</label><select name="contact_time">{ctime_opts}</select></div>
          </div>
          <div class="field"><label>{note_l}</label>
            <textarea name="note" maxlength="2000" data-i18n-ph="esco.f.note.ph" placeholder="{note_ph}"></textarea></div>
          <label class="consent"><input type="checkbox" name="consent" required> {consent}</label>
          <button class="btn blue lg" type="submit">{submit}</button>
          <p class="formnote" {fn_a} data-i18n-html>{fn}</p>
        </form>""".format(
        facility_l=S("esco.f.facility"), facility_opts=facility_opts,
        fname_l=S("esco.f.fname"), fname_ph=T["esco.f.fname.ph"][0],
        region_l=S("esco.f.region"), region_ph=T["esco.f.region.ph"][0],
        scale_l=S("esco.f.scale"), scale_ph=T["esco.f.scale.ph"][0],
        bill_l=S("esco.f.bill"), bill_opts=bill_opts,
        role_l=S("esco.f.role"), role_opts=role_opts,
        name_l=S("esco.f.name"), name_ph=T["esco.f.name.ph"][0],
        phone_l=S("esco.f.phone"), phone_ph=T["esco.f.phone.ph"][0],
        email_l=S("esco.f.email"), email_ph=T["esco.f.email.ph"][0],
        ctime_l=S("esco.f.ctime"), ctime_opts=ctime_opts,
        note_l=S("esco.f.note"), note_ph=T["esco.f.note.ph"][0],
        consent=S("esco.f.consent"), submit=S("esco.f.submit"),
        fn_a=w("esco.f.formnote",True)[0], fn=T["esco.f.formnote"][0])
    apply_section = """<section class="pad s96" data-bg="line" id="apply">
    <div class="wrap sectlabel">
      {eye}
      <h2 class="rv small">{h2}</h2>
      <div id="esco-success" class="quote-success" style="display:none">
        <div class="success-tag">{dtag}</div>
        <h2>{dh}</h2>
        <p>{dp}</p>
        <button class="btn" id="esco-reset">{dreset}</button>
      </div>
      {form}
    </div>
  </section>""".format(
        eye=S("esco.apply.eye",cls="eyebrow rv"), h2=S("esco.apply.h2",html=True),
        dtag=S("esco.done.tag"), dh=S("esco.done.h"), dp=S("esco.done.p"), dreset=S("esco.done.reset"),
        form=apply_form)

    seo_row = '<div class="seo-kw wrap">#ESCO #조명ESCO #에너지절약전문기업 #LED교체 #전기요금절감 #무료진단 #아파트조명 #주차장조명 #공장조명</div>'
    body = (header("esco") + "<main>" + hero + what + led + targets + calc + cases
            + structure + faq + apply_section + "</main>" + seo_row)

    service_ld = json.dumps({
        "@context":"https://schema.org","@type":"Service",
        "serviceType":"조명 ESCO (에너지절약전문기업) 사업",
        "name":"조명 ESCO 무료 절감 진단","url":DOMAIN+"/esco.html",
        "provider":{"@type":"Organization","name":"하우인터내셔널","url":DOMAIN},
        "areaServed":{"@type":"Country","name":"대한민국"},
        "description":"초기비용 0원으로 노후 조명을 3세대 스마트 AI LED로 교체하고 절감된 전기요금으로 상환하는 조명 ESCO 사업. 무료 절감 진단 제공."
    }, ensure_ascii=False)
    faq_ld = json.dumps({
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":T["esco.faq.q%d"%i][0],
                       "acceptedAnswer":{"@type":"Answer","text":T["esco.faq.a%d"%i][0]}} for i in range(1,8)]
    }, ensure_ascii=False)
    return head(
        "조명 ESCO — 초기비용 0원 LED 교체 · 무료 절감 진단 | 하우인터내셔널",
        "초기비용 0원으로 노후 조명을 3세대 스마트 AI LED로 바꾸고 절감된 전기요금으로 상환하는 조명 ESCO. 아파트·주차장·공장·병원 등 무료 절감 진단을 신청하세요.",
        "/esco.html","esco",
        extra_ld=[breadcrumb_ld([("홈","index.html"),("ESCO","esco.html")]), service_ld, faq_ld],
        keywords="ESCO,조명ESCO,에너지절약전문기업,LED교체,전기요금절감,무료진단,아파트조명,주차장조명,공장조명,에너지효율화,하우인터내셔널"
    ) + body + footer()

# ---------------------------------------------------------------- write i18n.js
def write_i18n():
    d = {k:{"ko":v[0],"en":v[1]} for k,v in T.items()}
    js = "window.I18N = " + json.dumps(d, ensure_ascii=False, indent=0) + ";\n"
    open(os.path.join(OUT,"assets","i18n.js"),"w",encoding="utf-8").write(js)

# ---------------------------------------------------------------- SEO/config
def seo_and_config():
    import datetime
    today = datetime.date.today().isoformat()
    freq = {"index.html":"weekly","business.html":"monthly","portfolio.html":"monthly","esco.html":"monthly",
            "about.html":"yearly","news.html":"daily","library.html":"weekly","quote.html":"monthly"}
    pri  = {"index.html":"1.0","business.html":"0.9","portfolio.html":"0.8","esco.html":"0.9",
            "about.html":"0.7","news.html":"0.8","library.html":"0.7","quote.html":"0.8"}
    pages = ["index.html","business.html","portfolio.html","esco.html","about.html","news.html","library.html","quote.html"]
    urls = "".join(
        '  <url><loc>%s/%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>\n'
        % (DOMAIN, p, today, freq.get(p,"monthly"), pri.get(p,"0.7"))
        for p in pages)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>\n'
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sitemap)
    open(os.path.join(OUT,"robots.txt"),"w").write("User-agent: *\nAllow: /\nDisallow: /admin.html\n\nSitemap: %s/sitemap.xml\n"%DOMAIN)
    manifest = {"name":"하우인터내셔널","short_name":"HOW","start_url":"/","display":"standalone",
                "background_color":"#ffffff","theme_color":"#0000FF",
                "icons":[{"src":"/assets/how-logo.png","sizes":"any","type":"image/png"}]}
    open(os.path.join(OUT,"site.webmanifest"),"w",encoding="utf-8").write(json.dumps(manifest,ensure_ascii=False,indent=2))

# ---------------------------------------------------------------- run
def main():
    global VER
    write_i18n()
    VER = asset_ver()
    files = {
        "index.html":home(),
        "about.html":about(),
        "business.html":business(),
        "portfolio.html":portfolio(),
        "esco.html":esco(),
        "quote.html":quote(),
        "news.html":listpage("news"),
        "library.html":listpage("library"),
    }
    for name,html in files.items():
        open(os.path.join(OUT,name),"w",encoding="utf-8").write(html)
    seo_and_config()
    print("generated:", ", ".join(sorted(files)))
    print("i18n keys:", len(T))

if __name__=="__main__":
    main()
