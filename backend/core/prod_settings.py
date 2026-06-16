from .settings import *
import dj_database_url
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database — Railway PostgreSQL
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

# Media files — Cloudinary
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": config("CLOUDINARY_API_KEY"),
    "API_SECRET": config("CLOUDINARY_API_SECRET"),
}


# CORS — Vercel domain
# CORS_ALLOWED_ORIGINS = [
#     config("FRONTEND_URL", default="http://localhost:5173"),
# ]

SECRET_KEY = config("SECRET_KEY")

# CORS settings
CORS_ALLOWED_ORIGINS = [
   "https://doctor-portfolio-95wd.vercel.app",
   "https://doctor-portfolio-95wd-git-master-rana-s-projects19.vercel.app",
   "http://localhost:5173",
]

# সব origin allowed করতে চাইলে (শুধু টেস্টিং এর জন্য)
CORS_ALLOW_ALL_ORIGINS = True

# credentials allow করতে চাইলে (cookie, auth header)
CORS_ALLOW_CREDENTIALS = True

# কোন HTTP methods allowed হবে
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# কোন headers allowed হবে
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUD_NAME'),
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET')
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}