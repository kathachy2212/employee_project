from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import Http404

# Create your views here.

def employee_list(request) :
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)


def employee_form(request,id=0) :
    if request.method == "GET" :
        if id == 0 :
            form = EmployeeForm()
        else :
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request, 'employee_register/employee_form.html', {'form' : form})
    else :
        if id == 0 :
            form = EmployeeForm(request.POST)
        else :
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee)
            
         
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


# def employee_form(request, id=0):
#     if request.method == "GET":
#         if id == 0:  # if no ID is provided, create a new form
#             form = EmployeeForm()
#         else:
#             try:
#                 employee = Employee.objects.get(pk=id)  # use the id parameter passed in URL
#                 form = EmployeeForm(instance=employee)
#             except Employee.DoesNotExist:
#                 raise Http404("Employee not found")  # Handle the case where the employee doesn't exist
#         return render(request, 'employee_register/employee_form.html', {'form': form})
#     else:
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/employee/list')
#         return render(request, 'employee_register/employee_form.html', {'form': form})
   


def employee_delete(request,id) :
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')