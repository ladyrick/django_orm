from django_orm.core.management.base import BaseCommand, no_translations
from django_orm.utils import translation


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        return translation.get_language()
