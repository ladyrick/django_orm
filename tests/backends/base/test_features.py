from django_orm.db import connection
from django_orm.test import SimpleTestCase


class TestDatabaseFeatures(SimpleTestCase):
    def test_nonexistent_feature(self):
        self.assertFalse(hasattr(connection.features, "nonexistent"))
