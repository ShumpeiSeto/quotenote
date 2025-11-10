let count = 0;
const good_btn = document.querySelector(".good-btn");
const good_count = document.querySelector(".good-count");
if (good_btn) {
  good_btn.addEventListener("click", function (e) {
    e.preventDefault();
    count += 1;
    good_count.textContent = `❤ ${count}`;
    good_count.classList.add("test-red-500");
  });
}

// タイトル補完を実装予定
// いったん空にしておくが使用する際に入力し*の方を有効にする
const API_KEY = "";
// const API_KEY = "YOUR_API_KEY_HERE" --- * ;

// 本の登録・タイトル補完表示
bookTitle = document.querySelector(".book-title");
if (bookTitle) {
  bookTitle.addEventListener("input", async function (e) {
    e.preventDefault();
    try {
      // いったん空にしておく
      const response = await fetch(
        `https://www.googleapis.com/books/v1/volumes?q=${keyword}+inauthor:${author}&key=${API_KEY}`
      );
      if (response.ok) {
        const data = await response.json();
      }
      // ThumbNail属性があるもののみを絞り込み
    } catch (error) {
      console.log("Error", error);
    }
    // ここで非同期処理を書く
    return null;
  });
}
// 本の登録・著者名の補完表示
bookAuthor = document.querySelector(".book-author");
if (bookAuthor) {
  bookAuthor.addEventListener("input", function (e) {
    e.preventDefault();
    // ここで非同期処理を書く
    return null;
  });
}
