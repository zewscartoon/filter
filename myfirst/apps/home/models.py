from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Advertisement(models.Model):
    alt = models.CharField(max_length=120, default='Название для изображения')
    image = models.FileField(null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Для слайдера'
