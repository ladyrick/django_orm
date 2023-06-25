from django_orm.contrib.admin import (
    HORIZONTAL,
    VERTICAL,
    AdminSite,
    ModelAdmin,
    StackedInline,
    TabularInline,
    action,
    autodiscover,
    display,
    register,
    site,
)
from django_orm.contrib.gis.admin.options import GeoModelAdmin, GISModelAdmin, OSMGeoAdmin
from django_orm.contrib.gis.admin.widgets import OpenLayersWidget

__all__ = [
    "HORIZONTAL",
    "VERTICAL",
    "AdminSite",
    "ModelAdmin",
    "StackedInline",
    "TabularInline",
    "action",
    "autodiscover",
    "display",
    "register",
    "site",
    "GISModelAdmin",
    # RemovedInDjango50Warning.
    "GeoModelAdmin",
    "OpenLayersWidget",
    "OSMGeoAdmin",
]
