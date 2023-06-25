from django_orm.contrib.staticfiles.handlers import StaticFilesHandler
from django_orm.test import LiveServerTestCase


class StaticLiveServerTestCase(LiveServerTestCase):
    """
    Extend django_orm.test.LiveServerTestCase to transparently overlay at test
    execution-time the assets provided by the staticfiles app finders. This
    means you don't need to run collectstatic before or as a part of your tests
    setup.
    """

    static_handler = StaticFilesHandler
