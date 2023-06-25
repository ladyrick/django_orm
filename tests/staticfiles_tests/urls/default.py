from django_orm.contrib.staticfiles import views
from django_orm.urls import re_path

urlpatterns = [
    re_path("^static/(?P<path>.*)$", views.serve),
]
