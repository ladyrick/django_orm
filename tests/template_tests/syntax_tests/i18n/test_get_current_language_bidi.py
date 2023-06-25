from template_tests.utils import setup

from django_orm.template import TemplateSyntaxError
from django_orm.test import SimpleTestCase


class I18nGetCurrentLanguageBidiTagTests(SimpleTestCase):
    libraries = {"i18n": "django_orm.templatetags.i18n"}

    @setup({"template": "{% load i18n %} {% get_current_language_bidi %}"})
    def test_no_as_var(self):
        msg = (
            "'get_current_language_bidi' requires 'as variable' (got "
            "['get_current_language_bidi'])"
        )
        with self.assertRaisesMessage(TemplateSyntaxError, msg):
            self.engine.render_to_string("template")
