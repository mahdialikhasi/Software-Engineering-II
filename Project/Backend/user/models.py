from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )
    # username
    # password
    # first_name
    # last_name
    role = models.IntegerField(null=False, blank=False)  # 1:admin , 2:student , 3:teacher
    gender = models.CharField(max_length=256, null=True, blank=True, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=256, null=True, blank=True)
    credit = models.FloatField(default=0, null=True, blank=True)
    date_of_birth = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.username + ' (' + self.first_name + ' ' + self.last_name + ')'
