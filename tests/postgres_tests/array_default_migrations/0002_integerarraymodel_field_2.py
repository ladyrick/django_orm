import django_orm.contrib.postgres.fields
from django_orm.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("postgres_tests", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="integerarraydefaultmodel",
            name="field_2",
            field=django_orm.contrib.postgres.fields.ArrayField(
                models.IntegerField(), default=[], size=None
            ),
            preserve_default=False,
        ),
    ]
