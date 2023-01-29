from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class comic(models.Model):
    img = models.TextField()
    name = models.CharField(max_length = 200)
    web = models.TextField()

class member(models.Model):
    avatar = models.TextField()
    membername = models.CharField(max_length = 50)

