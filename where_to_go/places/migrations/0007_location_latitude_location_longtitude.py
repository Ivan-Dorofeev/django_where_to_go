# Generated by Django 4.1.1 on 2022-10-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20220930_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='location',
            name='longtitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
    ]
