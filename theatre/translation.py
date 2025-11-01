from modeltranslation.translator import TranslationOptions, register
from theatre.models import EventCategory, Event, Play, AboutTheatre, TheatreDescription, Repertoire


class MediaAdminMixin:
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(EventCategory)
class EventCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'short_address', 'description')


@register(Play)
class PlayTranslationOptions(TranslationOptions):
    fields = ('title', 'director', 'author', 'genre', 'premiere', 'address', 'description')


@register(AboutTheatre)
class AboutTheatreTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TheatreDescription)
class TheatreDescriptionTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Repertoire)
class RepertoireTranslationOptions(TranslationOptions):
    fields = ('title', 'genre')


