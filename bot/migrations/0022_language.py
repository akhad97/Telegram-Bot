# Generated by Django 3.1.7 on 2021-03-18 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0021_auto_20210318_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=30)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.vacancy')),
            ],
        ),
    ]