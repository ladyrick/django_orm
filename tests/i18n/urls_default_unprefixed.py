from django_orm.conf.urls.i18n import i18n_patterns
from django_orm.http import HttpResponse
from django_orm.urls import path, re_path
from django_orm.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    re_path(r"^(?P<arg>[\w-]+)-page", lambda request, **arg: HttpResponse(_("Yes"))),
    path("simple/", lambda r: HttpResponse(_("Yes"))),
    re_path(r"^(.+)/(.+)/$", lambda *args: HttpResponse()),
    prefix_default_language=False,
)
