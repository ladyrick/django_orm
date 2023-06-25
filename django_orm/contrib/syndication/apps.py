from django_orm.apps import AppConfig
from django_orm.utils.translation import gettext_lazy as _


class SyndicationConfig(AppConfig):
    name = "django_orm.contrib.syndication"
    verbose_name = _("Syndication")
