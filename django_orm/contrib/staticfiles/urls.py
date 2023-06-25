from django_orm.conf import settings
from django_orm.conf.urls.static import static
from django_orm.contrib.staticfiles.views import serve

urlpatterns = []


def staticfiles_urlpatterns(prefix=None):
    """
    Helper function to return a URL pattern for serving static files.
    """
    if prefix is None:
        prefix = settings.STATIC_URL
    return static(prefix, view=serve)


# Only append if urlpatterns are empty
if settings.DEBUG and not urlpatterns:
    urlpatterns += staticfiles_urlpatterns()
