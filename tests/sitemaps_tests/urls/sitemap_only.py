from django_orm.contrib.sitemaps import views
from django_orm.urls import path

urlpatterns = [
    path(
        "sitemap-without-entries/sitemap.xml",
        views.sitemap,
        {"sitemaps": {}},
        name="django_orm.contrib.sitemaps.views.sitemap",
    ),
]
