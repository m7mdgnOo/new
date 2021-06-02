from django.db import models
from django.contrib.auth.models import User

class name(models.Model):
    first_name1 = models.CharField(max_length=20)
    last_name1 = models.CharField(max_length=20)
    email1 = models.CharField(max_length=20)


