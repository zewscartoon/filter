# Generated by Django 3.0.3 on 2020-04-19 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(default='Название для изображения', max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Для слайдера',
            },
        ),
    ]
