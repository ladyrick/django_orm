from django_orm.urls import include, path, re_path

urlpatterns = [
    path(
        "",
        include(
            [
                re_path("^include-with-dollar$", include([])),
            ]
        ),
    ),
]
