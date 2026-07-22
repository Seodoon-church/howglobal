# TASKS — 다음 개발 단계

각 작업은 **계획 → 컨펌 → 실행 → 개발일지 기록** 순서로 진행합니다.
체크박스를 완료 시 갱신하세요.

---

## T1. Firebase 프로젝트 연결 (기반)
- [ ] Firebase 콘솔에서 프로젝트 생성(또는 기존 사용) → `.firebaserc`의 `YOUR_FIREBASE_PROJECT_ID` 교체
- [ ] Firestore(프로덕션 모드) · Authentication(이메일/비밀번호) · Storage 활성화
- [ ] `public/assets/firebase-config.js`에 웹 SDK 값 입력
- [ ] `npm run deploy:rules`로 `firestore.rules` · `storage.rules` 반영
- [ ] 관리자 계정 생성(Authentication) — 기본 후보 `howintlsoft@gmail.com`
  - 이메일 기반 권한이면 `firestore.rules`의 `isAdmin()` 이메일 확인. 커스텀 클레임 방식 원하면 아래 T5 참고.
- **완료 기준**: 로컬에서 협력 문의 제출 시 Firestore `inquiries`에 문서 생성, `visits`에 방문 기록.

## T2. 어드민 — 뉴스 CRUD
- [ ] `public/admin.html`의 `#panel-news` TODO 구현
- [ ] 목록/작성/수정/삭제 (Firestore `news`)
- [ ] 필드: `title_ko, title_en, cat_ko, cat_en, excerpt_ko, excerpt_en, date, link, published`
- [ ] 공개 `news.html`의 데이터 소스를 `data/news.json` → Firestore `news`(published=true)로 전환
  - `public/assets/app.js`의 `renderList('news', …)`를 Firestore 조회로 교체(또는 분기)
- **완료 기준**: 어드민에서 뉴스 발행 → 공개 뉴스 페이지에 노출.

## T3. 어드민 — 자료실 CRUD (+ Storage)
- [ ] `#panel-library` TODO 구현
- [ ] 파일 업로드 → Storage `library/`, 다운로드 URL 획득 → Firestore `library` 메타 저장
- [ ] 필드: `title_ko, title_en, desc_ko, desc_en, type, size, file`
- [ ] 공개 `library.html` 데이터 소스를 Firestore로 전환(빈 상태 처리 유지)
- **완료 기준**: 어드민 업로드 → 공개 자료실에서 다운로드.

## T4. 어드민 — 방문 통계
- [ ] `#panel-visits` TODO 구현: `visits` 집계(일자별/페이지별/언어별), 기간 필터
- [ ] 데이터가 많아지면 인덱스(`firestore.indexes.json`) 추가 및 배포
- **완료 기준**: 최근 방문 추이를 어드민에서 확인.

## T5. GA4 연결 (선택이지만 권장)
- [ ] GA4 속성 생성 → 측정 ID(G-XXXX)
- [ ] `firebase-config.js`의 `window.GA_MEASUREMENT_ID`에 입력
- [ ] 각 페이지 `<head>`에 gtag 스니펫 주입(빌드 시 조건부). `tools/build.py`의 `head()`에 GA 블록 추가하고, ID 없으면 미출력.
- [ ] (선택) 어드민 방문 통계에 GA 지표 병행 표시
- **참고(커스텀 클레임 관리자 방식)**: Admin SDK로
  `admin.auth().setCustomUserClaims(uid, { admin: true })` 실행 → `firestore.rules`의 이메일 조건 제거 가능.

## T6. (옵션) 영문 `/en/` 별도 URL — 영문 SEO 강화
- [ ] `tools/build.py`를 확장해 `public/en/*.html` 미러 생성(영문 인라인 + hreflang 상호 링크)
- [ ] `sitemap.xml`에 en URL 추가, `<link rel="alternate" hreflang>` 삽입
- **완료 기준**: 영문 페이지가 독립 URL로 색인 가능.

---

## 마감 전 체크
- [ ] `.firebaserc` 실제 프로젝트 ID
- [ ] `firestore.rules`/`storage.rules`의 관리자 조건 확정(이메일 or 클레임)
- [ ] OG 커버(`public/assets/og-cover.png` 1200×630), 파비콘(`public/assets/favicon.png`)
- [ ] 네이버 서치어드바이저/구글 서치콘솔 사이트 확인 메타 삽입 + sitemap 제출
- [ ] `howglobal.co.kr` 커스텀 도메인 연결(SSL 자동)
