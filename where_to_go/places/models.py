from django.db import models
from django.utils.html import format_html_join, format_html


class Location(models.Model):
    title = models.CharField('Название места', max_length=50)
    description = models.TextField('Описание')
    latitude = models.FloatField('Широта', blank=True, null=True)
    longtitude = models.FloatField('Долгота', blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Location, verbose_name='Локация', related_name='images', on_delete=models.CASCADE,
                                 blank=True, null=True)
    images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.location} - {self.images}'

    class Meta:
        ordering = ["location"]