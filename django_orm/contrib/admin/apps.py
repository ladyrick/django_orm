from django_orm.apps import AppConfig
from django_orm.contrib.admin.checks import check_admin_app, check_dependencies
from django_orm.core import checks
from django_orm.utils.translation import gettext_lazy as _


class SimpleAdminConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    default_auto_field = "django_orm.db.models.AutoField"
    default_site = "django_orm.contrib.admin.sites.AdminSite"
    name = "django_orm.contrib.admin"
    verbose_name = _("Administration")

    def ready(self):
        checks.register(check_dependencies, checks.Tags.admin)
        checks.register(check_admin_app, checks.Tags.admin)


class AdminConfig(SimpleAdminConfig):
    """The default AppConfig for admin which does autodiscovery."""

    default = True

    def ready(self):
        super().ready()
        self.module.autodiscover()
