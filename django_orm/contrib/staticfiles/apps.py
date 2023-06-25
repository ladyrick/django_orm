from django_orm.apps import AppConfig
from django_orm.contrib.staticfiles.checks import check_finders
from django_orm.core import checks
from django_orm.utils.translation import gettext_lazy as _


class StaticFilesConfig(AppConfig):
    name = "django_orm.contrib.staticfiles"
    verbose_name = _("Static Files")
    ignore_patterns = ["CVS", ".*", "*~"]

    def ready(self):
        checks.register(check_finders, checks.Tags.staticfiles)
