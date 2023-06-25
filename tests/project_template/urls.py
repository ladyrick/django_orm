from django_orm.urls import path

from . import views

urlpatterns = [
    path("empty/", views.empty_view),
]
