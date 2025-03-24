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


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікує підтвердження'),
        ('processing', 'Обробляється'),
        ('delivered', 'Доставлено'),
        ('canceled', 'Скасовано'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    carts = models.ManyToManyField('Cart', verbose_name="Страви у замовленні")
    full_name = models.CharField(max_length=255, verbose_name="Повне ім'я")
    address = models.TextField(verbose_name="Адреса")
    credit_card = models.CharField(max_length=16, verbose_name="Кредитна карта")  # Додаємо маску для безпеки
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)