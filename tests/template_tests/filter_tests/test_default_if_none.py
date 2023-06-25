from django_orm.template.defaultfilters import default_if_none
from django_orm.test import SimpleTestCase


class FunctionTests(SimpleTestCase):
    def test_value(self):
        self.assertEqual(default_if_none("val", "default"), "val")

    def test_none(self):
        self.assertEqual(default_if_none(None, "default"), "default")

    def test_empty_string(self):
        self.assertEqual(default_if_none("", "default"), "")
