from io import StringIO

from django_orm.core.management import call_command
from django_orm.test.utils import modify_settings

from . import PostgreSQLTestCase


@modify_settings(INSTALLED_APPS={"append": "django_orm.contrib.postgres"})
class InspectDBTests(PostgreSQLTestCase):
    def assertFieldsInModel(self, model, field_outputs):
        out = StringIO()
        call_command(
            "inspectdb",
            table_name_filter=lambda tn: tn.startswith(model),
            stdout=out,
        )
        output = out.getvalue()
        for field_output in field_outputs:
            self.assertIn(field_output, output)

    def test_range_fields(self):
        self.assertFieldsInModel(
            "postgres_tests_rangesmodel",
            [
                "ints = django_orm.contrib.postgres.fields.IntegerRangeField(blank=True, "
                "null=True)",
                "bigints = django_orm.contrib.postgres.fields.BigIntegerRangeField("
                "blank=True, null=True)",
                "decimals = django_orm.contrib.postgres.fields.DecimalRangeField("
                "blank=True, null=True)",
                "timestamps = django_orm.contrib.postgres.fields.DateTimeRangeField("
                "blank=True, null=True)",
                "dates = django_orm.contrib.postgres.fields.DateRangeField(blank=True, "
                "null=True)",
            ],
        )
