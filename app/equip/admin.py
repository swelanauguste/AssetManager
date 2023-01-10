from django.contrib import admin

from .models import (
    Equipment,
    EquipmentModel,
    EquipmentNote,
    EquipmentType,
    Make,
    Status,
    IPAddress
)

admin.site.register(Equipment)
admin.site.register(EquipmentModel)
admin.site.register(Status)
admin.site.register(Make)
admin.site.register(EquipmentType)
admin.site.register(EquipmentNote)
admin.site.register(IPAddress)