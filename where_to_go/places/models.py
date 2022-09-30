from django.db import models


class Location(models.Model):
    title = models.CharField('Название места', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title
