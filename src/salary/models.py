from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from authenticate.models import *

# Create your models here.
# class Department(models.Model):
#     dno = models.IntegerField(primary_key=True)
#     dname = models.CharField(max_length=20)
#     mgrid = models.ForeignKey(User,on_delete=CASCADE)
#     dept_date = models.DateField()
    
#     def __str__(self):
#         return self.dname

class Salary(models.Model):
    slipno = models.AutoField(primary_key=True)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # dno = models.ForeignKey(Department, on_delete=CASCADE)
    
    basic_salary = models.FloatField()
    hra = models.FloatField(default=0,blank=True,null=True)
    conveyance_allowance = models.FloatField(default=0,blank=True,null=True)
    medical_allowance = models.FloatField(default=0,blank=True,null=True)
    performance_bonus = models.FloatField(default=0,blank=True,null=True)
    others = models.FloatField(default=0,blank=True,null=True)
    sdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.slipno)

class Deduction(models.Model):
    dedid = models.AutoField(primary_key=True)
    # eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    slipno = models.ForeignKey(Salary, on_delete=models.CASCADE) 
    dcategory = models.CharField(max_length=30)
    damt = models.FloatField(blank=False)

    def __str__(self):
        return str(self.dedid)

class Latest(models.Model):
    eid = models.OneToOneField(Employee, on_delete=models.CASCADE,primary_key=True)
    slipno = models.OneToOneField(Salary, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.eid.userid)+" Latest slip: "+str(self.slipno)
