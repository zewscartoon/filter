# Generated by Django 3.0.3 on 2020-05-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_auto_20200507_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='medal',
            field=models.CharField(blank=True, choices=[('Золото', 'Золото'), ('Серебро', 'Серебро'), ('Бронза', 'Бронза')], max_length=10),
        ),
    ]
