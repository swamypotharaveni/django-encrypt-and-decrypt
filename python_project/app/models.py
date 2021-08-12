from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    course = models.CharField(max_length=15)
    date=models.DateTimeField(auto_now_add=True)
