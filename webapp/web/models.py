from django.db import models

# Create your models here.

class St_user(models.Model):
    # login = models.CharField(max_length=16)
    # password = models.CharField(max_length=16)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    # birthdate = models.DateField()
    age = models.IntegerField(default=20, blank=True)
    university = models.CharField(max_length=40)
    kurs = models.IntegerField()
    skills = models.CharField(max_length=100)
    is_accepted = models.BooleanField(default=False)

class University(models.Model):
    name = models.CharField(max_length=40)
