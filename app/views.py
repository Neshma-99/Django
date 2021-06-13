
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
#render,
def Employee_list(request):
    context={'employee_list':Employee.objects.all()}
    return render(request,"list.html",context)


def Employee_form(request):
    form = EmployeeForm()
    if request.method == "POST":
        
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list/')    
    return render(request,"form.html",{'form':form})


def update(request,id):
    if request.method == "POST":
     form = Employee.objects.get(pk=id)
     form = EmployeeForm(request.POST,instance=form)
     if form.is_valid():
            form.save()
            return redirect('/list/')
    else:      
     form = Employee.objects.get(pk=id)
     form = EmployeeForm(instance=form)
     
    return render(request,"update.html",{'form':form})


def delete(request,id):
    if request.method == "POST":
      form = Employee.objects.get(pk=id)
      form.delete()
      return redirect('/list/')
    #return render(request,"list.html")


    




   

