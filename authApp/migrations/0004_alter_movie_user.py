# Generated by Django 3.2.7 on 2023-01-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user',
            field=models.CharField(max_length=30, verbose_name='Usuario'),
        ),
    ]
