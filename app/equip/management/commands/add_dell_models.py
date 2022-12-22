from django.core.management.base import BaseCommand

from ...models import EquipmentModel, Make

DEL_COMPUTER_MODEL_LIST = [
    "OptiPlex 5000",
    "OptiPlex 5090",
    "OptiPlex 5080",
    "OptiPlex 5070",
    "OptiPlex 5060",
    "OptiPlex 7050",
    "OptiPlex 5050",
    "Precision 3660",
    "Precision 3460",
    "Precision 5860",
    "Precision 7860",
    "Precision 3460",
    "Precision T5820",
    "Precision 7820",
    "Precision t3430",
    "Precision T3620",
    "Precision T3420",
]



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in DEL_COMPUTER_MODEL_LIST:
            computer_model = _.lower()
            make = Make.objects.get(make__icontains='dell')
            EquipmentModel.objects.get_or_create(make=make,computer_model=computer_model)
            self.stdout.write(self.style.SUCCESS(f"{make} - {computer_model}"))