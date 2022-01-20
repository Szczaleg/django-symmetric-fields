from encrypted.settings import *

INSTALLED_APPS = ('tests', )

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}