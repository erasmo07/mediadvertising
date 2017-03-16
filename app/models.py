from __future__ import unicode_literals

from django.db import models


class Features(models.Model):
    image = models.CharField(upload_to='features')
    title = models.CharField(max_legth=30)
    content = models.CharField(max_legth=124)


class TypeSection(models.Model):
    name = models.CharField(max_legth=24)


class Section(models.Model):
    title = models.CharField(max_legth=30)
    sub_title = models.CharField(max_legth=30)
