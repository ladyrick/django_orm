from django_orm.urls import path

from .models import site

urlpatterns = [
    path("admin/", site.urls),
]
