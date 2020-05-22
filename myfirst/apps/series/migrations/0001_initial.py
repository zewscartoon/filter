# Generated by Django 3.0.3 on 2020-05-01 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Описание')),
                ('keywords', models.CharField(default='Ключевые слова', max_length=120)),
                ('title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('visible', models.BooleanField(default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Автор')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Текст комментария')),
                ('cartoon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.Serie')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
