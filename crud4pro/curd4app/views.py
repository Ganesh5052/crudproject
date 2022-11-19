from django.shortcuts import render,redirect
from .models import EmployeeData

def homePage(request):
    employees = EmployeeData.objects.all()
    return render(request,'homePage.html',{'employees':employees})

def addEmployee(request):
    if request.method == "GET":
        return render(request,'addEmployee.html')

    else:
        EmployeeData(
        employee_id = request.POST.get('empid'),
        employee_name = request.POST.get('empname'),
        salary = request.POST.get('salary'),
        experience = request.POST.get('exp'),
        location = request.POST.get('loc')
        ).save()
        return redirect('main_page')

def update_data(request,id):
    employee = EmployeeData.objects.get(id=id)
    return render(request,'update_data.html',{'employee':employee})

def save_update_data(request,id):
    employee = EmployeeData.objects.get(id=id)
    employee.employee_id = request.POST.get('empid')
    employee.employee_name = request.POST.get('empname')
    employee.salary = request.POST.get('salary')
    employee.experience = request.POST.get('exp')
    employee.location = request.POST.get('loc')
    employee.save()
    return redirect('main_page')

def delete_data(request,id):
    employee = EmployeeData.objects.get(id=id)
    employee.delete()
    return redirect('main_page')
