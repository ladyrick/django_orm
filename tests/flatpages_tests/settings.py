import os

FLATPAGES_TEMPLATES = [
    {
        "BACKEND": "django_orm.template.backends.django_orm.DjangoTemplates",
        "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
        "OPTIONS": {
            "context_processors": ("django_orm.contrib.auth.context_processors.auth",),
        },
    }
]
