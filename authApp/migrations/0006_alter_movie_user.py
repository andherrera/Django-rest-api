# Generated by Django 3.2.7 on 2023-01-26 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0005_auto_20230125_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Email', to=settings.AUTH_USER_MODEL),
        ),
    ]
