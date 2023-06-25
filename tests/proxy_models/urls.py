from django_orm.urls import path

from .admin import site

urlpatterns = [
    path("admin/", site.urls),
]
