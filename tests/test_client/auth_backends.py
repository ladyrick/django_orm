from django_orm.contrib.auth.backends import ModelBackend


class TestClientBackend(ModelBackend):
    pass


class BackendWithoutGetUserMethod:
    pass
