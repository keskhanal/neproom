# Generated by Django 3.0.8 on 2020-08-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200804_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='garage',
            field=models.BooleanField(null=True),
        ),
    ]