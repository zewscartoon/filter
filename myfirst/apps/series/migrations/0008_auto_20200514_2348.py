# Generated by Django 3.0.3 on 2020-05-14 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0007_auto_20200507_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выпуска сериала'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serie',
            name='text',
            field=models.TextField(verbose_name='Описание сериала'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название сериала'),
        ),
    ]
