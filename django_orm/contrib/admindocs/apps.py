from django_orm.apps import AppConfig
from django_orm.utils.translation import gettext_lazy as _


class AdminDocsConfig(AppConfig):
    name = "django_orm.contrib.admindocs"
    verbose_name = _("Administrative Documentation")
