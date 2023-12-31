from django_orm.apps import AppConfig
from django_orm.contrib.messages.storage import base
from django_orm.contrib.messages.utils import get_level_tags
from django_orm.core.signals import setting_changed
from django_orm.utils.translation import gettext_lazy as _


def update_level_tags(setting, **kwargs):
    if setting == "MESSAGE_TAGS":
        base.LEVEL_TAGS = get_level_tags()


class MessagesConfig(AppConfig):
    name = "django_orm.contrib.messages"
    verbose_name = _("Messages")

    def ready(self):
        setting_changed.connect(update_level_tags)
