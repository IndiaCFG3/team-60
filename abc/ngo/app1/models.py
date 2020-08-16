from django.db import models

# Create your models here.
from django.db import models
class mob_login(models.Model):
    mob_email=models.CharField(max_length=100)
    mob_pass=models.CharField(max_length=100)

class op_login(models.Model):
    op_email=models.CharField(max_length=100)
    op_pass=models.CharField(max_length=100)

class mobilizer1(models.Model):
    mob_name = models.CharField(max_length=100)
    mob_contact = models.IntegerField()
    mob_email = models.CharField(max_length=100)
    mob_task = models.CharField(max_length=100)
    mob_date_task=models.CharField(max_length=10)

class User1(models.Model):
    user_name = models.CharField(max_length=100)
    user_contact = models.IntegerField()
    user_email = models.CharField(max_length=100)

class Skills(models.Model):
    user_name = models.CharField(max_length=100)
    user_skill=models.CharField(max_length=100)
