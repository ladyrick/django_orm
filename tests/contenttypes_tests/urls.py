from django_orm.contrib.contenttypes import views
from django_orm.urls import re_path

urlpatterns = [
    re_path(r"^shortcut/([0-9]+)/(.*)/$", views.shortcut),
]
