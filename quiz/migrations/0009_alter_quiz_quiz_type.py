# Generated by Django 3.2 on 2021-05-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_merge_0006_quiz_quiz_type_0007_alter_quiz_quiz_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_type',
            field=models.BooleanField(default=True),
        ),
    ]
