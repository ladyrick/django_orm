import re
from urllib.parse import urlsplit

from django_orm.conf import settings
from django_orm.core.exceptions import ImproperlyConfigured
from django_orm.urls import re_path
from django_orm.views.static import serve


def static(prefix, view=serve, **kwargs):
    """
    Return a URL pattern for serving files in debug mode.

    from django_orm.conf import settings
    from django_orm.conf.urls.static import static

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    elif not settings.DEBUG or urlsplit(prefix).netloc:
        # No-op if not in debug mode or a non-local prefix.
        return []
    return [
        re_path(
            r"^%s(?P<path>.*)$" % re.escape(prefix.lstrip("/")), view, kwargs=kwargs
        ),
    ]
