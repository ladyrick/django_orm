from django_orm.urls import path

from . import widgetadmin

urlpatterns = [
    path("", widgetadmin.site.urls),
]
