# Generated by Django 2.0.5 on 2018-08-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racechart', '0006_auto_20180802_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='track',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]