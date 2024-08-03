from os import name
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL',
                            max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
