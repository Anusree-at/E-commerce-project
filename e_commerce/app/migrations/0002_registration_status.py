# Generated by Django 5.0.3 on 2024-07-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=50, null=True),
        ),
    ]
