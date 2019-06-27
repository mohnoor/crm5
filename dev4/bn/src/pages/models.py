# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connections

from django.db import models
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="@M681755ma",
  database="crm",

)
# Create your models here.


n = mydb.cursor()

n.execute("SELECT username FROM pages_custumer")

c= n.fetchall()

for x in c:
  print(x)
class custumer(models.Model):
  username = models.IntegerField(default=100)
  fname = models.CharField(max_length=45)
  lname = models.CharField(max_length=45)
  speed = models.IntegerField(default=170)
  bundel = models.CharField(max_length=45)
  
class paid(models.Model):
  pamount = models.IntegerField(default=100)
  pdate = models.DateField(max_length=45)

class bills(models.Model):
  bfrom = models.IntegerField(default=100)
  to = models.CharField(max_length=45)
  amount = models.CharField(max_length=45)

class emploeey(models.Model):
  eid = models.IntegerField(default=100)
  efname = models.CharField(max_length=45)
  elname = models.CharField(max_length=45)
  esalary = models.IntegerField(default=170)
  epassword = models.CharField(max_length=45)
  edateofharing = models.CharField(max_length=45)
  
  
  
  