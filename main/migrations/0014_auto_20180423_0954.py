# Generated by Django 2.0.4 on 2018-04-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180416_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mosaicsite',
            name='period',
            field=models.CharField(blank=True, choices=[('byzantine', 'Byzantine'), ('roman', 'Roman')], max_length=50, verbose_name='Period'),
        ),
    ]
