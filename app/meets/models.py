from django.db import models

from accounts.models import Account
from core.models import TimeStampAbstractModel


class Meet(TimeStampAbstractModel):
    description = models.TextField(verbose_name="описание")
    date = models.DateTimeField(verbose_name="дата и время")
    lat = models.FloatField(blank=True, null=True, verbose_name="широта")
    lon = models.FloatField(blank=True, null=True, verbose_name="долгота")
    number_of_members = models.PositiveIntegerField(verbose_name="количество участников")
    is_open = models.BooleanField(verbose_name="открыта")

    class Meta:
        verbose_name = "встреча"
        verbose_name_plural = "встречи"


class Participant(models.Model):
    account = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        related_name="participant",
        verbose_name="аккаунт",
    )
    meet = models.ForeignKey(
        to=Meet,
        on_delete=models.CASCADE,
        related_name="participant",
        verbose_name="аккаунт",
    )

    class Meta:
        verbose_name = "участник"
        verbose_name_plural = "участники"
        constraints = [
            models.UniqueConstraint(
                fields=["account", "meet"],
                name="unique_participation",
            ),
        ]
