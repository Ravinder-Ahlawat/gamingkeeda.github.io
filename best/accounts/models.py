from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserDetail(models.Model):
    user_id = models.IntegerField()
    phone = models.CharField(max_length=10, blank=True)
    pubg_id = models.CharField(max_length=11, blank=True)
    pubg_name = models.CharField(max_length=20, blank=True)
    user = models.CharField(max_length=50, default='')

    