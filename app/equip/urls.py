from django.urls import path

from .views import EquipmentFilterListView, EquipmentListView

urlpatterns = [
    path("", EquipmentListView.as_view(), name="equip-list"),
    path("equip-filter/", EquipmentFilterListView.as_view(), name="equip-filter-list"),
]
