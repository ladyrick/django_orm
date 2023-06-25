from django_orm.conf import settings
from django_orm.contrib.messages import constants


def get_level_tags():
    """
    Return the message level tags.
    """
    return {
        **constants.DEFAULT_TAGS,
        **getattr(settings, "MESSAGE_TAGS", {}),
    }
