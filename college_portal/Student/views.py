from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table
# Create your views here.
def home(request):
    data1={
        'name':"abc",
        'age':17,
        'department':"BCA"
    }
    marks=[100,98,97]
    return render(request,'home.html',{'data1':data1 ,'marks1':marks })
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def forms1(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        name=request.POST.get('name')
        marks=request.POST.get('marks')
        email=request.POST.get('email')
        
        Student_table.objects.create(reg_no=reg_no,name=name,email=email,marks=marks)
        return HttpResponse("saved successfully")
    return render(request,'Student_form.html')

