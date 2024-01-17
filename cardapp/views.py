from django.shortcuts import render,HttpResponseRedirect
from .forms import formsdata
from .models import User
# Create your views here.

# This Function will Add new items/data and Show all items/data
def cardapp(request):
    if request.method == 'POST':
        S = formsdata(request.POST)
        if S.is_valid():
            # Sort Way data Save ()
            S.save()
            
            # From data submit then blank froms 
            S = formsdata()
            # # one one Data gat and Cleand data Save format 
            # nm = S.cleaned_data['name']
            # em = S.cleaned_data['email']
            # pw = S.cleaned_data['password']
            # save_data =User(name=nm,email=em,password=pw)
            # save_data.save()               
    else:
        S = formsdata()
        
    all_data = User.objects.all()
    return render(request,'cardapp/addandshow.html',{'from':S,'data':all_data})


# Thid Fucntion will Edit Items
def update_data(request, id):
    return render(request,'cardapp/updatedata.html',{'id':id})

# This Function will Remove Items
def remove_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')