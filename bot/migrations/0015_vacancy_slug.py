# Generated by Django 3.1.7 on 2021-03-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20210318_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
