from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser

from .filters import TicketListFilter, SeatListFilter
from .models import Ticket
from django_filters.rest_framework import DjangoFilterBackend

from .models import Seat
from .serializsers import SeatSerializer, TicketCreateSerializer, TicketListSerializer


class SeatListView(generics.ListAPIView):
    """Запрос для получения списка мест"""
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SeatListFilter


class SeatDetailUpdateView(generics.RetrieveUpdateAPIView):
    """Запрос для редактирования мест (детальная страница)"""
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class TicketCreateAPIView(generics.CreateAPIView):
    """Запрос для создания билета"""
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer
    parser_classes = [MultiPartParser, FormParser]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()
        return Response({
            "message": "Билет успешно оформлен!",
            "ticket_id": ticket.id,
            "ticket_pdf_url": request.build_absolute_uri(ticket.ticket_pdf.url) if ticket.ticket_pdf else None
        }, status=status.HTTP_201_CREATED)


class TicketListView(generics.ListAPIView):
    """Запрос для получения списка билетов"""
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TicketListFilter

    def get_queryset(self):
        data = self.request.query_params
        if not all([data.get('buyer_name'), data.get('buyer_phone'), data.get('buyer_email')]):
            raise ValidationError({"detail": "Необходимо указать Имя, телефон номер и email."})
        return super().get_queryset()