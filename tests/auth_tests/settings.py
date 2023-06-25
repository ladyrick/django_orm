import os

AUTH_MIDDLEWARE = [
    "django_orm.contrib.sessions.middleware.SessionMiddleware",
    "django_orm.contrib.auth.middleware.AuthenticationMiddleware",
]

AUTH_TEMPLATES = [
    {
        "BACKEND": "django_orm.template.backends.django_orm.DjangoTemplates",
        "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django_orm.template.context_processors.request",
                "django_orm.contrib.auth.context_processors.auth",
                "django_orm.contrib.messages.context_processors.messages",
            ],
        },
    }
]
