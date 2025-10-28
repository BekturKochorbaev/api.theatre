from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from .filters import GalleryListFilter, TeamListFilter
from .models import (
    EventCategory, Event, Play, AboutTheatre, TeamCategory, Team, Gallery, Repertoire, Contact, GalleryCategory
)
from .serializers import (
    EventCategorySerializer, PlayDetailSerializer, AboutTheatreSerializer,
    TeamCategorySerializer, TeamSerializer, GallerySerializer,
    RepertoireSerializer, ContactSerializer, EventDetailSerializer, EventListSerializer, PlayListSerializer,
    GalleryCategorySerializer
)


# ---------- EVENT ----------
class EventCategoryListView(generics.ListAPIView):
    """Запрос для получения категорий афиш"""
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer


class EventListView(generics.ListAPIView):
    """Запрос для получения афиш (детальная страниа)"""
    queryset = Event.objects.all().prefetch_related('event_date', 'category')
    serializer_class = EventListSerializer


class EventDetailView(generics.RetrieveAPIView):
    """Запрос для получения списка афиш"""
    queryset = Event.objects.all().prefetch_related('event_date', 'category')
    serializer_class = EventDetailSerializer



# ---------- PLAY & THEATRE ----------


class PlayListView(generics.ListAPIView):
    """Запрос для получения список спектаклей """
    queryset = Play.objects.all()
    serializer_class = PlayListSerializer


class PlayDetailView(generics.RetrieveAPIView):
    """Запрос для получения спектаклей (детальная страница)"""
    queryset = Play.objects.all()
    serializer_class = PlayDetailSerializer


class AboutTheatreListView(generics.ListAPIView):
    """Запрос для получения информации о театре"""
    queryset = AboutTheatre.objects.all().prefetch_related('theatre_description', 'theatre_image')
    serializer_class = AboutTheatreSerializer


# ---------- TEAM ----------
class TeamCategoryListView(generics.ListAPIView):
    """Запрос для получения списка категории команды"""
    queryset = TeamCategory.objects.all()
    serializer_class = TeamCategorySerializer


class TeamListView(generics.ListAPIView):
    """Запрос для получения списка команды"""
    queryset = Team.objects.all().select_related('category')
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeamListFilter


# ---------- GALLERY ----------

class GalleryCategoryListView(generics.ListAPIView):
    """Запрос для получения списка категории галерeи"""
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer


class GalleryListView(generics.ListAPIView):
    """Запрос для получения изображений галереи"""
    queryset = Gallery.objects.all().select_related('category')
    serializer_class = GallerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GalleryListFilter


# ---------- REPERTOIRE & CONTACT ----------


class RepertoireListView(generics.ListAPIView):
    """Запрос для получения репертуара"""
    queryset = Repertoire.objects.all()
    serializer_class = RepertoireSerializer


class ContactListView(generics.ListAPIView):
    """Запрос для получения контактной информации"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
