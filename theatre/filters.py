import django_filters
from .models import Gallery, Team


class GalleryListFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Gallery
        fields = ['category']


class TeamListFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Team
        fields = ['category']