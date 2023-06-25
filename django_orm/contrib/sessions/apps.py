from django_orm.apps import AppConfig
from django_orm.utils.translation import gettext_lazy as _


class SessionsConfig(AppConfig):
    name = "django_orm.contrib.sessions"
    verbose_name = _("Sessions")
