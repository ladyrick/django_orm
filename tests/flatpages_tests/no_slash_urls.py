from django_orm.urls import include, path

urlpatterns = [
    path("flatpage", include("django_orm.contrib.flatpages.urls")),
]
