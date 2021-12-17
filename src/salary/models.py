from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from authenticate.models import Employee
from django.db.models.deletion import CASCADE

# Create your models here.
class Department:
    dno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=20)
    mgrid = models.CharField(max_length=10)
    dept_date = models.DateField()
    
    def __str__(self):
        return self.dname

class Salary:
    slipno = models.CharField(max_length=10, primary_key=True)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
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
