# Generated by Django 2.1.5 on 2019-03-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190305_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='money',
        ),
        migrations.AddField(
            model_name='profile',
            name='money_possesed',
            field=models.FloatField(default=10000),
        ),
    ]
