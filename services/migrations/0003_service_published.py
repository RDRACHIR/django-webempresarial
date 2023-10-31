# Generated by Django 4.2.6 on 2023-10-28 01:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_services_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion'),
        ),
    ]
