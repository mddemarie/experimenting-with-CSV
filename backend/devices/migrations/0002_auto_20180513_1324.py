# Generated by Django 2.0.5 on 2018-05-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[(1, 'sensor'), (2, 'gateway')], max_length=1),
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.CharField(choices=[(1, 'online'), (2, 'offline')], max_length=1),
        ),
    ]
