import unittest

from django_orm.contrib.messages.middleware import MessageMiddleware
from django_orm.http import HttpRequest, HttpResponse


class MiddlewareTests(unittest.TestCase):
    def test_response_without_messages(self):
        """
        MessageMiddleware is tolerant of messages not existing on request.
        """
        request = HttpRequest()
        response = HttpResponse()
        MessageMiddleware(lambda req: HttpResponse()).process_response(
            request, response
        )
