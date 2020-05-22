from django.db import models
from django.utils import timezone

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    email = models.EmailField()
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name + " last login in at " + self.last_login
