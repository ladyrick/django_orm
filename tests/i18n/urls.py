from django_orm.conf.urls.i18n import i18n_patterns
from django_orm.http import HttpResponse, StreamingHttpResponse
from django_orm.urls import path
from django_orm.utils.translation import gettext_lazy as _

urlpatterns = i18n_patterns(
    path("simple/", lambda r: HttpResponse()),
    path("streaming/", lambda r: StreamingHttpResponse([_("Yes"), "/", _("No")])),
)
