from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from authenticate.models import Employee
# import salary
from .models import Salary,Department, Deduction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import *

# Create your views here.
@login_required(login_url='signin')
def details(request):
    eid=Employee.objects.filter(user=request.user).first()
    salary_list = Salary.objects.filter(eid=eid)

    # for slip in salary_list:
    #     deduction_list.append(Deduction.objects.filter(slipno=slip))
    emp_details = User.objects.filter(id=request.user.id)
    emp_details_2 = Employee.objects.get(user=request.user)

    salary_list = salary_list.order_by('-sdate').first()

    # salary_list is actually a salary slip
    # loop for deductions for that particular salary slip
    # filter returns a list 
    # deduction_list is queryset of deductions on that salary slip

    if salary_list:
        deduction_list=Deduction.objects.filter(slipno=salary_list)

    total_salary=0
    total_deductions=0
    net_salary=0

    if salary_list:
        total_salary = salary_list.basic_salary + salary_list.hra + salary_list.conveyance_allowance + salary_list.medical_allowance + salary_list.performance_bonus + salary_list.others
        for deduction in deduction_list:
            total_deductions+=deduction.damt
        net_salary = total_salary - total_deductions


    return render(request, "salary/salary_details.html", 
    {
        'list':salary_list,
        'ded_list': deduction_list,
        'emp_details': emp_details,
        'emp_details_2': emp_details_2,
        'net_salary': net_salary,
        'accountant': request.session.get('accountant')
    })


@login_required(login_url='signin')
def accountants(request):
    # context['employees'] = Employee.objects.all().order_by('user__first_name','user__last_name')
    employees = Employee.objects.all().order_by('userid')
    employeeind=None
    accountant= request.session.get('accountant')
    context={
        'employees': employees,
        'employeeind':employeeind,
        'accountant':accountant
    }
    return render(request, 'salary/accountants.html',context)


@login_required(login_url='signin')
def accountants_with_userid(request,userid):
    errors=[]
    salaryForm=SalaryForm()
    deductionForm=DeductionForm()
    (totsal,totded,netsal)=(0,0,0)
    success=False

    if request.method == 'POST':
        valid=True
        salaryForm=SalaryForm(request.POST)
        if salaryForm.is_valid():
            salaryobj=salaryForm.save(commit=False)
            eidobj=Employee.objects.get(userid=request.POST['eid'])
            salaryobj.eid = eidobj
            numDeductions=int(request.POST['num_deductions'])
            deductionobjs=[]
            totded=0
            for i in range(numDeductions):
                # print(f'ded1{i+1}')
                damt=request.POST.get(f'damt{i+1}')
                dcategory=request.POST.get(f'dcategory{i+1}')
                data={'damt':damt, 'dcategory':dcategory}
                deductionForm=DeductionForm(data)
                # print(request.POST.get(f'damt{i+1}'))
                # print(request.POST.get(f'dcategory{i+1}'))
                if valid and deductionForm.is_valid():
                    # print(f'ded2{i+1}')
                    deductionobj=deductionForm.save(commit=False)
                    deductionobj.eid=eidobj
                    deductionobj.slipno=salaryobj
                    deductionobjs.append(deductionobj)
                    totded+=deductionobj.damt
                else:
                    errors.append(deductionForm.errors)
                    # context['errors'].append(deductionForm.non_field_errors)
                    valid=False
            totsal=salaryobj.basic_salary+salaryobj.hra+salaryobj.conveyance_allowance+salaryobj.medical_allowance+salaryobj.performance_bonus+salaryobj.others
            totsal=totsal
            totded=totded
            netsal=totsal-totded
            if valid and totsal<totded:
                errors.append("Total salary can't be less than total deductions")
                valid=False
            if valid:
                # print('ded3')
                salaryobj.save()
                for deductionobj in deductionobjs:
                    deductionobj.save()
                success=True
        else:
            errors.append(salaryForm.errors)

    iserror =True
    if len(errors)>0:
        iserror=True
    else:
        iserror=False

    # context['employees'] = Employee.objects.all().order_by('user__first_name','user__last_name')
    employees = Employee.objects.all().order_by('userid')
    employeeind= Employee.objects.get(userid=userid)
    accountant= request.session.get('accountant')
    context={
        'errors': errors,
        'totsal': totsal,
        'totded': totded,
        'netsal': netsal,
        'success': success,
        'iserror': iserror,
        'employees': employees,
        'employeeind': employeeind,
        'accountant': accountant
    }
    return render(request, 'salary/accountants.html',context)

def slipcalc_history(slip):
    tot_salary=slip.basic_salary+slip.hra+slip.conveyance_allowance+slip.medical_allowance+slip.performance_bonus+slip.others
    deductions=Deduction.objects.filter(slipno=slip)
    num_deductions=deductions.count()
    tot_deduction=0
    for deduction in deductions:
        tot_deduction+=deduction.damt
    net_salary=tot_salary-tot_deduction
    return {'slip':slip,'tot_salary':tot_salary,'num_deductions':num_deductions,'tot_deduction':tot_deduction,'net_salary':net_salary}


@login_required(login_url='signin')
def history(request):
    # context['employees'] = Employee.objects.all().order_by('user__first_name','user__last_name')
    employees = Employee.objects.all().order_by('userid')
    employeeind=None
    slip=Salary.objects.filter(eid=employees.first()).order_by('-sdate').first()
    # context['slips']=[]
    # for slip in slips:
    #     context['slips'].append(slipcalc_history(slip))
    slipdict=None
    if slip:
        slipdict=slipcalc_history(slip)
        if not slipdict:
            slip_present=False
        else:
            slip_present=True
    else:
        slip_present=False
    accountant= request.session.get('accountant')
    context={
        'employees':employees,
        'employeeind': employeeind,
        'slipdict': slipdict,
        'slip_present': slip_present,
        'accountant': accountant
    }
    return render(request, 'salary/history.html',context)


@login_required(login_url='signin')
def history_with_userid(request,userid):
    # context['employees'] = Employee.objects.all().order_by('user__first_name','user__last_name')
    employees= Employee.objects.all().order_by('userid')
    employeeind= Employee.objects.get(userid=userid)
    slip=Salary.objects.filter(eid=employeeind).order_by('-sdate').first()
    # context['slips']=[]
    # for slip in slips:
    #      context['slips'].append(slipcalc_history(slip))
    slipdict=None
    if slip:
        slipdict=slipcalc_history(slip)
        if not slipdict:
            slip_present=False
        else:
            slip_present=True
    else:
        slip_present=False
    accountant= request.session.get('accountant')
    context={
        'employees':employees,
        'employeeind': employeeind,
        'slipdict': slipdict,
        'slip_present': slip_present,
        'accountant': accountant
    }
    return render(request, 'salary/history.html',context)


@csrf_exempt
def salary_slip_update(request,slipno):
    if(request.method == 'GET'):
        salary = Salary.objects.get(pk = slipno)
        deduction = Deduction.objects.filter(slipno = slipno).first()
        print(deduction)
        context={
            'currentSalary' :salary,
            'deduction': deduction
        }
        return render(request,'salary/salary_update.html', context)
    else:
        Salary.objects.filter(pk=slipno).update(basic_salary = request.POST['basic_salary'],
        hra=request.POST['hra'],
        conveyance_allowance=request.POST['conveyance_allowance'],
        medical_allowance=request.POST['medical_allowance'],
        performance_bonus=request.POST['performance_bonus'],
        others=request.POST['others']) 
        return redirect("history")
        