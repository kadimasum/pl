# Generated by Django 4.0.4 on 2022-06-23 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_rating_photographer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]