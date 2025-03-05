# Generated by Django 5.1.1 on 2025-02-19 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeApp', '0003_dishes_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cafeApp.cart')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cafeApp.dishes')),
            ],
        ),
    ]
