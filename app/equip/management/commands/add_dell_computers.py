from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Equipment, EquipmentModel, EquipmentType, Make, Status

model_count = EquipmentModel.objects.all().count()
status_count = Status.objects.all().count()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(model_count):
            equip_type = EquipmentType.objects.get(equip_type__icontains="computer")
            serial_number = fake.ean(length=8)
            model = EquipmentModel.objects.get(pk=randint(1, model_count))
            status = Status.objects.get(pk=randint(1, status_count))
            date_received = fake.date()
            Equipment.objects.get_or_create(
                equip_type=equip_type,
                serial_number=serial_number,
                model=model,
                status=status,
                date_received=date_received,
            )
            self.stdout.write(self.style.SUCCESS(f"{serial_number}"))
