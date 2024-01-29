import os
import environ
import dj_database_url
from pathlib import Path

env=environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent
# DEBUG =False
SECRET_KEY =os.environ.get("SECRET_KEY")
# DEBUG = os.environ.get('DEBUG', '0').lower() in ['true', 't', '1']
DEBUG =True
ALLOWED_HOSTS = []
# ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

SITE_ID=1
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',
    'main.apps.MainConfig',
     
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'ckeditor',
    'ckeditor_uploader',
]


CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS ={
    'default':{
        'tootbal':[["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
                ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                 'JustifyRight', 'JustifyBlock'],
                ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'], ["Source"],
                ["Maximize"]],
        "height":300,
        "width": '100%'
    }
}

AUTH_USER_MODEL = "myapp.User"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',#add
    'whitenoise.middleware.WhiteNoiseMiddleware',#add
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'nows.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.manicatigorey',
                'main.context_processors.reclama',
                'main.context_processors.boglanish',
                'main.context_processors.navbar',
            ],
        },
    },
]
WSGI_APPLICATION = 'nows.wsgi.application'
# DATABASE_URL=os.environ.get("DATABASE_URL")
DATABASES = {
	"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
# DATABASE_URL=os.environ.get("DATABASE_URL")
# DATABASES['default']=dj_database_url.parse(DATABASE_URL)
#"postgres://nowsdb_user:Ja8jHk2vsKQAXXA8HW0AqyV1BBUx06d0@dpg-cmqmtc821fec739ne6pg-a.oregon-postgres.render.com/nowsdb"
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
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT= os.path.join(BASE_DIR,'staticfields')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
