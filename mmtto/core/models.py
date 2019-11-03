from django.db import models
from datetime import datetime

# Create your models here.
class Prueba(models.Model):
    y=models.IntegerField(default=0)
    x=models.IntegerField(default=0)
