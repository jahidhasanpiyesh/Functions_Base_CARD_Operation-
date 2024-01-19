from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForms
from .models import User
# Create your views here.
def addandshow(request):
    if request.method == 'POST':
        F = StudentForms(request.POST)
        if F.is_valid():
            F.save()
        F = StudentForms() 
    else:
        F = StudentForms() 
    data = User.objects.all()
    return render(request, 'cardapp/addandshow.html',{'fm': F,'show': data})

def remove(request, id):
    if request.method == 'POST':
        R = User.objects.get(pk = id)
        R.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    if request.method == 'POST':
        U = StudentForms(request.POST)
        P = User.objects.get(pk = id)
        U = StudentForms(request.POST, instance = P)
        if U.is_valid():
            U.save()
    else:
        Z = User.objects.get(pk = id)
        U = StudentForms(instance = Z)
    return render(request,'cardapp/update.html',{'update': U})