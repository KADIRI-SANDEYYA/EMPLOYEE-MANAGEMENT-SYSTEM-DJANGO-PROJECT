from django.shortcuts import render, redirect
from application.forms import EmployeeForm
from application.models import EmployeeModel
from django.db.models import Sum




def employee_list(request):
    employee_data = EmployeeModel.objects.all()
    total_employees = EmployeeModel.objects.count()
    total_departments = EmployeeModel.objects.values('department').distinct().count()
    monthly_payroll = EmployeeModel.objects.aggregate(total_salary=Sum('salary'))['total_salary'] or 0
    monthly_payroll = round(monthly_payroll/100000)
    return render(
        request,
        'employee_list.html',
        {
            'employee_data': employee_data,
            'total_employees': total_employees,
            'total_departments': total_departments,
            'monthly_payroll': monthly_payroll,
        }
    )



def employee_form(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    return render(request,'employee_form.html',{'form': form})



def update_record(request,pk):
    update_data = EmployeeModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES,instance=update_data)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmployeeForm(instance=update_data)
        return render(request,'employee_form.html',{'form':form})



def delete_record(request,pk):
    delete_data = EmployeeModel.objects.get(pk=pk)
    delete_data.delete()
    return redirect('emp_list')



def card_details(request,pk):
    employee = EmployeeModel.objects.get(pk=pk)
    return render(request,'employee_card.html',{'employee':employee})