from django_orm.apps import apps as django_apps
from django_orm.contrib.sitemaps import Sitemap
from django_orm.core.exceptions import ImproperlyConfigured


class FlatPageSitemap(Sitemap):
    def items(self):
        if not django_apps.is_installed("django_orm.contrib.sites"):
            raise ImproperlyConfigured(
                "FlatPageSitemap requires django_orm.contrib.sites, which isn't installed."
            )
        Site = django_apps.get_model("sites.Site")
        current_site = Site.objects.get_current()
        return current_site.flatpage_set.filter(registration_required=False)
