from django_orm.contrib.flatpages import views
from django_orm.urls import path

urlpatterns = [
    path("<path:url>", views.flatpage, name="django_orm.contrib.flatpages.views.flatpage"),
]
