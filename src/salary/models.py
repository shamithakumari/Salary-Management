from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Department(models.Model):
    dno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=20)
    mgrid = models.ForeignKey(User,on_delete=CASCADE)
    dept_date = models.DateField()
    
    def __str__(self):
        return self.dname

class Salary(models.Model):
    slipno = models.CharField(max_length=10, primary_key=True)
    eid = models.ForeignKey(User, on_delete=models.CASCADE)
    dno = models.ForeignKey(Department, on_delete=CASCADE)
    basic_salary = models.FloatField()
    hra = models.FloatField()
    conveyance_allowance = models.FloatField()
    medical_allowance = models.FloatField()
    performance_bonus = models.FloatField()
    others = models.FloatField()
    sdate = models.DateField()

    def __str__(self):
        return self.slipno
