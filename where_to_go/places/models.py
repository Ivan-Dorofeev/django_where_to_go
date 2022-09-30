from django.db import models


class Location(models.Model):
    title = models.CharField('Название места', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Location, verbose_name='Локация', related_name='images', on_delete=models.CASCADE,
                                 blank=True, null=True)
    images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.location} = {self.images}'
