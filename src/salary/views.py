from django.shortcuts import render
from authenticate.models import Employee
from .models import Salary,Department, Deduction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin')
def details(request):
    salary_list = Salary.objects.filter(eid=request.user.id)
    deduction_list = Deduction.objects.filter(eid=request.user.id)
    emp_details = User.objects.filter(id=request.user.id)
    emp_details_2 = Employee.objects.get(user=request.user)

    salary_list = salary_list.order_by('-sdate').first()
    total_salary = salary_list.basic_salary + salary_list.hra + salary_list.conveyance_allowance + salary_list.medical_allowance + salary_list.performance_bonus + salary_list.others
    total_deductions = deduction_list[0].damt
    net_salary = total_salary - total_deductions

    return render(request, "salary/salary_details.html", 
    {
        'list':salary_list,
        'ded_list': deduction_list,
        'emp_details': emp_details,
        'emp_details_2': emp_details_2,
        'net_salary': net_salary,
    })