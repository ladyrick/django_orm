import logging

from django_orm.conf import settings
from django_orm.core.mail.backends.base import BaseEmailBackend
from django_orm.views.debug import ExceptionReporter


class MyHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
        self.config = settings.LOGGING


class MyEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        pass


class CustomExceptionReporter(ExceptionReporter):
    def get_traceback_text(self):
        return "custom traceback text"
