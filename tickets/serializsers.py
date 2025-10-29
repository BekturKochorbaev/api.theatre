from rest_framework import serializers

from theatre.serializers import EventListSerializer
from .models import Seat, Ticket


class SeatSerializer(serializers.ModelSerializer):
    event = EventListSerializer(read_only=True)

    class Meta:
        model = Seat
        fields = '__all__'


class TicketCreateSerializer(serializers.ModelSerializer):
    seat_id = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.filter(is_sold=False), source='seat')
    ticket_pdf = serializers.FileField(required=True, use_url=False, label='PDF билет')

    class Meta:
        model = Ticket
        fields = ['seat_id', 'buyer_name', 'buyer_phone', 'buyer_email', 'ticket_pdf']

    def create(self, validated_data):
        seat = validated_data['seat']
        seat.is_sold = True
        seat.save()
        return super().create(validated_data)


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['buyer_name', 'buyer_phone', 'buyer_email', 'ticket_pdf']