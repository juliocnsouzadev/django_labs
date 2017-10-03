# coding: utf-8

from django.db import models

class Profile(models.Model):
    
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=255, null=False)
    likes = models.IntegerField()

