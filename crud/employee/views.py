from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeForm, EmployeeRegister
from django.views.generic import ListView
from .models import Employee
from .filters import EmployeeFilter


# Create your views here.

def sidebar(request):
    return render(request, 'employee/sidebar.html')


def navbar(request):
    return render(request, 'employee/navbar.html')


def homepage(request):
    females = Employee.objects.filter(gender='F')
    males = Employee.objects.filter(gender='M')
    employees = Employee.objects.all()
    total_employees = employees.count()
    total_females = females.count()
    total_males = males.count()
    context = {
        'total_employees': total_employees,
        'total_females': total_females,
        'total_males': total_males,
    }
    return render(request, 'employee/home.html', context)


def employee_list(request):
    employees = Employee.objects.all()
    myFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = myFilter.qs
    context = {
        'employees': employees,
        'myFilter': myFilter,
    }
    return render(request, 'employee/employee_list.html', context)


def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee/employee_form.html', {
            'form': form
        })
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')


def user_login(request):
    return render(request, 'employee/login.html')
    pass


def user_register(request):
    if request.method == 'POST':
        form = EmployeeRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}. You can now login.')
            return redirect('login')
    else:
        form = EmployeeRegister()
    context = {
        'form': form
    }
    return render(request, 'employee/register.html', context)
