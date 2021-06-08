from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
