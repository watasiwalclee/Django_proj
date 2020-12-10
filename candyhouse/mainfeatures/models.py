from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=15)
    acount = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    in_battle = models.BooleanField(default=False)
    compensate = models.BooleanField(default=False)
    uid = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'member'

class Record(models.Model):
    uid = models.ForeignKey(Member, on_delete=models.CASCADE)
    turn = models.IntegerField(null=True,blank=True)
    compensate = models.BooleanField(default=False)
    week = models.IntegerField(null=True,blank=True)
    num = models.IntegerField(null=True,blank=True)
    damage = models.IntegerField(null=True,blank=True)
    ending = models.BooleanField(default=False)

    class Meta:
        db_table = 'record'
