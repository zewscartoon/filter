# Generated by Django 3.0.3 on 2020-04-19 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premiers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='premier',
        ),
    ]
