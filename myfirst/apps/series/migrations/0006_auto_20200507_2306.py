# Generated by Django 3.0.3 on 2020-05-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_auto_20200507_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='medal',
            field=models.CharField(blank=True, choices=[('Боевик', 'Боевик'), ('Комедия', 'Комедия'), ('Триллер', 'Триллер'), ('Драма', 'Драма'), ('Зарубежный', 'Зарубежный')], default='Жанр', max_length=10),
        ),
    ]
