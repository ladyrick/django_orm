from unittest import mock

from django_orm.db import migrations

try:
    from django_orm.contrib.postgres.operations import CryptoExtension
except ImportError:
    CryptoExtension = mock.Mock()


class Migration(migrations.Migration):
    # Required for the SHA database functions.
    operations = [CryptoExtension()]
