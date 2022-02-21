SECRET_KEY = "secret_key"

INSTALLED_APPS = ("tests",)

DSF_ENCRYPTION_KEYS = [
    b"qoVQ-4GEd4NO9bBKB6RKvGrzQ34-BiloN-UzV65jcko=",
    b"20q_FiBe6EF9lcEzupYqz5WeMUW_SULk6RRwvjEzhtI=",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
