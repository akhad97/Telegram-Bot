# Generated by Django 3.1.7 on 2021-03-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_auto_20210318_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='resume',
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/%Y/%m'),
        ),
    ]
