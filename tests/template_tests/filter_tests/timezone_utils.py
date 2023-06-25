from datetime import date, datetime

from django_orm.test import SimpleTestCase
from django_orm.utils import timezone


class TimezoneTestCase(SimpleTestCase):
    def setUp(self):
        self.now = datetime.now()
        self.now_tz = timezone.make_aware(
            self.now,
            timezone.get_default_timezone(),
        )
        self.now_tz_i = timezone.localtime(
            self.now_tz,
            timezone.get_fixed_timezone(195),
        )
        self.today = date.today()
