from django.db import models


class Stories(models.Model):
    id = models.IntegerField(primary_key=True)
    article = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=350, blank=True)
    comments = models.CharField(max_length=200, blank=True)
    domain = models.CharField(max_length=350, blank=True)
    points = models.IntegerField(blank=True, null=True)
    time_stamp = models.CharField(max_length=200, blank=True)
    by = models.CharField(max_length=256, blank=True, null=True)
    descendants = models.IntegerField(max_length=256, blank=True, null=True)
    kids = models.CharField(max_length=256, blank=True, null=True)
    score = models.IntegerField(max_length=256, blank=True, null=True)
    time = models.IntegerField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    dead = models.BooleanField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

