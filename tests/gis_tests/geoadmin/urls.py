from django_orm.contrib import admin
from django_orm.urls import include, path

urlpatterns = [
    path("admin/", include(admin.site.urls)),
]
