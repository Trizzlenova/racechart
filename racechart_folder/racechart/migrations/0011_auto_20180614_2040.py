# Generated by Django 2.0.5 on 2018-06-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racechart', '0010_auto_20180614_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='rookie_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]