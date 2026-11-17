# Merge these lines into the existing settings.py; do not remove Django's default apps.
# Add "django.contrib.staticfiles" and your app "myApp" to INSTALLED_APPS if missing.
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
