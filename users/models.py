from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()

    