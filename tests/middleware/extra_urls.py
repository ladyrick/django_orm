from django_orm.urls import path

from . import views

urlpatterns = [
    path("customurlconf/noslash", views.empty_view),
    path("customurlconf/slash/", views.empty_view),
    path("customurlconf/needsquoting#/", views.empty_view),
]
