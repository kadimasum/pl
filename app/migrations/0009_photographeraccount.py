# Generated by Django 4.0.4 on 2022-05-31 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotographerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_amount', models.IntegerField()),
                ('orders', models.IntegerField()),
                ('doenloads', models.IntegerField()),
                ('customers', models.IntegerField()),
                ('photograher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.photographer')),
            ],
        ),
    ]