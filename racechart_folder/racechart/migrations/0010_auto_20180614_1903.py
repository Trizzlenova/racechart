# Generated by Django 2.0.5 on 2018-06-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racechart', '0009_auto_20180614_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='height',
            field=models.IntegerField(),
        ),
    ]
