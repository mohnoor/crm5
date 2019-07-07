# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connections
from django.contrib.auth.models import User

from django.db import models
import mysql.connector
# Create your models here.


class serves(models.Model):
  sname = models.CharField(max_length=45, primary_key=True)
  scoast = models.IntegerField(default=100)
  


class custumer(models.Model):
  username = models.CharField(max_length=45, primary_key=True)
  fname = models.CharField(max_length=45, primary_key=True)
  lname = models.CharField(max_length=45)
  identity = models.IntegerField(default=True)
  mobile = models.IntegerField(default=True)
  address = models.CharField(max_length=45)
  cserve = models.ForeignKey(serves,default=True, on_delete=models.CASCADE)







class emploeey(models.Model):
  eid = models.IntegerField(default=100)
  efname = models.CharField(max_length=45)
  elname = models.CharField(max_length=45)
  esalary = models.IntegerField(default=170)
  epassword = models.CharField(max_length=45)
  edateofharing = models.CharField(max_length=45)
  
  
  
  