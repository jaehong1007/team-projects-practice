from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    age = models.IntegerField('나이')
    occupation = models.CharField(
        '직업',
        max_length=10,
    )
    gender = models.CharField(
        '성별',
        max_length=5,
    )
    img_profile = models.ImageField(
        upload_to='user',
        blank=True,
    )

    objects = UserManager()
