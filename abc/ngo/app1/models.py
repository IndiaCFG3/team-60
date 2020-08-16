from django.db import models

# Create your models here.
class OprationManager(models.Model):
    Op_name=models.CharField(max_length=34)
    Op_email=models.CharField(max_length=40)
    Op_phn=models.IntegerField(max_length=10)
    Op_password=models.CharField(max_length=50)

class Op_to_Mob(models.Model):
    Op_name=models.CharField(max_length=34)
    Mob_name=models.CharField(max_length=100)