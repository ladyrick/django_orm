from django_orm.contrib.admin.decorators import action, display, register
from django_orm.contrib.admin.filters import (
    AllValuesFieldListFilter,
    BooleanFieldListFilter,
    ChoicesFieldListFilter,
    DateFieldListFilter,
    EmptyFieldListFilter,
    FieldListFilter,
    ListFilter,
    RelatedFieldListFilter,
    RelatedOnlyFieldListFilter,
    SimpleListFilter,
)
from django_orm.contrib.admin.options import (
    HORIZONTAL,
    VERTICAL,
    ModelAdmin,
    StackedInline,
    TabularInline,
)
from django_orm.contrib.admin.sites import AdminSite, site
from django_orm.utils.module_loading import autodiscover_modules

__all__ = [
    "action",
    "display",
    "register",
    "ModelAdmin",
    "HORIZONTAL",
    "VERTICAL",
    "StackedInline",
    "TabularInline",
    "AdminSite",
    "site",
    "ListFilter",
    "SimpleListFilter",
    "FieldListFilter",
    "BooleanFieldListFilter",
    "RelatedFieldListFilter",
    "ChoicesFieldListFilter",
    "DateFieldListFilter",
    "AllValuesFieldListFilter",
    "EmptyFieldListFilter",
    "RelatedOnlyFieldListFilter",
    "autodiscover",
]


def autodiscover():
    autodiscover_modules("admin", register_to=site)
