# Generated by Django 2.2.6 on 2019-10-08 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191008_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidorder',
            name='available',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='allow_bids', to='api.Collectable'),
        ),
    ]
