from rest_framework import serializers
from .models import (
    EventCategory, Event, EventDate,
    Play, AboutTheatre, TheatreDescription, TheatreImage,
    TeamCategory, Team,
    GalleryCategory, Gallery,
    Repertoire, Contact
)


# ---------- EVENT SERIALIZERS ----------

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'name']


class EventDateSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField('%d-%m-%Y ' '%H-%M')

    class Meta:
        model = EventDate
        fields = ['id', 'date']


class EventListSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer(read_only=True)
    event_date = EventDateSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'category', 'address',
            'image', 'price', 'event_date'
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer(read_only=True)
    event_date = EventDateSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'category', 'address', 'short_address',
            'image', 'price', 'age_control', 'description', 'event_date'
        ]

# ---------- PLAY & THEATRE SERIALIZERS ----------


class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ['id', 'title', 'image']


class PlayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ['id', 'title', 'director', 'genre', 'premiere', 'time', 'address', 'image', 'description']


class TheatreDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreDescription
        fields = ['id', 'description', 'theatre']


class TheatreImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreImage
        fields = '__all__'


class AboutTheatreSerializer(serializers.ModelSerializer):
    theatre_description = TheatreDescriptionSerializer(many=True, read_only=True)
    theatre_image = TheatreImageSerializer(many=True, read_only=True)

    class Meta:
        model = AboutTheatre
        fields = ['id', 'title', 'theatre_description', 'theatre_image']


# ---------- TEAM SERIALIZERS ----------

class TeamCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCategory
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    category = TeamCategorySerializer(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'category', 'name', 'position', 'image', 'order']


# ---------- GALLERY SERIALIZERS ----------

class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    category = GalleryCategorySerializer(read_only=True)

    class Meta:
        model = Gallery
        fields = ['id', 'category', 'image']


# ---------- REPERTOIRE SERIALIZER ----------

class RepertoireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repertoire
        fields = ['id', 'title', 'genre', 'date', 'time', 'age_control', 'price']


# ---------- CONTACT SERIALIZER ----------

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
