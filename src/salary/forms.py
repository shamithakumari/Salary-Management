from django import forms
# from django.contrib.auth.models import User

from .models import *

class SalaryForm(forms.ModelForm):
    class Meta:
        model=Salary
        exclude=['slipno','eid']
    
class DeductionForm(forms.ModelForm):
    class Meta:
        model=Deduction
        fields=['dcategory','damt']