from django_orm.conf.urls.i18n import i18n_patterns
from django_orm.urls import path
from django_orm.views.generic import TemplateView

view = TemplateView.as_view(template_name="dummy.html")

urlpatterns = i18n_patterns(
    path("prefixed/", view, name="prefixed"),
)
