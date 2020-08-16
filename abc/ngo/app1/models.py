from django.db import models

# Create your models here.

from django.db import models

class mob_login(models.Model):
    mob_email=models.CharField(max_length=100)
    mob_pass=models.CharField(max_length=100)

class op_login(models.Model):
    op_email=models.CharField(max_length=100)
    op_pass=models.CharField(max_length=100)

class mobilizer(models.Model):
    mob_name = models.CharField(max_length=100)
    mob_contact = models.IntegerField()
    mob_email = models.CharField(max_length=100)

class mob_to_task(models.Model):
    mob_name=models.CharField(max_length=100)
    mob_task=models.CharField(max_length=100)
    task_date=models.CharField(max_length=100)
    task_name=models.CharField(max_length=100)

class user(models.Model):
    user_name = models.CharField(max_length=100)
    user_contact = models.IntegerField()
    user_email = models.CharField(max_length=100)

class user_to_skills(models.Model):
    user_name=models.CharField(max_length=100)
    user_skills=models.CharField(max_length=100)

class op_manager(models.Model):
    op_name = models.CharField(max_length=100)
    op_contact = models.IntegerField()
    op_email = models.CharField(max_length=100)

class op_to_mob(models.Model):
    op_name = models.CharField(max_length=100)
    mob_name=models.CharField(max_length=100)

