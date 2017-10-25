from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    occupation = models.CharField(
        '직업',
        max_length=10,
        blank=True,
    )
    gender = models.CharField(
        '성별',
        max_length=5,
        blank=True,
    )
    img_profile = models.ImageField(
        upload_to='user',
        blank=True,
    )
