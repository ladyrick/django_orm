from django_orm.urls import re_path

urlpatterns = [
    re_path("^$", lambda x: x, name="name_with:colon"),
]
