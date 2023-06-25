from django_orm.urls import path

urlpatterns = [
    path("ending-with-dollar$", lambda x: x),
]
