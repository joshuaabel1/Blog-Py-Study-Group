# Generated by Django 4.1.1 on 2022-09-10 04:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 10, 1, 23, 5, 942950)),
        ),
    ]
