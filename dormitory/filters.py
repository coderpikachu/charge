import django_filters
from .models import Dormitory
class DormitoryFilter(django_filters.FilterSet):
    dId = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Dormitory
        fields = ['accommodationCharge']