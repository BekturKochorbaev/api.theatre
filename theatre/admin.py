from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline

from .models import EventCategory, EventDate, Event, Play, TheatreDescription, TheatreImage, AboutTheatre, TeamCategory, \
    Team, GalleryCategory, Gallery, Repertoire, Contact, GalleryImage
from .translation import MediaAdminMixin
from adminsortable2.admin import SortableAdminMixin


@admin.register(EventCategory)
class EventCategoryAdmin(TranslationAdmin, MediaAdminMixin):
    list_display = ('name',)


class EventDateInline(admin.TabularInline):
    model = EventDate
    extra = 1


@admin.register(Event)
class EventAdmin(TranslationAdmin, MediaAdminMixin):
    inlines = [EventDateInline,]
    list_display = ('title', 'category', 'price')


@admin.register(Play)
class PlayAdmin(TranslationAdmin, MediaAdminMixin):
    list_display = ('title', 'director', 'genre', 'time')


class TheatreDescriptionInline(TranslationTabularInline, admin.TabularInline):
    model = TheatreDescription
    extra = 1


class TheatreImageInline(admin.TabularInline):
    model = TheatreImage
    extra = 1


@admin.register(AboutTheatre)
class AboutTheatreAdmin(TranslationAdmin, MediaAdminMixin):
    inlines = [TheatreDescriptionInline, TheatreImageInline]
    list_display = ('title',)


@admin.register(TeamCategory)
class TeamCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Team)
class TeamAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'position', 'category')
    ordering = ['order']


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('category',)



@admin.register(Repertoire)
class RepertoireAdmin(TranslationAdmin, MediaAdminMixin):
    list_display = ('title', 'genre')


@admin.register(Contact)
class RepertoireAdmin(admin.ModelAdmin):
    list_display = ('address', 'number', 'whatsapp', 'instagram')




