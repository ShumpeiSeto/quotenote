# QuoteNote

本の名言を保存・共有できるソーシャルプラットフォーム

## 機能

- 📚 本の引用文を保存・管理
- 👥 フォロー/フォロワー機能
- 📖 書籍情報の登録
- 🔍 引用文の検索
- 💬 ユーザー間のつながり

## 使用技術

- Python 3.x
- Django 5.2
- SQLite（開発環境）
- JavaScript
- TailwindCSS

## セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/ShumpeiSeto/quotenote.git
cd quotenote
```

### 2. 仮想環境を作成・有効化

```bash
python -m venv venv

# Windowsの場合
venv\Scripts\activate

# Mac/Linuxの場合
source venv/bin/activate
```

### 3. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

### 4. データベースのマイグレーション

```bash
python manage.py migrate
```

### 5. 開発サーバーを起動

```bash
python manage.py runserver
```

ブラウザで http://127.0.0.1:8000/quotes/ にアクセス

## 使い方

### 1. 本を登録する

まず「本登録」から読んだ本の情報（タイトル、著者、ISBN 等）を登録します。

### 2. 引用文を作成する

「引用登録」で登録した本を選び、心に残った引用文とページ数を記録します。

### 3. タイムラインで共有

ホーム画面で自分や他のユーザーの引用文を閲覧。気になるユーザーをフォローして、読書体験を共有しましょう。

## スクリーンショット

### ホーム画面

![ホーム画面](screenshots/home.png)
引用文のタイムライン表示。フォロー/アンフォロー機能搭載。

### 引用登録

![引用登録](screenshots/quote_create.png)
本を選択し、該当ページと引用文を登録。

### 本の登録

![本の登録](screenshots/book_create.png)
書籍情報（タイトル、著者、ISBN、カテゴリ）を管理。

## 今後の実装予定

- GoogleBooksAPI を使ったタイトル入力補完と著者入力補完
- PostgreSQL に変更(全文検索機能有のため)
- レコメンド機能

## 作者

Shumpei Seto
