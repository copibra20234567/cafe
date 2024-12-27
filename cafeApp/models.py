from django.db import models

# Create your models here.


class Dishes(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)



