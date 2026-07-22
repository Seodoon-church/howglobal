# 하우인터내셔널 웹사이트 (howglobal.co.kr)

유통 × 소프트웨어 두 사업부를 소개하는 공식 웹사이트. 바닐라 정적 사이트 + Firebase.

## 빠른 시작
```bash
# 1) 의존성 없이 바로 로컬 실행 (Python 필요)
npm run dev          # → http://localhost:5173

# 2) Firebase 연결
npm i -g firebase-tools
firebase login
# .firebaserc 의 YOUR_FIREBASE_PROJECT_ID 를 실제 프로젝트 ID로 교체
# public/assets/firebase-config.js 에 콘솔 SDK 값 입력

# 3) 배포
npm run deploy       # 빌드 후 전체 배포
```

## 구조 한눈에
- `public/` — 배포 대상(정적 사이트). `index/about/business/news/library/contact.html` + `admin.html`
- `tools/build.py` — 페이지·i18n·SEO 생성기. 공개 페이지 문구/구조 변경은 여기서 하고 `npm run build`
- `firebase.json`·`firestore.rules`·`storage.rules` — Firebase 설정/규칙
- `docs/` — 작업 명세(`TASKS.md`)·개발일지

## 개발할 때
클로드코드로 이어서 개발합니다. **먼저 `CLAUDE.md`를 읽어주세요** — 스택·구조·데이터모델·컨벤션·작업방식이 정리돼 있습니다.
공개 사이트는 지금 상태로 배포 가능하며, 다음 작업(어드민 완성·문의 저장·방문통계·GA4)은 `docs/TASKS.md`에 단계별로 있습니다.
