from django_orm.apps import AppConfig


class MyAdmin(AppConfig):
    name = "django_orm.contrib.admin"
    verbose_name = "Admin sweet admin."


class MyAuth(AppConfig):
    name = "django_orm.contrib.auth"
    label = "myauth"
    verbose_name = "All your password are belong to us."


class BadConfig(AppConfig):
    """This class doesn't supply the mandatory 'name' attribute."""


class NotAConfig:
    name = "apps"


class NoSuchApp(AppConfig):
    name = "there is no such app"


class PlainAppsConfig(AppConfig):
    name = "apps"


class RelabeledAppsConfig(AppConfig):
    name = "apps"
    label = "relabeled"


class ModelPKAppsConfig(AppConfig):
    name = "apps"
    default_auto_field = "django_orm.db.models.BigAutoField"
