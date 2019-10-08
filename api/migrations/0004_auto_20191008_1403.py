# Generated by Django 2.2.6 on 2019-10-08 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectable',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bidorder',
            name='bid_item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bid_order', to='api.Collectable'),
        ),
        migrations.AlterField(
            model_name='bidorder',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
