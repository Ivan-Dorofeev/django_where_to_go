# Generated by Django 4.1.3 on 2022-12-01 06:10

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название места')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Короткое описание')),
                ('text', tinymce.models.HTMLField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('longtitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.location', verbose_name='Локация')),
            ],
            options={
                'ordering': ['location'],
            },
        ),
    ]
