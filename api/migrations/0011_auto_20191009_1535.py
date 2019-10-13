# Generated by Django 2.2.6 on 2019-10-09 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20191008_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidorder',
            old_name='filled_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='bidorder',
            name='bid_item',
        ),
        migrations.RemoveField(
            model_name='bidorder',
            name='status',
        ),
        migrations.AddField(
            model_name='bidorder',
            name='collectable',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bid_order', to='api.Collectable'),
            preserve_default=False,
        ),
    ]