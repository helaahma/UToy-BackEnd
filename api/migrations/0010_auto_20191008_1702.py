# Generated by Django 2.2.6 on 2019-10-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20191008_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidorder',
            name='available',
        ),
        migrations.RemoveField(
            model_name='collectable',
            name='ready_for_bidding',
        ),
        migrations.AlterField(
            model_name='bidorder',
            name='filled_price',
            field=models.IntegerField(null=True),
        ),
    ]
