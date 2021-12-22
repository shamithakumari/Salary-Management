from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Employee(models.Model):
    userid = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    address = models.TextField()
    phoneno = models.CharField(max_length=12)

    def __str__(self):
        return str(self.userid)

    # def create(self):


class Accountant(models.Model):
    aid = models.OneToOneField(Employee, on_delete=models.CASCADE,primary_key=True)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.aid)
