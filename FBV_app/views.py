from django.http.response import HttpResponse, HttpResponseRedirect
from FBV_app.models import User
from FBV_app.forms import UserInfoForm
from django.shortcuts import render

# Create your views here.
def display(request):
    if request.method=='POST':
        fm=UserInfoForm(request.POST, request.FILES)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            mob=fm.cleaned_data['mob_number']
            img=fm.cleaned_data['image']

            obj=User(name=nm,email=em,mob_number=mob,image=img)
            obj.save()
            fm=UserInfoForm()
    else:
        fm=UserInfoForm()
    std=User.objects.all()
    return render(request,'FBV_app/display.html',{'form':fm,'std':std})

def update_data(request,id):
    std=User.objects.get(pk=id)
    if request.method=='POST':
        fm=UserInfoForm(request.POST,request.FILES,instance=std)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm=UserInfoForm(instance=std)
        return render(request,'FBV_app/update.html',{'form':fm,'id':id})

def delete_data(request,id):
    if request.method=='POST':
        std=User.objects.get(pk=id)
        std.delete()
        return HttpResponseRedirect('/')