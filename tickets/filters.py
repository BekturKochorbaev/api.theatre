import django_filters
from .models import Ticket, Seat


class TicketListFilter(django_filters.FilterSet):
    buyer_name = django_filters.CharFilter(field_name='buyer_name', lookup_expr='exact')
    buyer_phone = django_filters.CharFilter(field_name='buyer_phone', lookup_expr='exact')
    buyer_email = django_filters.CharFilter(field_name='buyer_email', lookup_expr='exact')

    class Meta:
        model = Ticket
        fields = ['buyer_name', 'buyer_phone', 'buyer_email']


class SeatListFilter(django_filters.FilterSet):
    event = django_filters.CharFilter(
        field_name='event__title',
        lookup_expr='icontains',
        label='Название концерта'
    )
    row = django_filters.NumberFilter(field_name='row', lookup_expr='exact')
    number = django_filters.NumberFilter(field_name='number', lookup_expr='exact')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='exact')
    is_sold = django_filters.BooleanFilter(field_name='is_sold')

    class Meta:
        model = Seat
        fields = ['event', 'row', 'number', 'price', 'is_sold']

