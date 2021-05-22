# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connections

from django.db import models
import mysql.connector
# Create your models here.
from datetime import date
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField




class customer(models.Model):
  create = models.DateField(auto_now_add=True,null=True)
  Arabicname = models.CharField(max_length=45)
  
  Englishname = models.CharField(max_length=45,null=True)
  
  email =models.EmailField(null=True)
  service =models.CharField(max_length=45, null=True)
  bundle =models.CharField(max_length=45, null=True)
  speed =models.CharField(max_length=45, null=True)
  period =models.CharField(max_length=45, null=True)
  SecondaryEmail1 =models.EmailField(null=True)
  SecondaryEmail2 =models.EmailField(null=True)
  mobile = models.CharField(max_length=45)
  SecondaryMobile1 = models.CharField(max_length=45,null=True)
  SecondaryMobile2 = models.CharField(max_length=45,null=True)
  Fax = models.CharField(max_length=45,null=True)
  Nationality = models.CharField(max_length=45)
  city = models.CharField(max_length=45)
  username = models.CharField(max_length=45,primary_key=True)
  identity = models.CharField(max_length=45, null=True)
  address  =models.CharField(max_length=45)
  status = models.CharField(max_length=45,default='Activation')
  update = models.CharField(null=True,max_length=45)
  emergency =models.CharField(null=True,max_length=45)
  emergencycount =models.IntegerField(default=0,null=True)
  usercustomer = models.CharField(max_length=45,null=True)
  street = models.CharField(max_length=45,null=True)
  pointing =models.CharField(max_length=45,null=True)
  payment_total = models.CharField(max_length=45,null=True)
  #class Meta:
        #default_permissions = ('add',)
       # permissions = (('can_show_customer','Can show customer'),)

  

class note(models.Model):
  id = models.AutoField(primary_key=True)
  notename =models.CharField(max_length=45,null=True)
  notedate=models.CharField(max_length=45,null=True)
  new_status=models.CharField(max_length=45,null=True)
  report = models.ForeignKey(customer, on_delete=models.CASCADE,null=True)
  usernote = models.CharField(max_length=45,null=True)

class general_note(models.Model):
  id = models.AutoField(primary_key=True)
  generalname =models.CharField(max_length=45,null=True)
  generaldate=models.CharField(max_length=45,null=True)
  generalreport = models.ForeignKey(customer, on_delete=models.CASCADE,null=True)
  usergeneral = models.CharField(max_length=45,null=True)


class edit_note(models.Model):
  id = models.AutoField(primary_key=True)
  editname =models.CharField(max_length=45,null=True)
  editdate=models.CharField(max_length=45,null=True)
 
  editreport = models.ForeignKey(customer, on_delete=models.CASCADE,null=True)
  useredit = models.CharField(max_length=45,null=True)  

from django.db import models

class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class ticket(models.Model):
  id = models.AutoField(primary_key=True)
  tickname =models.CharField(max_length=45,null=True)
  tickdate=models.CharField(max_length=45,null=True)
  tickreport = models.ForeignKey(customer, on_delete=models.CASCADE,null=True)
  tickstatus = models.CharField(max_length=45,default='open')
  close =models.CharField(max_length=45,null=True)
  closedate=models.CharField(max_length=45,null=True)
  useradd = models.CharField(max_length=45,null=True)
  userclose = models.CharField(max_length=45,null=True)
  ticktype = models.CharField(max_length=45,null=True)
  ticksub = models.CharField(max_length=45,null=True)

class replay(models.Model):
  id = models.AutoField(primary_key=True)
  id1 =models.CharField(max_length=45,null=True)
  replaybody =models.CharField(max_length=45,null=True)
  replaydate=models.CharField(max_length=45,null=True)
  replayreport = models.ForeignKey(ticket, on_delete=models.CASCADE,null=True)
  userreplay = models.CharField(max_length=45,null=True)

  


class bills(models.Model):
 id=models.AutoField(primary_key=True)
 billcoast=models.IntegerField(default=1,null=True)
 billdate=models.CharField(max_length=45, null=True)
 cusbill=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
 billstat=models.CharField(max_length=45,default='Unpaid')
 userbill = models.CharField(max_length=45,null=True)
 userpaid = models.CharField(max_length=45,null=True)
 credit =models.CharField(max_length=45,null=True)
 creditdate=models.CharField(max_length=45,null=True)
 usercredit  =models.CharField(max_length=45,null=True)
 startdate = models.DateTimeField(auto_now_add=False,null=True)
 enddate = models.DateTimeField(auto_now_add=False,null=True)
 instalment=models.CharField(max_length=45,null=True)
 billc = models.CharField(max_length=45,null=True)
 prom = models.CharField(max_length=45,null=True)


class payment(models.Model):
 id=models.BigAutoField(primary_key=True)
 payment=models.IntegerField(null=True)
 paiddate = models.CharField(max_length=45,null=True)
 userpaid = models.CharField(max_length=45,null=True)
 billid = models.CharField(max_length=45,null=True)
 cuspaid=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)

class promotions(models.Model):
  monthnum = models.CharField(max_length=45,null=True)
  cusprom = models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
  userprom = models.CharField(max_length=45,null=True)
  prodate = models.CharField(max_length=45,null=True)
  billid = models.CharField(max_length=45,null=True)


class vas(models.Model):
  sname = models.CharField(primary_key=True,max_length=45)
  scoast = models.IntegerField(default=100)
class vas1(models.Model):
  id = models.AutoField(primary_key=True)
  sname1 = models.CharField(max_length=45)
  vasstat = models.CharField(max_length=45,null=True)
  vasreport = models.ForeignKey(customer, on_delete=models.CASCADE,null=True)
  vstartdate = models.CharField(max_length=45,null=True)
  venddate = models.CharField(max_length=45,null=True)
  uservas = models.CharField(max_length=45,null=True)
  billid = models.CharField(max_length=45,null=True)


class employee1(models.Model):
  eid = models.CharField(max_length=45)
  ename = models.CharField(max_length=45)
  vacation= models.CharField(max_length=45)
  worktime = models.TimeField(default='8:00')
  endtime = models.TimeField(default='16:00')

class vacations(models.Model):
  vdate = models.CharField(max_length=45)
  evdate=models.ForeignKey(employee1,on_delete=models.CASCADE,null=True)

  
  
  

