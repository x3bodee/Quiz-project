# Generated by Django 3.2.3 on 2021-05-19 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
    ]
