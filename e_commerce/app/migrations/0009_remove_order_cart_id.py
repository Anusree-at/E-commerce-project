# Generated by Django 5.0.3 on 2024-07-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_id',
        ),
    ]