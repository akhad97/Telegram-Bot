# Generated by Django 3.1.7 on 2021-03-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_auto_20210318_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contact_number',
        ),
        migrations.AlterField(
            model_name='post',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/%Y/%m'),
        ),
    ]
