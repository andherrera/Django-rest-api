# Generated by Django 3.2.7 on 2023-01-23 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(code='nomatch', message=' A valid password MUST contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ]', regex='^(?=.?[A-Z])(?=.?[a-z])(?=.*?[!@#?\\]^]).{10,}$')], verbose_name='Password'),
        ),
    ]
