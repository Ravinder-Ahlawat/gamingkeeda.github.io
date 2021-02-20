from django.db import models

# Create your models here.

class Match(models.Model):
    match_id = models.AutoField
    match_name = models.CharField(max_length=20)
    match_type = models.CharField(max_length=5)
    match_map = models.CharField(max_length=20)
    match_date = models.DateField()
    match_time = models.TimeField()
    match_entry = models.IntegerField()
    per_kill_prize = models.IntegerField()
    winner_prize = models.IntegerField()
    match_pics = models.ImageField(default='')
    prize_pool = models.IntegerField(default=0)
    room_id = models.CharField(max_length=10, default='', blank='True')
    room_pass = models.CharField(max_length=10, default='', blank='True')


class Join(models.Model):
    username = models.CharField(max_length=20)
    pubg_id = models.IntegerField()
    Match_id = models.IntegerField()
    match_name = models.CharField(max_length=20)
    pubg_name = models.CharField(max_length=20)
    kill = models.IntegerField(null=True)
    win = models.CharField(max_length=3, default='')
    Email = models.CharField(max_length=80, default='')
    amount = models.IntegerField(null=True, default=0)
    order_id = models.CharField(max_length=10, default='')
    user_id = models.IntegerField(default=0)
    payment =models.BooleanField(default=False)

    
class Links(models.Model):
    Heading = models.CharField(max_length=50)
    link = models.URLField()


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    country = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")