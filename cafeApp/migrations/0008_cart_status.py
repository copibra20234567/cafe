# Generated by Django 5.1.1 on 2025-03-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeApp', '0007_order_carts'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
