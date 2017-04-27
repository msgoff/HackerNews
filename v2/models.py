from __future__ import unicode_literals

from django.db import models

class comments(models.Model):
        by =models.CharField(max_length=350,blank=True)
        ID =models.CharField(max_length=350,blank=True)
        kids =models.CharField(max_length=350,blank=True)
        parent = models.CharField(max_length=350,blank=True)
        text = models.TextField(blank=True)
        time =models.CharField(max_length=350,blank=True)


class stories(models.Model):
	descendants=models.IntegerField(blank=True)
	score=models.IntegerField(blank=True)
	time=models.CharField(max_length=350,blank=True)
	title=models.CharField(max_length=350,blank=True)
	by=models.CharField(max_length=350,blank=True)
	ID=models.CharField(max_length=350,unique=True)
	url=models.CharField(max_length=350,blank=True)
        kids =models.CharField(max_length=350,blank=True)

