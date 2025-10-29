from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings

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
        return f"{self.event.title}: Ряд {self.row}, Место {self.number} — {self.price} - {self.is_sold}"


class Ticket(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='ticket', verbose_name='Место')
    buyer_name = models.CharField(max_length=100, verbose_name='Имя покупателя')
    buyer_phone = models.CharField(max_length=20, verbose_name='Телефон покупателя')
    buyer_email = models.EmailField(null=True, blank=True, verbose_name='Email покупателя')
    ticket_pdf = models.FileField(upload_to='tickets/', null=True, blank=True, verbose_name='PDF билет')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Билет {self.seat} — {self.buyer_name}"


@receiver(post_save, sender=Ticket)
def send_ticket_email(sender, instance, created, **kwargs):
    if created and instance.buyer_email and instance.ticket_pdf:
        subject = f"Ваш билет на {instance.seat.event.title}"
        body = (
            f"Здравствуйте, {instance.buyer_name}!\n\n"
            f"Спасибо за покупку билета.\n"
            f"Концерт: {instance.seat.event.title}\n"
            f"Место: ряд {instance.seat.row}, место {instance.seat.number}\n\n"
            f"Ваш билет прикреплён в PDF файле."
        )

        email = EmailMessage(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [instance.buyer_email],
        )

        # Прикрепляем PDF билет
        email.attach_file(instance.ticket_pdf.path)

        # Отправляем письмо
        email.send(fail_silently=False)


@receiver(post_save, sender=Event)
def create_seats_for_event(sender, instance, created, **kwargs):
    if created:
        templates = SeatTemplate.objects.all()
        seats = [
            Seat(
                event=instance,
                row=t.row,
                number=t.number,
                price=instance.price,
            )
            for t in templates
        ]
        Seat.objects.bulk_create(seats)
