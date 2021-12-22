from django.shortcuts import render
from authenticate.models import Employee
from .models import Salary,Department, Deduction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin')
def details(request):
    # emp = request.user.eid
    # salary_list = Salary.objects.filter(eid=request.user) 
    salary_list = Salary.objects.filter(eid=request.user.id)
    deduction_list = Deduction.objects.filter(eid=request.user.id)
    emp_details = User.objects.filter(id=request.user.id)
    emp_details_2 = Employee.objects.get(user=request.user)

    # for list in salary_list.iterator():
    #     if salary_list.index(list) in [0,1,2,3,9]:
    #         pass
    #     total += list

    s = salary_list[0]
    total_salary = s.basic_salary + s.hra + s.conveyance_allowance + s.medical_allowance + s.performance_bonus + s.others
    total_deductions = deduction_list[0].damt
    net_salary = total_salary - total_deductions

    return render(request, "salary/salary_details.html", 
    {
        'salary_list':salary_list,
        'ded_list': deduction_list,
        'emp_details': emp_details,
        'emp_details_2': emp_details_2,
        'net_salary': net_salary,
    })