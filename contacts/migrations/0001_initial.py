# Generated by Django 5.1.6 on 2025-02-16 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[+]?[0-9]*$', message='Enter a valid phone number.')])),
            ],
        ),
    ]
