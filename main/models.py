from django.db import models


# Create your models here.
class Stories(models.Model):
    id = models.IntegerField(primary_key=True)
    article = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=350, blank=True)
    comments = models.CharField(max_length=200, blank=True)
    domain = models.CharField(max_length=350, blank=True)
    points = models.IntegerField(blank=True)
    time_stamp = models.CharField(max_length=200, blank=True)
    by = models.CharField(max_length=256, blank=True, null=True)
    descendants = models.CharField(max_length=256, blank=True, null=True)
    kids = models.CharField(max_length=256, blank=True, null=True)
    score = models.CharField(max_length=256, blank=True, null=True)
    time = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
