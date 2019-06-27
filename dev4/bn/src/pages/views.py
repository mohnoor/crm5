# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
from django.http import HttpResponse
from .models import custumer


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="@M681755ma",
  database="crm",

)
# Create your views here.
#for p in custumer.objects.raw('SELECT username FROM pages_custumer'):
#	print(p)
def  home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request)
	return render(request, "home.html", {})
	

def contact_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request)
	
	
	return render(request, "contact.html", {})
	
def emplog(request, *args, **kwargs):

	return render(request, "emplog.html", {})



def search(request, *args, **kwargs):
	return render(request, "search.html", {})
def new_custumer(request, *args, **kwargs):
   # entry = custumer.objects.get(username)
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname'):
	        new =custumer()
	        new.fname=request.POST.get('fname')
	        new.lname=request.POST.get('lname')
	        new.save()
        return render(request, "newcustumer.html", {})
    else:
        return render(request, "newcustumer.html", {})
       

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



