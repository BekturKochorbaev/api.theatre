from django.db import models


class EventCategory(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='Категория')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Адрес')
    short_address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Короткий Адрес')
    image = models.FileField(upload_to='event_image/', null=True, blank=True, verbose_name='Фото')
    price = models.PositiveIntegerField(verbose_name='Цена')
    age_control = models.PositiveSmallIntegerField(verbose_name='Возрастное ограничение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class EventDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_date')
    date = models.DateTimeField(verbose_name='Дата начала')


class Play(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    director = models.CharField(max_length=300, verbose_name='Режиссёр')
    genre = models.CharField(max_length=250, verbose_name='Жанр')
    premiere = models.CharField(max_length=250, null=True, blank=True, verbose_name='Премьера')
    time = models.PositiveSmallIntegerField(verbose_name='Продолжительность')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Адрес')
    image = models.FileField(upload_to='play_image/', null=True, blank=True, verbose_name='Фото')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = "Спектакль"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class AboutTheatre(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')\


    class Meta:
        verbose_name = "Театр"
        verbose_name_plural = verbose_name


class TheatreDescription(models.Model):
    theatre = models.ForeignKey(AboutTheatre, on_delete=models.CASCADE, related_name='theatre_description')
    description = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = verbose_name


class TheatreImage(models.Model):
    theatre = models.ForeignKey(AboutTheatre, on_delete=models.CASCADE, related_name='theatre_image')
    image = models.FileField(upload_to='theatre_images/', null=True, blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = verbose_name


class TeamCategory(models.Model):
    name = models.CharField(max_length=300, verbose_name='Названия')

    class Meta:
        verbose_name = "Категория Команды"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Team(models.Model):
    category = models.ForeignKey(TeamCategory, on_delete=models.CASCADE, verbose_name='Категория ')
    name = models.CharField(max_length=300, verbose_name='ФИО')
    position = models.CharField(max_length=250, verbose_name='Должность')
    image = models.FileField(upload_to='theam_images/', null=True, blank=True, verbose_name='Фото')
    order = models.PositiveIntegerField(default=0, verbose_name='порядок')

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = verbose_name
        ordering = ['order']


    def __str__(self):
        return self.name


class GalleryCategory(models.Model):
    name = models.CharField(max_length=300, verbose_name='Названия')

    class Meta:
        verbose_name = "Категория Галереии"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, verbose_name='Категория ')
    image = models.FileField(upload_to='gallery_images/', null=True, blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = verbose_name


class Repertoire(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    genre = models.CharField(max_length=250, verbose_name='Жанр')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    age_control = models.PositiveSmallIntegerField(verbose_name='Возрастное ограничение')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = "Репертуар"
        verbose_name_plural = verbose_name


class Contact(models.Model):
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name='Адрес')
    number = models.CharField(max_length=250, null=True, blank=True, verbose_name='Номер')
    whatsapp = models.CharField(max_length=250, null=True, blank=True, verbose_name='Номер Whatsapp')
    instagram = models.URLField(null=True, blank=True, verbose_name='Ссылка на Instagram')
    facebook = models.URLField(null=True, blank=True, verbose_name='Ссылка на FaceBook')
    map_link = models.URLField(null=True, blank=True, verbose_name='Ссылка на 2GIS')

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = verbose_name
