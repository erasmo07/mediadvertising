from __future__ import unicode_literals

from django.db import models


class Feature(models.Model):
    image = models.ImageField(upload_to='features')
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=124)
    content = models.TextField()


class Section(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Percent(models.Model):
    image = models.ImageField(upload_to='percent')
    title = models.CharField(max_length=24)
    sub_title = models.CharField(max_length=24)
    content = models.CharField(max_length=240)
    rentable = models.ForeignKey('rentable', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Rentable(models.Model):
    title = models.CharField(max_length=124)
    sub_title = models.CharField(max_length=124)

    def __str__(self):
        return self.title

    def percent(self):
        return Percent.objects.filter(rentable_id=self.pk).all()


class Caracterist(models.Model):
    """ Model Representation to save caracterist of one price"""
    name = models.CharField(max_length=24)
    price = models.ForeignKey('prices')

    def __str__(self):
        return self.name


class Prices(models.Model):
    """ Model Representation to save prices. """
    title = models.CharField(max_length=12)
    sub_title = models.CharField(max_length=12, null=True, blank=True)
    price = models.CharField(max_length=3)

    def __str__(self):
        return self.title

    def get_all_caracterist(self):
        """ Get all Caracterist by self-price. """
        return Caracterist.objects.filter(price=self.pk).all()


class Allience(models.Model):
    title = models.CharField(max_length=24)
    content = models.TextField()
    image = models.ImageField(upload_to='allience')

    def __str__(self):
        return self.title
