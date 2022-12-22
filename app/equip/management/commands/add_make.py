from django.core.management.base import BaseCommand

from ...models import Make

MANUFACTURER_LIST = [
    "HP",
    "DELL",
    "LENOVO",
    "XEROX",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in MANUFACTURER_LIST:
            make = _.lower()
            Make.objects.get_or_create(make=make)
            self.stdout.write(self.style.SUCCESS(f"{make}"))