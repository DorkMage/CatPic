# Generated by Django 3.1.4 on 2020-12-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatPic', '0004_auto_20201201_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='clowder',
            name='clow_cats',
            field=models.JSONField(default=[]),
        ),
        migrations.AddField(
            model_name='clowder',
            name='clow_pics',
            field=models.JSONField(default=[]),
        ),
        migrations.AddField(
            model_name='pic',
            name='pic_cats',
            field=models.JSONField(default=[]),
        ),
    ]
