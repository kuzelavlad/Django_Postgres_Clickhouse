# Generated by Django 3.2.12 on 2024-06-17 20:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Position'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Position'),
            preserve_default=False,
        ),
    ]