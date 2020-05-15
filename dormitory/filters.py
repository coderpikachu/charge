import django_filters
from .models import Dormitory
class DormitoryFilter(django_filters.FilterSet):
    dId = django_filters.CharFilter(lookup_expr='icontains')
    telephone = django_filters.CharFilter(lookup_expr='icontains')
    peopleNum=django_filters.RangeFilter()
    accommodationCharge=django_filters.RangeFilter()
    class Meta:
        model = Dormitory
        fields = "__all__"