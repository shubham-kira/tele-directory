# Generated by Django 3.2.13 on 2022-06-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rk', models.CharField(max_length=10)),
                ('appt', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('unit', models.CharField(max_length=30)),
                ('number', models.BigIntegerField()),
            ],
        ),
    ]
