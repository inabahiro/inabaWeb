from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hp&xz_44qdvu6_p9z9l0qa6htz!0jpd&v)b6-$6+mn!_ucxk$c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# メディアファイルの配置場所
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガーの設定（ログのエントリーポイント）
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    },

    # ハンドラの設定（ログの出力先）
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定(ログの出力形式)
    'formatters': {
        'dev': {
            'format': '¥t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:¥(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

