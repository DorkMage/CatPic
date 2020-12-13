# Generated by Django 3.1.4 on 2020-12-06 23:11

import CatPic.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatPic', '0006_auto_20201201_1235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clowder',
        ),
        migrations.RemoveField(
            model_name='pic',
            name='id',
        ),
        migrations.AddField(
            model_name='pic',
            name='pic_id',
            field=models.CharField(default='CatPic000', max_length=16, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pic',
            name='pic_cats',
            field=models.JSONField(default=CatPic.models.default_cats),
        ),
        migrations.AlterField(
            model_name='pic',
            name='pic_name',
            field=models.CharField(default='A Picture of a Cat', max_length=64),
        ),
    ]
