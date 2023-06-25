from django_orm.apps import AppConfig
from django_orm.utils.translation import gettext_lazy as _


class FlatPagesConfig(AppConfig):
    default_auto_field = "django_orm.db.models.AutoField"
    name = "django_orm.contrib.flatpages"
    verbose_name = _("Flat Pages")
