# Generated by Django 3.2.1 on 2021-05-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_quiz_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_type',
            field=models.BooleanField(default=False),
        ),
    ]
