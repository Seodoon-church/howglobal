# CLAUDE.md — 하우인터내셔널 웹사이트

> Claude Code가 이 저장소에서 작업할 때 먼저 읽는 문서입니다.
> 세부 작업 명세는 `docs/TASKS.md`, 이력은 `docs/개발일지.md`를 참고하세요.

## 프로젝트
- **무엇**: 하우인터내셔널(HOW INTERNATIONAL) 공식 웹사이트. 신규 도메인 **howglobal.co.kr**.
- **성격**: 세 사업부(유통 · 헬스케어 · 디지털미디어)를 소개하는 프리미엄 B2B 사이트 + 관리자 어드민.
- **스택**: 바닐라 정적 사이트(프레임워크 없음) + **Firebase**(Hosting · Auth · Firestore · Storage). GA4(선택).
  - 프레임워크를 쓰지 않는 것은 **의도된 선택**입니다. 공개 사이트와 어드민을 하나의 가벼운 스택으로 유지합니다. 새 라이브러리/빌드도구 도입은 먼저 제안·컨펌 후에.

## ⚠️ 작업 방식 (사용자 선호 — 반드시 준수)
1. **계획 먼저**: 실행 전 계획을 세운다.
2. **방향 점검**: 그 계획이 목표에 맞는지 한 번 더 검토한다.
3. **컨펌 후 실행**: 파일을 만들거나 고치기 전에 사용자 확인을 받는다.
4. **기록**: 실행 후 `docs/개발일지.md`에 무엇을 왜 했는지 남긴다.
- 응답·주석·커밋 메시지는 **한국어**.

## 회사 정보 (푸터·SEO·문의처의 정본)
- 사명: 하우인터내셔널 (HOW INTERNATIONAL)
- 사업자등록번호: **214-88-51839**
- 주소: 경기도 화성시 동탄광역환승로73
- 이메일: **howintlsoft@gmail.com** (기본 관리자 계정 후보)
- 도메인: howglobal.co.kr

## 사업 구성 (콘텐츠 정본)
- **디지털미디어사업부 (DIV. 01)**
  - marketshare — 분양몰 솔루션 · https://marketshare-2e00c.web.app/
  - KoreanFlow — 한국어 학습 플랫폼 · https://koreanflow.app
  - 우리家 이야기(familya) — 디지털 족보 · https://familya.co.kr
  - 고객 맞춤 플랫폼 개발 (수탁)
- **헬스케어사업부 (DIV. 02)**
  - Painfree 8800 — KFDA Class III 6-in-1 통증치료 의료기기(제조 GM R&D) · https://painfree8800.com
- **유통사업부 (DIV. 03)**
  - 바이오타맥스(BiotaMax) — 미국 직수입 토양생균제, 10종 유익 토양미생물 · https://biotamax.co.kr
- **에너지사업부 (DIV. 04) — 조명 ESCO**
  - 초기비용 0원으로 노후 조명을 3세대 스마트 AI LED로 교체하고 절감된 전기요금으로 상환하는 ESCO 사업. 하우인터내셔널은 **제안·사업 총괄**(상담 창구, 무료 진단 연결, 계약~준공 관리).
  - 파트너: 켑코이에스㈜(에너지효율화사업자·금융·성과보증), ㈜투반산업(EPC·3세대 AI LED 제조·시공·하자보증 60개월)
  - 페이지: `/esco.html` — 무료 절감 진단 신청(Firestore `inquiries`, `type:"esco"`). 영업 1순위: 아파트. 제안서 PDF는 비공개(신청자 개별 발송).

## 브랜드 토큰 (styles.css의 :root)
- 블루(강조 전용): `#0000FF` / blue-ink `#0D1BD1`
- 잉크 `#0A0C14` · 보조 `#20242F` · muted `#6A707E`
- 화이트 `#FFFFFF` · 미스트 `#F4F5F8` · 블루워시 `#EEF0FF` · 라인 `#E4E6EC`
- 폰트: **Pretendard**(국문/본문) · **Space Grotesk**(라틴 디스플레이) · **Space Mono**(스펙 라벨)
- 톤: 블루는 **포인트로만**. 편집형 카탈로그 + 모노 스펙 라벨(4-디비전: 유통 · 헬스케어 · 디지털미디어 · 에너지).

## 저장소 구조
```
howglobal/
├─ CLAUDE.md                      ← 이 문서
├─ README.md                      ← 사람용 온보딩
├─ package.json                   ← npm 스크립트
├─ firebase.json .firebaserc      ← Firebase 프로젝트/호스팅
├─ firestore.rules storage.rules  ← 보안 규칙
├─ firestore.indexes.json
├─ tools/
│  └─ build.py                    ← 페이지·i18n·SEO 생성기 (소스)
├─ public/                        ← 배포 대상(Firebase hosting public)
│  ├─ index/about/business/news/library/contact .html   ← 생성물
│  ├─ admin.html                  ← 관리자(스캐폴드)
│  ├─ assets/
│  │  ├─ styles.css  app.js       ← 손으로 편집하는 소스
│  │  ├─ i18n.js                  ← 생성물 (build.py가 씀)
│  │  ├─ firebase.js              ← Firebase 통합(설정 시 자동 활성)
│  │  ├─ firebase-config.js       ← 여기에 콘솔 값 입력
│  │  └─ how-logo.png
│  ├─ data/  news.json library.json   ← 어드민 연동 전 임시 콘텐츠 소스
│  └─ sitemap.xml robots.txt site.webmanifest  ← 생성물
└─ docs/  TASKS.md  개발일지.md
```

### ✅ 소스 vs 생성물 (중요)
- **직접 편집(소스)**: `tools/build.py`(페이지 템플릿 + `T` 번역사전), `public/assets/styles.css`, `public/assets/app.js`, `public/assets/firebase.js`, `public/admin.html`, `public/data/*.json`
- **생성물(직접 편집 금지 — `npm run build`로 재생성)**: `public/*.html`(단, admin.html은 소스), `public/assets/i18n.js`, `public/sitemap.xml`, `public/robots.txt`, `public/site.webmanifest`
- 공개 페이지의 문구/구조를 바꾸려면 **build.py의 `T`와 템플릿을 고치고 `npm run build`**.

## 명령어
```bash
npm run dev            # build 후 public/을 http://localhost:5173 로 서빙
npm run build          # tools/build.py 실행 → public/ 재생성
npm run emulate        # firebase 에뮬레이터(Auth/Firestore/Hosting/Storage)
npm run deploy         # build 후 firebase 전체 배포
npm run deploy:hosting # 호스팅만
npm run deploy:rules   # firestore/storage 규칙만
```
> 최초 1회: `.firebaserc`의 `YOUR_FIREBASE_PROJECT_ID`를 실제 프로젝트 ID로 교체.

## i18n (국/영)
- 한 URL에서 JS로 전환. `public/*.html`에 한국어가 인라인(=검색엔진 색인 언어), 영문은 `assets/i18n.js` 사전에서 치환.
- 패턴: 요소에 `data-i18n="키"`(텍스트), `data-i18n-html`(HTML 허용), `data-i18n-ph`(placeholder). 사전은 `T`에서 관리 → build가 `i18n.js` 생성.
- **번역 추가/수정은 build.py의 `T`에서** 하고 빌드. HTML/JS를 직접 고치지 말 것.
- SEO 심화가 필요하면 영문 `/en/` 별도 URL 생성이 다음 옵션(`docs/TASKS.md`).

## Firestore 데이터 모델
- `inquiries` — 협력 문의: `type`(distribution|healthcare|media|esco|other), `name`, `company`, `email`, `phone`, `message`, `consent`, `createdAt`. 생성 공개, 열람 관리자.
  - `type:"esco"`는 추가 필드: `facility`(시설 유형 영문 key), `facility_name`, `region`, `scale`, `monthly_bill`, `role`, `contact_time`, `note`, `calc`({monthly_bill_input, est_low, est_high} | null), `lang`, `page`. `message`는 app.js가 자동 생성(규칙상 필수). 어드민(admin.html)에서 ESCO 필터·시설 상세 표시.
- `news` — 뉴스: `title_ko/en`, `cat_ko/en`, `excerpt_ko/en`, `date`, `link`, `published`. 열람 공개, 작성 관리자.
- `library` — 자료실: `title_ko/en`, `desc_ko/en`, `type`, `size`, `file`(Storage 다운로드 URL). 열람 공개, 작성 관리자.
- `visits` — 방문 로그: `path`, `referrer`, `lang`, `ua`, `at`. 생성 공개(익명), 열람 관리자.
- 관리자 판별(`firestore.rules`의 `isAdmin()`): 커스텀 클레임 `admin:true` **또는** 이메일 `howintlsoft@gmail.com`. 운영 계정 확정 시 갱신.

## Firebase 통합 동작 (`public/assets/firebase.js`)
- `firebase-config.js`가 플레이스홀더면 **아무 것도 안 함**(사이트 정상, 문의는 mailto 폴백).
- 실제 값이 채워지면: `window.HOW_submitInquiry()`로 문의 저장, 방문 로그 자동 기록, `window.HOW.{app,db,auth,fs,authMod}` 노출 → admin.html이 재사용.
- SDK는 gstatic CDN 모듈을 동적 import(번들러 불필요).

## 현재 상태 / 다음 작업
- **완료**: 공개 사이트 7페이지(국/영·SEO, ESCO 포함), Firebase 설정·규칙, firebase.js 통합, admin 스캐폴드(+ESCO 필터).
- **다음(우선순위)**: `docs/TASKS.md` 참고
  1. Firebase 프로젝트 생성 + `firebase-config.js` 채우기 → 문의 저장/방문로그 실활성
  2. 어드민 완성: 뉴스 CRUD · 자료실 CRUD(Storage 업로드) · 방문 통계
  3. GA4 연결
  4. (옵션) 영문 `/en/` 별도 URL

## 주의사항 / 알려진 이슈
- `localStorage`는 try/catch로 감쌀 것(app.js 참고) — 일부 환경에서 접근 차단.
- familya 푸터 사업자번호(286-02-01290)가 본사(214-88-51839)와 다름 → 표기 기준 사용자 확인 필요.
- 로고는 현재 PNG. 벡터(SVG) 원본 확보 시 레티나 대응 교체.
- OG 커버(`assets/og-cover.png` 1200×630)·파비콘(`assets/favicon.png`) 미첨부 — 추가 필요.
- 접근성 기준(포커스 표시·모바일 대응·prefers-reduced-motion)은 유지할 것.
