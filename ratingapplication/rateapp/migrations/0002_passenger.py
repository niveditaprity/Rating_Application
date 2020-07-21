# Generated by Django 3.0.8 on 2020-07-20 18:06
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_id', models.CharField(max_length=20)),
                ('passenger_name', models.CharField(max_length=100)),
                ('passenger_rating', models.IntegerField()),
            ],
        ),
    ]