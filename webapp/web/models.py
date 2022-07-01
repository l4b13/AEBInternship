from django.db import models

# Create your models here.

class University(models.Model):
    uname = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.uname

class Degree(models.Model):
    degree_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.degree_name

class Status(models.Model):
    status_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.status_name

class St_user(models.Model):
    # login = models.CharField(max_length=16)
    # password = models.CharField(max_length=16)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    # birthdate = models.DateField()
    age = models.IntegerField(default=20, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    current_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, blank=True, null=True)
    kurs = models.IntegerField()
    skills = models.CharField(max_length=100)
    is_accepted = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.id