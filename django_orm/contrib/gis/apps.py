from django_orm.apps import AppConfig
from django_orm.core import serializers
from django_orm.utils.translation import gettext_lazy as _


class GISConfig(AppConfig):
    default_auto_field = "django_orm.db.models.AutoField"
    name = "django_orm.contrib.gis"
    verbose_name = _("GIS")

    def ready(self):
        serializers.BUILTIN_SERIALIZERS.setdefault(
            "geojson", "django_orm.contrib.gis.serializers.geojson"
        )
