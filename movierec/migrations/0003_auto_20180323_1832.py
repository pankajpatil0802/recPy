# Generated by Django 2.0.3 on 2018-03-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierec', '0002_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
