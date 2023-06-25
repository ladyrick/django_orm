from django_orm.conf.urls.i18n import i18n_patterns
from django_orm.http import HttpResponse
from django_orm.urls import path

urlpatterns = i18n_patterns(
    path("exists/", lambda r: HttpResponse()),
)
