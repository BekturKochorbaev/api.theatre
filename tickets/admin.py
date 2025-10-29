from django.contrib import admin
from .models import SeatTemplate, Seat, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('seat', 'buyer_name', 'buyer_phone', 'buyer_email')


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('event', 'row', 'number', 'price', 'is_sold')


@admin.register(SeatTemplate)
class SeatTemplateAdmin(admin.ModelAdmin):
    list_display = ('row', 'number', 'price')



