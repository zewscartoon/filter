from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime


# Create your models here.
class Cartoon(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='Описание')
    keywords = models.CharField(max_length=120, default='Ключевые слова')
    title = models.CharField('Название статьи', max_length = 200)
    text = models.TextField('Текст статьи')
    visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.FileField(null=True, blank=True)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return "/cartoon/%i/" % self.id

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Мультфильм'
        verbose_name_plural = 'Мультфильмы'

class Comment(models.Model):
    cartoon = models.ForeignKey(Cartoon, on_delete = models.CASCADE)
    author_name = models.CharField('Автор', max_length = 50)
    comment_text = models.CharField('Текст комментария', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
