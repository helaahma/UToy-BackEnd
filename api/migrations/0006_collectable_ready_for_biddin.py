# Generated by Django 2.2.6 on 2019-10-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191008_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectable',
            name='ready_for_biddin',
            field=models.BooleanField(default=False),
        ),
    ]
