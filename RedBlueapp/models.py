from django.db import models

# Create your models here.
class Nifty50(models.Model):
    name =models.CharField(max_length=200)
