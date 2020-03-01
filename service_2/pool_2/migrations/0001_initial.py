# Generated by Django 3.0.3 on 2020-02-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultPoolService',
            fields=[
                ('ticket', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PoolCompare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_pool', models.IntegerField()),
                ('result_pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pool_2.ResultPoolService')),
            ],
        ),
    ]