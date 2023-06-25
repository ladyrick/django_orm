from django_orm.contrib.flatpages.sitemaps import FlatPageSitemap
from django_orm.contrib.sitemaps import views
from django_orm.urls import include, path

urlpatterns = [
    path(
        "flatpages/sitemap.xml",
        views.sitemap,
        {"sitemaps": {"flatpages": FlatPageSitemap}},
        name="django_orm.contrib.sitemaps.views.sitemap",
    ),
    path("flatpage_root/", include("django_orm.contrib.flatpages.urls")),
    path("accounts/", include("django_orm.contrib.auth.urls")),
]
