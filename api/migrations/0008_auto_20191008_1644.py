# Generated by Django 2.2.6 on 2019-10-08 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191008_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidorder',
            name='available',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='allow_bids', to='api.Collectable'),
        ),
        migrations.AlterField(
            model_name='collectable',
            name='desired_price',
            field=models.IntegerField(),
        ),
    ]
