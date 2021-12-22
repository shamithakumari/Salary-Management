from django.shortcuts import render
<<<<<<< HEAD
=======
from authenticate.models import Employee
>>>>>>> 396575b3f1a8428a45dc69eff94cd3570e983a98
from .models import Salary,Department, Deduction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
<<<<<<< HEAD
# @login_required(login_url='signin')
def details(request):
    # emp = request.user.eid
    # salary_list = Salary.objects.filter(eid=request.user) 
    salary_list = Salary.objects.filter(slipno=101)
    deduction_list = Deduction.objects.filter(dedid=202)
=======
@login_required(login_url='signin')
def details(request):
    # emp = request.user.eid
    # salary_list = Salary.objects.filter(eid=request.user) 
    salary_list = Salary.objects.filter(eid=request.user.id)
    deduction_list = Deduction.objects.filter(eid=request.user.id)
    emp_details = User.objects.filter(id=request.user.id)
    emp_details_2 = Employee.objects.get(user=request.user.id)

>>>>>>> 396575b3f1a8428a45dc69eff94cd3570e983a98
    return render(request, "salary/salary_details.html", 
    {
        'salary_list':salary_list,
        'ded_list': deduction_list,
<<<<<<< HEAD
=======
        'emp_details': emp_details,
        'emp_details_2': emp_details_2,
>>>>>>> 396575b3f1a8428a45dc69eff94cd3570e983a98
    })