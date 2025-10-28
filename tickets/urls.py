from django.urls import path
from .views import *

urlpatterns = [
    path('seat/', SeatListView.as_view(), name='seat-list')
]
