import django_filters
from .models import Student
class StudentFilter(django_filters.FilterSet):
    sId = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='icontains')
    nation = django_filters.CharFilter(lookup_expr='icontains')
    specialty = django_filters.CharFilter(lookup_expr='icontains')
    classId = django_filters.CharFilter(lookup_expr='icontains')
    telephone=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Student
        fields = "__all__"