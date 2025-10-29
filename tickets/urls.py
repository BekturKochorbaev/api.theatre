from django.urls import path
from .views import *

urlpatterns = [
    path('seat/', SeatListView.as_view(), name='seat-list'),
    path('seat/<int:pk>/', SeatDetailUpdateView.as_view(), name='seat-detail'),
    path('ticket-create/', TicketCreateAPIView.as_view(), name='ticket-create'),
    path('ticket-list/', TicketListView.as_view(), name='ticket-create'),
]
