from django_orm.core.checks import Tags
from django_orm.core.management.base import BaseCommand


class Command(BaseCommand):
    requires_system_checks = [Tags.staticfiles, Tags.models]

    def handle(self, *args, **options):
        pass
