# Generated by Django 3.1.4 on 2020-12-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatPic', '0005_auto_20201201_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clowder',
            name='clow_cats',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='clowder',
            name='clow_pics',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='pic',
            name='pic_cats',
            field=models.JSONField(default=list),
        ),
    ]
