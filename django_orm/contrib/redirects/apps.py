from django_orm.apps import AppConfig
from django_orm.utils.translation import gettext_lazy as _


class RedirectsConfig(AppConfig):
    default_auto_field = "django_orm.db.models.AutoField"
    name = "django_orm.contrib.redirects"
    verbose_name = _("Redirects")
