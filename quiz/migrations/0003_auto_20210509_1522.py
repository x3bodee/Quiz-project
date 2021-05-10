# Generated by Django 3.2.2 on 2021-05-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_rename_number_of_quiz_number_of_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='score_to_pass',
            field=models.IntegerField(help_text='requier score in %'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(help_text='Duration of the Quiz in minutes'),
        ),
    ]