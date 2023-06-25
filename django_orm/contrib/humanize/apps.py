from django_orm.apps import AppConfig
from django_orm.utils.translation import gettext_lazy as _


class HumanizeConfig(AppConfig):
    name = "django_orm.contrib.humanize"
    verbose_name = _("Humanize")
