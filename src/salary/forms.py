from django import forms
# from django.contrib.auth.models import User
import re

from .models import *

class SalaryForm(forms.ModelForm):
    class Meta:
        model=Salary
        exclude=['slipno','eid']

    def clean(self):
        basic_salary=self.cleaned_data['basic_salary']
        hra=self.cleaned_data['hra']
        conveyance_allowance=self.cleaned_data['conveyance_allowance']
        medical_allowance=self.cleaned_data['medical_allowance']
        performance_bonus=self.cleaned_data['performance_bonus']
        others=self.cleaned_data['others']
        if not re.search("^[0-9]+$",str(basic_salary)) and basic_salary<0:
            self.add_error('basic_salary','Basic Salary must be provided and not less than 0.')

        if not hra:
            self.cleaned_data['hra']=0
        elif not re.search("^[0-9]+$",str(hra)) and hra<0:
            self.add_error('hra','Hra must not be less than 0.')

        if not conveyance_allowance:
            self.cleaned_data['conveyance_allowance']=0
        elif not re.search("^[0-9]+$",str(conveyance_allowance)) and conveyance_allowance<0:
            self.add_error('conveyance_allowance','Conveyance allowance must not be less than 0.')
        
        if not medical_allowance:
            self.cleaned_data['medical_allowance']=0
        elif not re.search("^[0-9]+$",str(medical_allowance)) and medical_allowance<0:
            self.add_error('medical_allowance','Medical allowance must not be less than 0.')

        if not performance_bonus:
            self.cleaned_data['performance_bonus']=0
        elif not re.search("^[0-9]+$",str(performance_bonus)) and performance_bonus<0:
            self.add_error('performance_bonus','Performance bonus must not be less than 0.')

        if not others:
            self.cleaned_data['others']=0
        elif not re.search("^[0-9]+$",str(others)) and others<0:
            self.add_error('Others','Others(Additional income) must not be less than 0.')

        return super(SalaryForm, self).clean()
    
class DeductionForm(forms.ModelForm):
    class Meta:
        model=Deduction
        fields=['dcategory','damt']
        # exclude=['dedid','eid','slipno']

    def clean(self):
        dcategory=self.cleaned_data['dcategory']
        damt=self.cleaned_data['damt']

        if not re.search("^[0-9]+$",str(damt)) and damt<0:
            self.add_error('damt','Deduction amount must be provided and not less than 0.')

        return super(DeductionForm, self).clean()