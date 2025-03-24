from django.contrib import admin
from .models import Dishes, Cart, Order

# Register your models here.
admin.site.register(Dishes)
admin.site.register(Cart)
admin.site.register(Order)