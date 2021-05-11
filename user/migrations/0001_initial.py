# Generated by Django 3.2.2 on 2021-05-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last_name')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('img', models.TextField(verbose_name='img')),
                ('user_type', models.CharField(default='1', max_length=2, verbose_name='user_type')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
