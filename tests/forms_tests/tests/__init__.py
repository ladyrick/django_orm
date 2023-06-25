from unittest import skipIf

from django_orm.test.utils import override_settings

try:
    import jinja2
except ImportError:
    jinja2 = None


def jinja2_tests(test_func):
    test_func = skipIf(jinja2 is None, "this test requires jinja2")(test_func)
    return override_settings(
        # RemovedInDjango50Warning: When the deprecation ends, revert to
        # FORM_RENDERER="django_orm.forms.renderers.Jinja2",
        FORM_RENDERER="django_orm.forms.renderers.Jinja2DivFormRenderer",
        TEMPLATES={"BACKEND": "django_orm.template.backends.jinja2.Jinja2"},
    )(test_func)
