from django.core.management.base import BaseCommand

from ...models import Status

STATUS_LIST = [
    "Issued",
    "decommissioned",
    "Damaged",
    "received",
    "in repair"
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in STATUS_LIST:
            status = _.lower()
            Status.objects.get_or_create(status=status)
            self.stdout.write(self.style.SUCCESS(f"{status}"))