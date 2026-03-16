from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-changeme")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".railway.app"]
# Railwayのための設定
CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "quotes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    # dj_database_urlを使った書き方に変更する
    # 環境変数 DATABASE_URLがなければローカルのSQLiteを使う
    "default": dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}", conn_max_age=600
    )
    # "default": {
    #     # 本番用にPostgreSQLに変更
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": BASE_DIR / "db.postgresql",
    # }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "ja-jp"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ログイン関連の設定
LOGIN_REDIRECT_URL = "/quotes/"  # ログイン後のリダイレクト先
LOGOUT_REDIRECT_URL = "/quotes/"  # ログアウト後のリダイレクト先

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
