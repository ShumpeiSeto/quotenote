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

## スクリーンショット

（準備中）

## 今後の実装予定

- AI 機能（引用文への多角的な視点提供）
- 全文検索機能
- レコメンド機能

## 作者

Shumpei Seto
