from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    # def save(self, request):
    #     self.author = request.user

class University(models.Model):
    uname = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.uname

class Degree(models.Model):
    degree_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.degree_name

# class Status(models.Model):
#     status_name = models.CharField(max_length=40, unique=True)

#     def __str__(self):
#         return self.status_name

class St_user(models.Model):
    STATUS = [
        ('I', 'Ignored'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]
    email = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    group = models.CharField(max_length=20, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    institute = models.CharField(max_length=40)
    current_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True)
    kurs = models.IntegerField()
    skills = models.CharField(max_length=100)
    is_accepted = models.CharField(max_length=8, choices=STATUS, default='I')
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.surname + " " + self.name + " " + self.patronymic