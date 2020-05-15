import django_filters
from .models import User
class UserFilter(django_filters.FilterSet):
    uId = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    pwd = django_filters.CharFilter(lookup_expr='icontains')
    types=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields =['uId','name','pwd','types']