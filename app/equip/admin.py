from django.contrib import admin

from .models import (
    Equipment,
    EquipmentModel,
    EquipmentType,
    Maintenance,
    MaintenanceComment,
    Make,
    Status,
)

admin.site.register(Equipment)
admin.site.register(EquipmentModel)
admin.site.register(Maintenance)
admin.site.register(Status)
admin.site.register(Make)
admin.site.register(EquipmentType)
admin.site.register(MaintenanceComment)
