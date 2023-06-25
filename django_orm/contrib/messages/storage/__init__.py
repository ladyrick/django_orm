from django_orm.conf import settings
from django_orm.utils.module_loading import import_string


def default_storage(request):
    """
    Callable with the same interface as the storage classes.

    This isn't just default_storage = import_string(settings.MESSAGE_STORAGE)
    to avoid accessing the settings at the module level.
    """
    return import_string(settings.MESSAGE_STORAGE)(request)
