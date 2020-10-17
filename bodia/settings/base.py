import os
import sys
import environ

from celery.schedules import crontab
# from prometheus_client import multiprocess
# from prometheus_client import CollectorRegistry

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'my secret'),
    ALLOWED_HOSTS=(str, '*'),

    POSTGRES_MAIN_DB_HOST=(str, ''),
    POSTGRES_MAIN_DB_PORT=(int, 0),
    POSTGRES_MAIN_DB_NAME=(str, ''),
    POSTGRES_MAIN_DB_USER=(str, ''),
    POSTGRES_MAIN_DB_PASSWORD=(str, ''),

    POSTGRES_SEARCH_DB_HOST=(str, ''),
    POSTGRES_SEARCH_DB_PORT=(int, 0),
    POSTGRES_SEARCH_DB_NAME=(str, ''),
    POSTGRES_SEARCH_DB_USER=(str, ''),
    POSTGRES_SEARCH_DB_PASSWORD=(str, ''),

    REDIS_HOST=(str, 'localhost'),
    REDIS_PORT=(int, 6379),
    REDIS_DB=(int, 0),

    GEOPOSITION_GOOGLE_MAPS_API_KEY=(str, 'AIzaSyCZ1aXdM7uzr9SVGPwtS0Dukhv_1xDany8'),

    LIQPAY_PUBLIC_KEY=(str, 'i41433970357'),
    LIQPAY_PRIVATE_KEY=(str, '57LCBcLjhxsZaNQWC0XJqmWXGyd61RGDNg8cR9Wv'),
    LIQPAY_SANDBOX=(int, 1),
    LIQPAY_CALLBACK=(str, 'http://159.69.53.206/pay-callback'),

    SOCIAL_AUTH_FACEBOOK_KEY=(int, 0),
    SOCIAL_AUTH_FACEBOOK_SECRET=(str, ''),

    S3_AWS_ACCESS_KEY_ID=(str, ''),
    S3_AWS_SECRET_ACCESS_KEY=(str, ''),

    AWS_CLOUDFRONT_DOMAIN=(str, ''),

    SES_AWS_ACCESS_KEY_ID=(str, ''),
    SES_AWS_SECRET_ACCESS_KEY=(str, ''),

    PIPELINE_SASS_BINARY=(str, ''),
    DEFAULT_FROM_EMAIL=(str, 'ibodia@ukr.net'),
)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

AUTH_USER_MODEL = 'main.CustomUser'

ACCOUNT_ADAPTER = 'main.adapters.MyAccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_FORMS = {'signup': 'main.forms.CustomSignupForm'}
EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/auth/login/'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
CONFIRM_EMAIL_ON_GET = False

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

SECRET_KEY = env('SECRET_KEY')

# False if not in os.environ
DEBUG = env('DEBUG')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..')
sys.path.append(os.path.join(BASE_DIR, 'apps'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env('POSTGRES_MAIN_DB_HOST'),
        'PORT': env('POSTGRES_MAIN_DB_PORT'),
        'NAME': env('POSTGRES_MAIN_DB_NAME'),
        'USER': env('POSTGRES_MAIN_DB_USER'),
        'PASSWORD': env('POSTGRES_MAIN_DB_PASSWORD'),
        'CONN_MAX_AGE': 0
    },
    'search_replicas': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env('POSTGRES_SEARCH_DB_HOST'),
        'PORT': env('POSTGRES_SEARCH_DB_PORT'),
        'NAME': env('POSTGRES_SEARCH_DB_NAME'),
        'USER': env('POSTGRES_SEARCH_DB_USER'),
        'PASSWORD': env('POSTGRES_SEARCH_DB_PASSWORD'),
        'CONN_MAX_AGE': 0
    }
}

DATABASE_ROUTERS = ['bodia.database_routers.SearchReplicasRouter']

CACHEOPS_REDIS = f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/{env('REDIS_DB')}"

INSTALLED_APPS = [
    'search_replicas',
    'dextension',
    # 'dal',
    # 'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    'storages',
    'django.contrib.sitemaps',
    'social_django',
    'main',
    'coronavirus',
    'bodia_liqpay',
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    'widget_tweaks',
    'versatileimagefield',
    'ckeditor',
    'dseo',
    'django_js_reverse',
    'django_user_agents',
    'geoposition',
    'cacheops',
    'django_extensions',
    'anymail',
    'allauth',
    'allauth.account',
    'solo.apps.SoloAppConfig',
    'mapwidgets',
    # 'django_prometheus',
    'analytics',
    'apps.payment',
    'captcha',
]

RECAPTCHA_PUBLIC_KEY = '6LfP6swZAAAAAHS6I9jgeKT87mSWyhiU_EuZBnUu'
RECAPTCHA_PRIVATE_KEY = '6LfP6swZAAAAABGqfBQzeFcM5Maq5qq5HTzMRUnj   '

VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 60 * 60 * 24 * 30 * 12,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 70,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': False,
    'image_key_post_processor': None,
    'progressive_jpeg': False
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'company_image': [
        ('company_image_134', 'crop__134x134'),
        ('company_image_200', 'crop__200x200'),
        ('company_image_170', 'crop__170x170'),
        ('company_image_110', 'crop__110x110'),
        ('company_image_48', 'crop__48x48'),
        ('company_image_17', 'crop__17x17'),
    ],
    'company_bg': [
        ('company_bg', 'crop__1000x200'),
    ],
    'banner_wide': [
        ('banner_wide', 'crop__217x270'),
        ('banner_wide_250', 'crop__250x266'),
        ('banner_wide_main_250', 'crop__250x311'),
        ('banner_wide_1140', 'crop__1140x60'),
    ],
    'banner_narrow': [
        ('banner_narrow_300', 'crop__300x80'),
        ('banner_narrow_main_300', 'crop__300x75'),
        ('banner_narrow_1140', 'crop__1140x60'),
        ('banner_narrow_320', 'crop__320x48'),
    ],
    'banner_fullscreen_desk': [
        ('banner_fullscreen', 'crop__1000x480'),
    ],
    'banner_fullscreen_mob': [
        ('banner_fullscreen', 'crop__250x270'),
    ],
    'user': [
        ('user_210', 'crop__210x210'),
        ('user_60', 'crop__60x60'),
        ('user_200', 'crop__200x200'),
        ('user_250', 'crop__250x250'),
    ],
    'image_gallery': [
        ('image_gallery', 'crop__300x200'),
        ('image_gallery', 'crop__200x200'),
        ('image_gallery', 'crop__400x400'),
    ],
    'company_page': [
        ('company_page_200', 'crop__200x200'),
        ('company_page_134', 'crop__134x134'),
        ('company_page_gallery', 'crop__300x200'),
        ('company_page_170', 'crop__170x170'),
        ('company_page_110', 'crop__110x110')
    ],
    'comment_image': [
        ('comment_image_134', 'crop__134x134'),
    ],

}

MIDDLEWARE = [
    # 'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'dseo.middleware.RobotsDisallowMiddleware',
    'dseo.middleware.NoIndexMiddleware',
    'dseo.middleware.LinkRelCanonicalMiddleware',
    'dseo.middleware.LinkRelHomeMiddleware',
    'dseo.middleware.PermanentRedirectMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    # 'django_prometheus.middleware.PrometheusAfterMiddleware',
]

DSEO_LINK_REL_CANONICAL = 'https://bodia.online'
DSEO_LINK_REL_HOME = DSEO_LINK_REL_CANONICAL

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'bodia.urls'

INDEX_PAGE_SLUG = ''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.counters',
                'main.context_processors.categories',
                'main.context_processors.custom_links',
                'main.context_processors.footer_links',
                'main.context_processors.sidebar_context',
                'main.context_processors.banner_context',
                'main.context_processors.additional_links',
                'main.context_processors.menu_mobile_constants',
                'main.context_processors.google_maps_api_key',
                'main.context_processors.counter_constants',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'debug': DEBUG
        },
    },
]

LIQPAY_PUBLIC_KEY = env('LIQPAY_PUBLIC_KEY')
LIQPAY_PRIVATE_KEY = env('LIQPAY_PRIVATE_KEY')
LIQPAY_SANDBOX = env('LIQPAY_SANDBOX')

LIQPAY_LANGUAGE = 'uk'
LIQPAY_CURRENCY = 'UAH'
LIQPAY_SUCCESS = 'sandbox' if DEBUG else 'success'

CSRF_COOKIE_SECURE = False

WSGI_APPLICATION = 'bodia.wsgi.application'
COMPANIES_DEFAULT_ORDER_BY = '-start'
COMPANIES_DEFAULT_ORDER_BY_SEARCH = '-rank'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

CELERY_BROKER_URL = f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/{env('REDIS_DB')}"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'ORDERING_PARAM': 'ordering',
}

SITE_ID = 1

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_global'),
    os.path.join(BASE_DIR, 'apps/main/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
TAGS_INPUT_MAPPINGS = {
    'main.Tag': {
        'field': 'value',
        'create_missing': True
    },
}
TAGS_INPUT_INCLUDE_JQUERY = True
SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']  # user_birthday, user_gender, 'user_link'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale': 'uk_UA',
    'fields': 'id, first_name, last_name, email, picture.type(large), birthday, gender, link'
}
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

EMAIL_BACKEND = 'anymail.backends.amazon_ses.EmailBackend'
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
ANYMAIL = {
    "AMAZON_SES_CLIENT_PARAMS": {
        "aws_access_key_id": env('SES_AWS_ACCESS_KEY_ID'),
        "aws_secret_access_key": env('SES_AWS_SECRET_ACCESS_KEY'),
        "region_name": "us-east-1",
        "config": {
            "connect_timeout": 30,
            "read_timeout": 30,
        }
    },
}

SOCIAL_AUTH_PIPELINE = [
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'main.social_pipeline.user_details',
]

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'liststyle',
            'image',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'table',
            'tableresize',
            'tabletools',
            'templates,'
        ]),
    },
    'simple': {
        'skin': 'moono',
        'tabSpaces': 4,
    },
    'comment_editor': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
    'company_editor': {
        'height': 'auto',
        'width': 'auto',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            {'name': 'clipboard', 'items': ['Undo', 'Redo']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'insert',
             'items': ['Table', ]},
        ],
    }
}

JS_REVERSE_INCLUDE_ONLY_NAMESPACES = ['main']

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{env('REDIS_HOST')}:{env('REDIS_PORT')}/{env('REDIS_DB')}",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        },
        'KEY_PREFIX': 'bodia_caches',
        'TIMEOUT': 600,
        'MAX_ENTRIES': 5000,
    },
}

CACHEOPS = {
    'main.*': {'ops': {'fetch', 'get'}, 'timeout': 60*60},
    'search_replicas.*': {'ops': {'fetch', 'get'}, 'timeout': 60*60},
    'coronavirus.*': {'ops': {'fetch', 'get'}, 'timeout': 60*60},
    'analytics.*': {'ops': {'fetch', 'get'}, 'timeout': 60*60},
    'dseo.*': {'ops': {'fetch', 'get'}, 'timeout': 60*60},
    'geoposition.*': {'ops': {'fetch', 'get'}, 'timeout': 60*60},
    'main.Company': None,
    'main.Comment': None,
}

UPLOAD_TO_PATHS = {
    'CustomUser': 'upload_images/avatars/%Y/%m/%d/',
    'Category': 'categories/',
    'Company': 'upload_images/avatars/%Y/%m/%d/',
    'CompanySearchReplica': 'upload_images/avatars/%Y/%m/%d/',
    'CompanyRequest': 'upload_images/avatars/%Y/%m/%d/',
    'Image': 'images/%Y/%m/%d/',
    'ImageGallery': 'upload_images/%Y/%m/%d/',
    'TopSliderImage': 'upload_images/slider_images/%Y/%m/%d/',
    'Banner': 'materials/%Y/%m/%d/',
    'CompanyPage': 'pages/%Y/%m/%d/',
    'CommentImage': 'comments/%Y/%m/%d/',
}
CACHE_MIDDLEWARE_SECONDS = 60
GEOPOSITION_GOOGLE_MAPS_API_KEY = env('GEOPOSITION_GOOGLE_MAPS_API_KEY')

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 10),
        ("mapCenterLocationName", "kiev"),
        ("mapCenterLocation", [50.3685005, 30.8950709]),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'uk'}}),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": env('GEOPOSITION_GOOGLE_MAPS_API_KEY'),
    "LANGUAGE": LANGUAGE_CODE,
}

UPDATE_PROJECT_INTERPRETER_BIN = '/home/web/.local/share/virtualenvs/bodia-Zyyw1EXJ/bin/'
UPDATE_PROJECT_SETTINGS = 'bodia.settings.sandbox'
UPDATE_PROJECT_SETTINGS_COLLECTSTATIC = 'bodia.settings.collectstatic'
UPDATE_PROJECT_S3 = 's3://bodia-production/static/'
UPDATE_PROJECT_REPO = 'git@gitlab.com:dteam.dev/bodia.git'

NAME_MAX_LENGTH = 255
SLUG_MAX_LENGTH = 50

CELERY_BEAT_SCHEDULE = {
    'inspect_subscriptions': {
        'task': 'apps.payment.tasks.inspect_subscriptions',
        'schedule': crontab(),
    },
}

DEFAULT_USER_LOGO = 'main/imgs/dummy-user-logo.png'
DEFAULT_COMPANY_BG = 'main/imgs/dummy-company-heading.png'


# Prometheus settings.
# This workaround is required because of multiworker gunicorn setup on sandbox/production servers
# So without it metrics such as counter (that can only increase) can decreasing
# because of different workers provide different stats
# Look more about it here: https://github.com/korfuri/django-prometheus/blob/master/documentation/exports.md
if not DEBUG:
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
