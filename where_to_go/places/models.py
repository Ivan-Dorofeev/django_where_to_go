from django.db import models
from tinymce.models import HTMLField
from tinymce import models as tinymce_models


class Location(models.Model):
    title = models.CharField('Название места', max_length=50)
    description = tinymce_models.HTMLField(blank=True, null=True)
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