from django.core.management.base import BaseCommand

from ...models import EquipmentType

MANUFACTURER_LIST = [
    "computer",
    "scanner",
    "printer",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in MANUFACTURER_LIST:
            equip_type = _.lower()
            EquipmentType.objects.get_or_create(equip_type=equip_type)
            self.stdout.write(self.style.SUCCESS(f"{equip_type}"))