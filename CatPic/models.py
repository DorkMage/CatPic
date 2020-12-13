from django.db import models


def default_cats():
    return ['cat', 'other']

class Pic(models.Model):
    pic_id = (models.CharField(max_length=16, default='CatPic000', primary_key=True, unique=True))
    pic_name = (models.CharField(max_length=64, default='A Picture of a Cat'))
    pic_url = (models.ImageField(upload_to='CatPicPics'))
    pic_cats = (models.JSONField(default=default_cats))
    objects = models.Manager

    def __str__(self):
        return self.pic_id


class Filter(models.Model):
    fil_text = (models.CharField(max_length=128, default='filter'))
    fil_cat = (models.CharField(max_length=32, default='filter'))
    objects = models.Manager

    def __str__(self):
        return self.fil_text
