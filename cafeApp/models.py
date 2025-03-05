from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Dishes(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="dishes/", null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts", null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)  # Додаємо сесію
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE, related_name="cart_items", null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username if self.user else 'Гість'}"