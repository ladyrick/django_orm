from django_orm.apps import AppConfig
from django_orm.contrib.sites.checks import check_site_id
from django_orm.core import checks
from django_orm.db.models.signals import post_migrate
from django_orm.utils.translation import gettext_lazy as _

from .management import create_default_site


class SitesConfig(AppConfig):
    default_auto_field = "django_orm.db.models.AutoField"
    name = "django_orm.contrib.sites"
    verbose_name = _("Sites")

    def ready(self):
        post_migrate.connect(create_default_site, sender=self)
        checks.register(check_site_id, checks.Tags.sites)
