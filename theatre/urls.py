from django.urls import path
from .views import EventCategoryListView, EventListView, PlayListView, AboutTheatreListView, \
    TeamListView, GalleryListView, RepertoireListView, ContactListView, EventDetailView, PlayDetailView, \
    TeamCategoryListView, GalleryCategoryListView, TeamDetailView, NewsListView, VacancyListView

urlpatterns = [
    path('event-category/', EventCategoryListView.as_view(), name='event-category-list'),
    path('event/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('play/', PlayListView.as_view(), name='play-list'),
    path('play/<int:pk>', PlayDetailView.as_view(), name='play-detail'),
    path('about-theatre/', AboutTheatreListView.as_view(), name='about-theatre-list'),
    path('team-category/', TeamCategoryListView.as_view(), name='team-list'),
    path('team/', TeamListView.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('gallery-category/', GalleryCategoryListView.as_view(), name='gallery-list'),
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),
    path('repertoire/', RepertoireListView.as_view(), name='repertoire-list'),
    path('contact/', ContactListView.as_view(), name='repertoire-list'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('vacancy/', VacancyListView.as_view(), name='vacancy-list'),
]
