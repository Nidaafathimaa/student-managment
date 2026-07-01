from django.shortcuts import render,redirect
from . models import Student

def home(request):
    item=Student.objects.all()
    if request.method=='POST':
        a=request.POST.get('user')
        b=request.POST.get('user-age')
        Student.objects.create(name=a,age=b)
        return redirect('home')
    return render(request,'index.html',{'item':item})
def index(request):
    return render(request,'index.html')

def delete_Student(request,id):
    items=Student.objects.filter(id=id)
    items.delete()
    return redirect('home')
def update_Student(request,id):
    items=Student.objects.get(id=id)
    if request.method=='POST':
        items.name=request.POST.get('user')
        items.age=request.POST.get('user-age')
        items.save()
        return redirect('home')
    return render(request,'update.html',{'items':items})    
    
