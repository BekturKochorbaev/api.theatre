from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from theatre.models import Event


class SeatTemplate(models.Model):
    row = models.PositiveIntegerField(verbose_name='Ряд')
    number = models.PositiveIntegerField(verbose_name='Место')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = "Шаблон места"
        verbose_name_plural = "Шаблоны мест"
        unique_together = ('row', 'number')

    def __str__(self):
        return f"Ряд {self.row}, Место {self.number} — {self.price}₽"


class Seat(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='seats', verbose_name='Концерт')
    row = models.PositiveIntegerField(verbose_name='Ряд')
    number = models.PositiveIntegerField(verbose_name='Место')
    price = models.PositiveIntegerField(verbose_name='Цена')
    is_sold = models.BooleanField(default=False, verbose_name='Продано')

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = verbose_name
        unique_together = ('event', 'row', 'number')

    def __str__(self):
        return f"{self.id} - {self.event.title}: Ряд {self.row}, Место {self.number} — {self.price} - {self.is_sold}"


class Ticket(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='ticket', verbose_name='Место')
    buyer_name = models.CharField(max_length=100, verbose_name='Имя покупателя')
    buyer_phone = models.CharField(max_length=20, verbose_name='Телефон покупателя')
    buyer_email = models.EmailField(null=True, blank=True, verbose_name='Email покупателя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Билет {self.seat} — {self.buyer_name}"


# 👇 Сигнал — внизу файла, после всех моделей!
@receiver(post_save, sender=Event)
def create_seats_for_event(sender, instance, created, **kwargs):
    """
    После создания концерта автоматически создаются все места
    на основе шаблонов SeatTemplate.
    """
    if created:
        templates = SeatTemplate.objects.all()
        seats = [
            Seat(
                event=instance,
                row=t.row,
                number=t.number,
                price=t.price,
            )
            for t in templates
        ]
        Seat.objects.bulk_create(seats)
