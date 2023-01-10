import django_filters

from .models import Equipment


class EquipmentFilter(django_filters.FilterSet):
    serial_number = django_filters.CharFilter(lookup_expr='icontains')
    branch = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    details = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Equipment
        fields = "__all__"
