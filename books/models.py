# coding=utf-8
from django.urls import reverse
from django.db import models


class Book(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации', blank=True, null=True)
    slug = models.SlugField(u'URL', db_index=True)

    def __str__(self):
        return self.name + " " + self.author

    def get_absolute_url(self):
        return reverse('books', kwargs={'slug': self.slug})
