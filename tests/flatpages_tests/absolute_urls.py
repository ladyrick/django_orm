from django_orm.contrib.flatpages import views
from django_orm.urls import path

urlpatterns = [
    path("flatpage/", views.flatpage, {"url": "/hardcoded/"}),
]
