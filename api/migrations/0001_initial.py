# Generated by Django 2.2.6 on 2019-10-02 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collectable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=60)),
                ('group', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('condition', models.CharField(blank=True, max_length=70)),
                ('special_features', models.CharField(blank=True, max_length=500)),
                ('desired_price', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collectables', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BidOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filled_price', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('bid_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bid_order', to=settings.AUTH_USER_MODEL)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
