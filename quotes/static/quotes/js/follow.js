document.addEventListener("DOMContentLoaded", function () {
  const hoverCard = document.getElementById("userHoverCard");
  const triggers = document.querySelectorAll(".user-trigger");
  let hideTimeout;

  triggers.forEach((trigger) => {
    trigger.addEventListener("mouseenter", function (e) {
      clearTimeout(hideTimeout);

      // data属性からデータを取得
      const username = this.dataset.username;
      const email = this.dataset.email;
      const postCount = this.dataset.postCount;
      const followUrl = this.dataset.followUrl; // ← これが重要！

      // カードに情報をセット
      document.getElementById("userAvatar").textContent = username
        .charAt(0)
        .toUpperCase();
      document.getElementById("userName").textContent = username;
      document.getElementById("userEmail").textContent = email;
      document.getElementById("postCount").textContent = postCount;
      document.getElementById("unfollowBtn").href = followUrl; // ← URLを動的に設定

      // カードの位置を計算
      const rect = this.getBoundingClientRect();
      hoverCard.style.left = rect.left + "px";
      hoverCard.style.top = rect.bottom + window.scrollY + 10 + "px";
      hoverCard.classList.remove("hidden");
    });

    trigger.addEventListener("mouseleave", function () {
      hideTimeout = setTimeout(() => {
        hoverCard.classList.add("hidden");
      }, 300);
    });
  });

  // カード自体にマウスが乗ったら消さない
  hoverCard.addEventListener("mouseenter", function () {
    clearTimeout(hideTimeout);
  });

  hoverCard.addEventListener("mouseleave", function () {
    hoverCard.classList.add("hidden");
  });
});
