#!/bin/bash

# データベースのテーブル作成・更新
python manage.py migrate --noinput

# 静的ファイル（CSSなど）を1箇所に集める（後述）
python manage.py collectstatic --noinput

# Gunicornでサーバーを起動
# quotenote はあなたのプロジェクト名（wsgi.pyがあるフォルダ名）に変えてください
gunicorn quotenote.wsgi --bind 0.0.0.0:$PORT