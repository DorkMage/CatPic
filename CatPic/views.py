from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils.safestring import mark_safe
from .models import Pic
from .models import Filter
from random import randint
import json


def index(request):
    clowder = dict()
    catpics = Pic.objects.all()
    for i, pic in enumerate(catpics):
        url = pic.pic_url.url
        cats = pic.pic_cats
        text = pic.pic_name
        clowder[i] = ([url, cats, text])
    filters_qs = Filter.objects.all()
    filters = dict()
    for i, fil in enumerate(filters_qs):
        fil_text = fil.fil_text
        fil_cat = fil.fil_cat
        filters[i] = ([fil_text, fil_cat])
    template = loader.get_template('catpic/index.html')
    try:
        catpic = catpics[randint(0, len(catpics) - 1)]
    except:
        catpic = None
    #catpic = None
    context = {
        'filters_qs': filters_qs,
        'filters': mark_safe(json.dumps(filters)),
        'catpic': catpic,
        'clowder': mark_safe(json.dumps(clowder))
    }
    return HttpResponse(template.render(context, request))
