# Generated by Django 2.0.5 on 2018-06-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racechart', '0002_auto_20180616_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standing',
            name='avg_finish_position',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='standing',
            name='avg_laps_completed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='standing',
            name='avg_start_postion',
            field=models.IntegerField(),
        ),
    ]
