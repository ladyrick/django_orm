import os

from django_orm.conf import settings
from django_orm.test import SimpleTestCase
from django_orm.utils.translation import activate, get_language

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pdir = os.path.split(os.path.split(os.path.abspath(here))[0])[0]
extended_locale_paths = settings.LOCALE_PATHS + [
    os.path.join(pdir, "i18n", "other", "locale"),
]


class MultipleLocaleActivationTestCase(SimpleTestCase):
    """
    Tests for template rendering when multiple locales are activated during the
    lifetime of the same process.
    """

    def setUp(self):
        self._old_language = get_language()

    def tearDown(self):
        activate(self._old_language)
