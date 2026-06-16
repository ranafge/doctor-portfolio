from .settings import *
import dj_database_url
from decouple import config

DEBUG = False
ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
        conn_max_age=600
    )
}

# Static files
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ========== CLOUDINARY (এটুকুই যথেষ্ট) ==========
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ========== CORS ==========
CORS_ALLOWED_ORIGINS = [
    "https://doctor-portfolio-95wd.vercel.app",
    "https://doctor-portfolio-95wd-git-master-rana-s-projects19.vercel.app",
    "http://localhost:5173",
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with']

SECRET_KEY = config("SECRET_KEY")