""" This containt all view of app. """

from django.shortcuts import render_to_response
from . import models


def home(request):
    """ Principal view. """
    context = {"rentables": models.Rentable.objects.all(),
               "prices": models.Prices.objects.all(),
               "allience": models.Allience.objects.first(),
               "feature": models.Feature.objects.first(),
               "sections": models.Section.objects.all()}
    return render_to_response('index.html', context)


def home_build(request):
    return render_to_response('build.html')
