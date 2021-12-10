from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .form import Employeeupdate
# Create your views here.

def home(request):
    obj = Employee.objects.all()
    form = Employeeupdate()
    if request.method == "POST":
        form = Employeeupdate(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    return render(request, "index.html",{"obj":obj,"form":form})

# table delete query
def tabledelete(request,pk):

    getpro = Employee.objects.get(pk=pk)
    getpro.delete()
    return redirect('home')

def tableupdate(request,pk):

    getemployee = Employee.objects.get(pk=pk)

    form = Employeeupdate(request.POST or None,instance=getemployee)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request,"tableupdate.html",{"form":form})

def tablecreate(request,pk):

    form = Employeeupdate(request.POST)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request,"tablecreate.html",{"form":form})



