from django.contrib import admin
from .models import Department, Salary, Deduction
# Register your models here.
admin.site.register(Department)
admin.site.register(Salary)
admin.site.register(Deduction)