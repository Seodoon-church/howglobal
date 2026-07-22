/* HOW INTERNATIONAL — Firebase 통합 (모듈)
 *
 * 동작 원칙
 *  - firebase-config.js의 값이 아직 플레이스홀더(YOUR_...)면 아무 것도 하지 않습니다.
 *    → 공개 사이트는 그대로 동작하고, 협력 문의 폼은 app.js의 mailto 폴백을 사용합니다.
 *  - 실제 값이 채워지면:
 *      · window.HOW_submitInquiry(data)  → Firestore `inquiries` 컬렉션에 저장
 *      · 방문 로그를 Firestore `visits` 컬렉션에 1건 기록(익명 집계용)
 *      · window.HOW.app / db / auth 를 노출 → admin.html 등에서 재사용
 *
 * 다음 단계(어드민)에서 이 파일의 export를 그대로 활용해 로그인·CRUD를 붙입니다.
 * SDK는 gstatic CDN의 모듈 빌드를 동적 import 합니다(번들러 불필요).
 */
const SDK = "https://www.gstatic.com/firebasejs/10.12.5";
const cfg = window.FIREBASE_CONFIG || {};
const isConfigured = !!cfg.apiKey && !/^YOUR_/.test(cfg.apiKey);

(async () => {
  if (!isConfigured) {
    // 미설정: 안전하게 종료. 폼은 mailto 폴백 사용.
    window.HOW = window.HOW || { configured: false };
    return;
  }
  try {
    const [{ initializeApp }, fs, authMod] = await Promise.all([
      import(`${SDK}/firebase-app.js`),
      import(`${SDK}/firebase-firestore.js`),
      import(`${SDK}/firebase-auth.js`),
    ]);
    const app = initializeApp(cfg);
    const db = fs.getFirestore(app);
    const auth = authMod.getAuth(app);

    // 공용 핸들 노출 (admin.html에서 재사용)
    window.HOW = {
      configured: true, app, db, auth,
      fs,        // firestore 함수 모음 (collection, addDoc, getDocs, query, orderBy, ...)
      authMod,   // auth 함수 모음 (signInWithEmailAndPassword, onAuthStateChanged, signOut, ...)
    };

    // 협력 문의 저장 (app.js가 제출 시 호출)
    window.HOW_submitInquiry = (data) =>
      fs.addDoc(fs.collection(db, "inquiries"), { ...data, createdAt: fs.serverTimestamp() });

    // 방문 로그 (익명, 관리자만 열람). 어드민 페이지는 제외.
    if (document.body.getAttribute("data-page") !== "admin") {
      try {
        await fs.addDoc(fs.collection(db, "visits"), {
          path: location.pathname,
          referrer: document.referrer || null,
          lang: (window.HOW_LANG || document.documentElement.lang || "ko"),
          ua: navigator.userAgent,
          at: fs.serverTimestamp(),
        });
      } catch (e) { /* 로그 실패는 조용히 무시 */ }
    }
  } catch (err) {
    console.warn("[HOW] Firebase 초기화 실패 — 폴백으로 동작합니다.", err);
    window.HOW = { configured: false };
  }
})();
