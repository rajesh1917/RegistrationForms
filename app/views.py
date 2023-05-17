from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.forms import *

def registration(request):

    ufo=UserForm()
    pfo=ProfileForm()

    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            #not saved user object
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()

            #not saved profile object

            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
    
            return HttpResponse('Data is submitted successfully')
        else:
            return HttpResponse('Invalid Data')
        
    return render (request,'registration.html',d)