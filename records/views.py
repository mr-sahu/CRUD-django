from django.shortcuts import render,HttpResponseRedirect
from .forms import Regtab
from .models import UserRegistration
# Create your views here.
def add(request):
    if request.method=='POST':
        fm=Regtab(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pas=fm.cleaned_data['password']
            cou=fm.cleaned_data['country']
            fm=Regtab()
            ft=UserRegistration(name=nm,email=em,password=pas,country=cou)
            ft.save()
    else:
        fm=Regtab()
    return render(request,'records/home.html',{'forms':fm})

def showuser(request):
    mt=UserRegistration.objects.all()
    return render(request,'records/show_data.html',{'data':mt})

def delete_data(request,id):
    if request.method=='POST':
        dt=UserRegistration.objects.get(pk=id)
        dt.delete()
        return HttpResponseRedirect('/')
    
##update
def update_data(request,id):
    if request.method=='POST':
        mt=UserRegistration.objects.get(pk=id)
        fm=Regtab(request.POST,instance=mt)
        if fm.is_valid():
            saved=fm.save()
            
    else:
        mt=UserRegistration.objects.get(pk=id)
        fm=Regtab(instance=mt)
    return render(request,'records/update.html',{'form':fm})
