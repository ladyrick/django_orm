from django_orm.contrib.sitemaps import views
from django_orm.urls import path

from .http import simple_sitemaps

urlpatterns = [
    path(
        "simple/index.xml",
        views.index,
        {"sitemaps": simple_sitemaps},
        name="django_orm.contrib.sitemaps.views.index",
    ),
]
