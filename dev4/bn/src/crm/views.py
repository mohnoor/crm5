# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector
from django.http import HttpResponse
from .models import custumer
from .models import serves
from django.contrib.auth import authenticate, login
#from .forms import UsersLoginForm
from django.db.models import Q
from django.views.generic import TemplateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import n



def f(request,id):
    d=custumer.objects.get(username=id)

    context = {
        f : d,
    }
    return render(request,'search.html',context)    


def  home_view(request, *args, **kwargs):
    if request.method == 'GET':
        print(args, kwargs)
        print(request)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            port_number = request.META['SERVER_PORT']
        return render(request,'home.html',{'ip':ip,'port':port_number})
    
           
    else:
        return render(request,"base.html")
	
def custumer_view(request):
    if request.method == 'GET':
        query= request.GET.get('username') 

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(fname__icontains=query) 
            results= custumer.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request,"custumer.html", context)

        else:
            return render(request, "custumer.html")

    else:
        return render(request, "custumer.html")

def delete_view(request):
    if request.method == 'GET':    
   
        query= request.GET.get('username')

        
        if query is not None:
            lookups= Q(username__icontains=query) 

            results= custumer.objects.filter(lookups).delete()
    
            context= {'results': results
              }
    
            return render(request, "home.html",context)
        else:
            return render(request, "home.html")
    else:
        return render(request, "home.html")

def edit_view(request):
    
    if request.method == 'GET':    
   
        query= request.GET.get('username')

        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(username__icontains=query) 
           
            results= custumer.objects.filter(lookups).update()
    
            context= {'results': results,'submitbutton': submitbutton
              }
    
            return render(request, "edit.html",context)
        else:
            return render(request, "edit.html")
    else:
        return render(request, "edit.html")   
    return render(request, "edit.html")             

def add_serves(request):
    if request.method == 'post':

        if request.post.get('username'):
            b =custumer()
            b.cserve=request.post.get('cserve')
            b.save()
        return render(request, "addserves.html", {})
    else:
        return render(request, "addserves.html", {})    


def show_serves(request):
    hh= serves.objects.all()
    context = {
    
        'hh': hh
        }
    return render(request, 'addserves.html', context)
    


    if request.method == 'GET1':
        query= request.GET.get('username')

        submitbutton= request.GET.get('submit1')

        if query is not None:
            lookups= Q(username__icontains=query) 

            g= custumer.objects.filter(lookups).distinct()

            context={'g': g,
                     'submitbutton': submitbutton}

            return render(request, "addserves.html", context)

        else:
            return render(request, "addserves.html")

    else:
        return render(request, "addserves.html")

	
def emplog(request, *args, **kwargs):

	return render(request)


def search_view(request):
    if request.method == 'GET':
        query= request.GET.get('username') 

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(username__icontains=query) 
            results= custumer.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request,"search.html", context)

        else:
            return render(request, "search.html")

    else:
        return render(request, "search.html")

def new_custumer(request):
    if request.method == 'POST':
        form = n(request.POST)
        form.save()

        
    
    else:
        form = n()
    context = {

        'form' : form ,

    
    }    
    return render(request,"new_custumer.html", context)
        

def edit(request):  
    if request.method == 'GET2':
        query= request.GET.get('username')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(username__icontains=query) 

            results1= custumer.objects.filter(lookups).distinct()

            context={'results1': results1,'submitbutton': submitbutton}
  

            return render(request, "edit.html", context)

        else:
            return render(request, "edit.html")

    else:
        return render(request, "edit.html")



def new_serves(request, *args, **kwargs):
    if request.method == 'POST':
        if request.POST.get('sname'): 
	        new =serves()
	        new.sname=request.POST.get('sname')
	        new.scoast=request.POST.get('scoast')
	        

	        new.save()
        return render(request, "add_newserves.html", {})
    else:
        return render(request, "add_newserves.html", {})
      




