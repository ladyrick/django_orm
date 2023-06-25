from template_tests.utils import setup

from django_orm.template import TemplateSyntaxError
from django_orm.test import SimpleTestCase


class I18nLanguageTagTests(SimpleTestCase):
    libraries = {"i18n": "django_orm.templatetags.i18n"}

    @setup({"i18n_language": "{% load i18n %} {% language %} {% endlanguage %}"})
    def test_no_arg(self):
        with self.assertRaisesMessage(
            TemplateSyntaxError, "'language' takes one argument (language)"
        ):
            self.engine.render_to_string("i18n_language")
