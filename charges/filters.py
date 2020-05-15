import django_filters
from .models import Charges
class ChargeFilter(django_filters.FilterSet):
    cId = django_filters.CharFilter(lookup_expr='icontains')
    money=django_filters.RangeFilter()

    class Meta:
        model = Charges
        fields = "__all__"