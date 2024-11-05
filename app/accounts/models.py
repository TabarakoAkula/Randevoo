from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(
        to=User,
        related_name="account",
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )
    telegram_id = models.CharField(verbose_name="telegram id")
    telegram_username = models.CharField(verbose_name="telegram username")
    bio = models.TextField(null=True, blank=True, verbose_name="о себе")
    birth_date = models.DateField(blank=True, null=True, verbose_name="дата рождения")
    profile_image = models.ImageField(
        upload_to="img/profile_images/%Y-%d-%m/",
        null=True,
        blank=True,
        verbose_name="изображение профиля",
    )

    class Meta:
        verbose_name = "аккаунт"
        verbose_name_plural = "аккаунты"
