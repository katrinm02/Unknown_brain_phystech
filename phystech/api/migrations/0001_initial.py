# Generated by Django 3.0.3 on 2020-03-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('day', models.DateField()),
            ],
        ),
    ]
