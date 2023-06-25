from django_orm.urls import path

urlpatterns = [
    path(r"(?P<named_group>\d+)", lambda x: x),
]
