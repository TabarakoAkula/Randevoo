from django.db import models

from accounts.models import Account
from core.models import TimeStampAbstractModel

RATE_CHOICES = {}


class Feedback(TimeStampAbstractModel):
    author = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        related_name="feedback",
        verbose_name="автор",
    )
    rate = models.IntegerField(choices=RATE_CHOICES, verbose_name="оценка")
    comment = models.TextField(verbose_name="комментарий")

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
