from django.db import models


class TimeStampAbstractModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
    )

    class Meta:
        abstract = True
