# Generated by Django 3.0.3 on 2020-02-03 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0003_auto_20200203_2241'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PoopPending',
            new_name='PoolPending',
        ),
    ]