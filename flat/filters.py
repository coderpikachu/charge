import django_filters
from .models import Flat
class FlatFilter(django_filters.FilterSet):
    fId = django_filters.CharFilter(lookup_expr='icontains')
    layers=django_filters.RangeFilter()
    roomNum=django_filters.RangeFilter()
    class Meta:
        model = Flat
        fields = ['fId','layers','roomNum']