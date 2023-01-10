from django.views.generic import ListView

from .filters import EquipmentFilter
from .models import Equipment, IPAddress


class EquipmentListView(ListView):
    model = Equipment


class EquipmentFilterListView(ListView):
    model = Equipment
    template_name = "equip/filter.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EquipmentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context
