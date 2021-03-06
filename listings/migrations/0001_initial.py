# Generated by Django 3.0.8 on 2020-08-04 13:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=16)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('kitchen', models.IntegerField(default=0)),
                ('sqft', models.IntegerField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tenants.Tenant')),
            ],
        ),
    ]
