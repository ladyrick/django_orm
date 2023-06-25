from django_orm.http import HttpResponse
from django_orm.urls import path

urlpatterns = [
    path("", lambda request: HttpResponse("root is here")),
]
