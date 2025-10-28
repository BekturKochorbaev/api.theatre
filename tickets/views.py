from django.shortcuts import render
from rest_framework import generics

from .models import Seat
from .serializsers import SeatSerializer


class SeatListView(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
