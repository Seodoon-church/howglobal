/* Firebase 웹 설정 — 콘솔에서 발급한 값으로 교체하세요.
   (클라이언트 키는 공개되어도 안전합니다. 접근 제어는 firestore.rules/storage.rules로 합니다.)
   콘솔: https://console.firebase.google.com → 프로젝트 설정 → 내 앱 → SDK 설정 및 구성
   값을 채우면 assets/firebase.js가 자동으로 문의 저장·방문로그를 활성화합니다. */
window.FIREBASE_CONFIG = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};

/* GA4 측정 ID (선택). 발급 후 채우면 방문 분석용으로 사용합니다. 미설정 시 무시됩니다. */
window.GA_MEASUREMENT_ID = "";
