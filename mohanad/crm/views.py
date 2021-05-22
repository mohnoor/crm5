# -*- coding: utf-8 -*-
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector
from django.http import HttpResponse
from .models import customer,vas,note,bills,ticket,replay,vas1,edit_note,payment,employee1,vacations,general_note,promotions
from django import forms
#from .forms import UsersLoginForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404,reverse
from admin_view_permission.admin import AdminViewPermissionAdminSite
from dateutil.relativedelta import relativedelta

from django.http import HttpResponseRedirect
from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta,date

date_string = datetime.strftime(timezone.now(), '%Y-%m-%d %H:%M:%s')
from bootstrap4.widgets import RadioSelectButtonGroup
from django.test import TestCase, override_settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .mixins import AjaxTemplateMixin
from django.core.mail import send_mail

def home_view(request):
    

    if request.user.is_authenticated():
        query= request.GET.get('username') 
        submitbutton= request.GET.get('submit')


            
            
        

        lookups= Q(username=query)
           
            
            
            
        lookups1= Q(status='Activation')
        lookups2= Q(status='Billing')
        lookups3= Q(status='Pending')
            
        results= (customer.objects.filter(lookups1))
        results2= (customer.objects.filter(lookups2))
        results3= (customer.objects.filter(lookups3))
        context={'results': results,'results2': results2,'results3': results3,
                         'submitbutton': submitbutton}

        return render(request, 'home.html',context)
        
            
    else:

        return redirect('login')


def search_view(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('username')
        submitbutton= request.GET.get('submit')
        
        

            
            

        if  not query:
            return render(request,"home.html")

        
        else:   
            if request.GET.get('field')=='username':            
                
            
                
            
                lookups=Q(username__icontains=query)
                results= customer.objects.filter(lookups).distinct()
                context={'results': results,
                'submitbutton': submitbutton}
            
        
                return render(request,"search.html", context)
            elif request.GET.get('field')=='identity':
                lookups=Q(identity__icontains=query)
                results= customer.objects.filter(lookups).distinct()
                context={'results': results,
                'submitbutton': submitbutton}
                return render(request,"search.html", context) 
            elif request.GET.get('field')=='mobile':
                lookups=Q(mobile__icontains=query)
                results= customer.objects.filter(lookups).distinct()
                context={'results': results,
                'submitbutton': submitbutton}
                return render(request,"search.html", context) 
            elif request.GET.get('field')=='email':
                lookups=Q(email__icontains=query)
                results= customer.objects.filter(lookups).distinct()
                context={'results': results,
                'submitbutton': submitbutton}
                return render(request,"search.html", context) 
            elif request.GET.get('field')=='arabic_name':
                lookups=Q(Arabicname__icontains=query)
                results= customer.objects.filter(lookups).distinct()
                context={'results': results,
                'submitbutton': submitbutton}
                return render(request,"search.html", context) 
            elif request.GET.get('field')=='Name':
                lookups=Q(Englishname__icontains=query)
                results= customer.objects.filter(lookups).distinct()
                context={'results': results,
                'submitbutton': submitbutton}
                return render(request,"search.html", context)     

            else:
                return render(request,"search.html", {}) 
        
                    
             
            

          
          
               


   
    else:
        
        return redirect('login')


        









def all(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('username') 
            

        submitbutton= request.GET.get('submit')
        
        if query is not None:
            lookups= Q(username__icontains=query) 
            results= customer.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request,"all.html", context)
    else:
        return redirect('login')

            



def customer_view(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('username') 
        submitbutton= request.GET.get('submit')


        #cos= general_note.objects.all().delete()
        #cos1= edit_note.objects.all().delete()
        #cos2= note.objects.all().delete()
            
        if query is not None:

            lookups= Q(username=query)
            if customer.objects.filter(lookups).distinct():   
                results= customer.objects.filter(lookups).distinct()
            else:
                return render(request, "home.html",{})      
            
            
            
            lookups1= Q(report__username=query)
            lookups2= Q(tickreport__username=query)
            lookupspaid= Q(cuspaid__username=query)
            lookupsbill= Q(cusbill__username=query)
            lookups3= Q(vasreport__username=query)
            lookups4= Q(editreport__username=query) 
            lookups5= Q(generalreport__username=query) 
            results4= reversed(edit_note.objects.filter(lookups4))
            lookups7= Q(cusprom__username=query) 
            results7= reversed(promotions.objects.filter(lookups7))
            results5= reversed(general_note.objects.filter(lookups5))
            results3= vas1.objects.filter(lookups3).order_by('vasstat')
            results1= reversed(note.objects.filter(lookups1))
            results2= reversed(ticket.objects.filter(lookups2).distinct())
            query1=(ticket.objects.filter(lookups2).distinct())
            resultsreplay= (replay.objects.all())
            insresults=reversed(payment.objects.filter(lookupspaid))

            resultsbill= reversed(bills.objects.filter(lookupsbill))
            diff4=bills.objects.filter(lookupsbill).aggregate(Sum('billcoast'))['billcoast__sum']
            diff5= bills.objects.filter(lookupsbill).aggregate(Sum('instalment'))['instalment__sum']
            diff6=F('billcoast')-F('instalment') 
            new = customer.objects.get(username=query)
            new.payment_total=diff5
   
                
            context={'results': results,'results1': results1,'resultsreplay': resultsreplay,'results2': results2,'resultsbill':resultsbill,
                    'results5': results5,'results7':results7,'results4': results4,'insresults':insresults,'results3': results3,'diff6':diff6,'diff4':diff4,'diff5':diff5, 'submitbutton': submitbutton}
            
                              
                           
            if request.method == 'POST':
                 
                if request.POST.get('Emailb') is not None:
                    if request.POST.get('Email'):
                        send_mail(
                        'Welcome',
                        request.POST.get('Emailb'),
                        'crm11728@gmail.com',
                        [request.POST.get('Email')],
                        fail_silently=False,
                        ) 
                        new = customer.objects.get(username=query)
                        newgen= general_note()
                        newgen.generalreport= new
                        newgen.generalname=request.POST.get('generalname')
                        newgen.usergeneral=request.POST.get('usergeneral')
                        newgen.generaldate=timezone.now().replace(microsecond=0)
                        newgen.save()
                        messages.success(request, 'Email sent successfully.')
                        messages.set_level(request, messages.SUCCESS)

                        return redirect(request.META['HTTP_REFERER'])

                    else:
                        messages.error(request, 'The customer dont have Email.')
                        messages.set_level(request, messages.ERROR)

                        return redirect(request.META['HTTP_REFERER'])    

                if request.POST.get('username'):
                   
                    
                    new = customer.objects.get(username=query)
                    
                    ticket.objects.filter(id=request.POST.get('close')).update(tickstatus=request.POST.get('tickstatus'),closedate=timezone.now().replace(microsecond=0),userclose=request.POST.get('userclose'))
                    vas1.objects.filter(id=request.POST.get('vasdis')).update(vasstat=request.POST.get('vasstat'),venddate=timezone.now().replace(microsecond=0))


                    new3=ticket()
                    new4=bills()
                    new1=note()
                    new5=replay()
                    newgen= general_note()
                    new3.tickreport= new
                    
                    
                    
                    if request.POST.get('generalemer') is not None:
                        newgen.generalreport= new

                        newgen.generalname=request.POST.get('generalname')+request.POST.get('emergency')
                        newgen.generaldate=timezone.now().replace(microsecond=0)
                        newgen.usergeneral=request.POST.get('usergeneral')
                        newgen.save()
                        

                    

                    new1.report= new
                    
                    new5.replaybody=request.POST.get('replaybody')
                    
                    
                    new3.tickst=request.POST.get('tickst')
                    new3.tickname=request.POST.get('tickname')
                    new3.tickstatus=request.POST.get('tickstatus')
                    new3.useradd=request.POST.get('useradd')
                    new3.tickdate=timezone.now().replace(microsecond=0)
                    new3.ticktype=request.POST.get('ticktype')
                    new3.ticksub=request.POST.get('ticksub')
                    
                    new1.notename=request.POST.get('notename')
                    new1.usernote=request.POST.get('usernote')
                    new1.new_status=request.POST.get('status')
                    
                    new1.notedate=timezone.now().replace(microsecond=0)
                    if request.POST.get('status') == 'Active':
                        new.emergencycount=0
                    elif request.POST.get('status') == 'Emergency':   
                        
                        new.emergencycount=int(request.POST.get('emergencycount'))+1
                    else:
                        new.emergencycount=new.emergencycount
                        

                    

                    new.update=timezone.now().replace(microsecond=0)
                    if  request.POST.get('emergency') is not None:
                        new.emergency=request.POST.get('emergency') 
                    else:
                        new.emergency=new.emergency
                        
                    if  request.POST.get('status') is not None:
                        new.status=request.POST.get('status')    
                        new.save()

                        
                       
                    
                    
                    
                    if new5.replaybody is not None:
                        new9 = ticket.objects.get(id=request.POST.get('close'))  
                        new5.replayreport=new9
                        new5.replaydate=timezone.now().replace(microsecond=0)
                        new5.userreplay=request.POST.get('userreplay')
                        new5.save()
                        return redirect(request.META['HTTP_REFERER'])
                    if new1.notename is not None:
                        new1.save()
                        return redirect(request.META['HTTP_REFERER'])
                    if new3.tickname is not None:
                        if new3.tickname:
                            new3.save()
                            return redirect(request.META['HTTP_REFERER'])

                    
                    new4.save()
                    
                    return redirect(request.META['HTTP_REFERER'])
            return render(request, "customer.html", context) 
         




        
            return render(request, "customer.html", {})
       

    else:
        
       return redirect('login')
              



#from djsms import send_text
import json

    
 #   djsms.send_text(text, +970592320020,+970598892373 , fail_silently=True, status_report=False)
def no(request):
 #   djsms.send_text(text, +970592320020,+970598892373 , fail_silently=True, status_report=False)

    query= request.GET.get('username') 
    submitbutton= request.GET.get('submit')
    lookups2= Q(cuspaid__username=3)
    results1= vacations.objects.all()
    
    context={'results1': results1,'submitbutton': submitbutton}
    


    return render(request,"no.html",context)
from django.shortcuts import render
from django.http import JsonResponse
from .models import Post



def advert(request):
    if request.method == "POST":
        form = AdvertForm(request.POST)

        message = 'something wrong!'
        if(form.is_valid()):
            print(request.POST['title'])
            message = request.POST['title']

        return HttpResponse(json.dumps({'message': message}))

    return render_to_response('contact/advert.html',
            {'form':AdvertForm()}, RequestContext(request))
def newbill(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('username') 
        submitbutton= request.GET.get('submit')


            
            
        if query is not None:
            lookups= Q(username__icontains=query)
            
            results= customer.objects.filter(lookups).distinct()
            
            lookupsbill= Q(cusbill__username=query)
        
            resultsbill= reversed(bills.objects.filter(lookupsbill))
            context={'resultsbill':resultsbill,'results':results,
                    'submitbutton': submitbutton}
            if request.method == 'POST':
               

                if request.POST.get('username'):
                    new = customer.objects.get(username=query)
                    new3=bills()
                    new3.cusbill=new
                    new3.billcoast=request.POST.get('billcoast')
                    new3.billstat='Unpaid'
                    new3.userbill=request.POST.get('userbill')
                    new3.billdate=timezone.now().replace(microsecond=0)
                    new3.startdate=request.POST.get('startdate')
                    new3.enddate=request.POST.get('enddate')
                    
                    new3.instalment='0'
                    new3.prom='0'

                    if new3.billcoast is not None :
                        new3.save()
                    return redirect(request.META['HTTP_REFERER'])
                    
            return render(request, "newbill.html", context) 

        else:
            return render(request, "newbill.html", {})
    else:
        
       return redirect('login')
from django.db.models import Sum
from django.db.models import Count,Avg,Sum,F

def prom(request):
    if request.user.is_authenticated():
        query= request.GET.get('username')
        query1= request.GET.get('id')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups=Q(username__icontains=query)
            results=customer.objects.filter(lookups).distinct()
            lookups1=Q(cusbill=query)
            results1=bills.objects.filter(lookups1).order_by('-id')[0]
            if results1.billcoast == '168':

                context={'results': results,'results1': results1,
                            'submitbutton': submitbutton}
            else:
                results1=bills.objects.filter(lookups1).order_by('-id')[1]
                context={'results': results,'results1': results1,
                            'submitbutton': submitbutton}
                            

            
            if request.method == 'POST':
                new = customer.objects.get(username=query)
                new2 =promotions()
                new2.billid=request.POST.get('billid') 
                new2.cusprom =new
                new2.monthnum=request.POST.get('monthnum')
                new2.userprom=request.POST.get('userprom')
                new2.prodate=timezone.now().replace(microsecond=0)
                
                r=bills.objects.get(id=request.POST.get('billid'))

                if r.prom == '2':
                    messages.add_message(request, messages.INFO, 'The customer already have promotions!.')

                else:
                    if request.POST.get('monthnum') == 'One Free Month':
                        if r.prom == '1':
                            bills.objects.filter(id=request.POST.get('billid')).update(prom=2,enddate=r.enddate + relativedelta(months=1))
                            messages.add_message(request, messages.INFO, 'Promotion added successfully.')
                            new2.save()

                        elif r.prom == '0':
                            bills.objects.filter(id=request.POST.get('billid')).update(prom=1,enddate=r.enddate + relativedelta(months=1))
                            messages.add_message(request, messages.INFO, 'Promotion added successfully.')
                            new2.save()
                    elif request.POST.get('monthnum') == 'Two Free Month':
                        if r.prom == '1' :  
                            messages.add_message(request, messages.INFO, 'The customer already have One Free Month  promotions!.')
                        elif r.prom == '0': 
                            bills.objects.filter(id=request.POST.get('billid')).update(prom=2,enddate=r.enddate + relativedelta(months=2))
       
                            messages.add_message(request, messages.INFO, 'Promotion added successfully.')
                            new2.save()


                return redirect(request.META['HTTP_REFERER'])            
            

            return render(request, "promotions.html",context) 
    else:
        return redirect('login')

def paid(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('id') 
        query1= request.GET.get('username') 
        submitbutton= request.GET.get('submit')
        lookupsbill= Q(cusbill__username=query1)

        diff5= bills.objects.filter(lookupsbill).aggregate(Sum('instalment'))['instalment__sum']

        
        lookups= Q(id__icontains=query) 
        
        results= bills.objects.filter(lookups).distinct()
        lookups1= Q(cusbill__username=query1) 
        
        results1= bills.objects.filter(lookups1).distinct()
       
        context={'results': results,'results1': results1,
                         'submitbutton': submitbutton}



            
            

      
        if request.method == 'POST':
            new = bills.objects.get(id=query) 
            new3 = customer.objects.get(username=query1)
            new2 =payment()
            new2.cuspaid=new3
            new2.payment=request.POST.get('instalment')
            new2.userpaid=request.POST.get('userpaid')
            new2.billid=request.POST.get('billid')
            new2.paiddate=timezone.now().replace(microsecond=0)
            if new2.payment is not None:
                new2.save()


            instalment1= int(request.POST.get('instalment'))+int(request.POST.get('instalment2'))
            if (diff5 + instalment1)  >= 1000 and (diff5 + instalment1) <= 3000:
                customer.objects.filter(username=request.POST.get('cususer')).update(pointing='Silver')
            elif (diff5 + instalment1) >= 3000 and (diff5 + instalment1) <= 6000: 
                customer.objects.filter(username=request.POST.get('cususer')).update(pointing='Gold')
            elif (diff5 + instalment1) >= 6000 and (diff5 + instalment1) <= 10000:     
                customer.objects.filter(username=request.POST.get('cususer')).update(pointing='Platinum')
            elif (diff5 + instalment1) >= 10000 :
                customer.objects.filter(username=request.POST.get('cususer')).update(pointing='Diamond')
 
            bills.objects.filter(id=request.POST.get('billid')).update(instalment=instalment1,userpaid=request.POST.get('userpaid'))
            if instalment1 == new.billcoast :
                bills.objects.filter(id=request.POST.get('billid')).update(billstat="Paid")
            return redirect(request.META['HTTP_REFERER'])
        return render(request, "paid.html",context) 

   
    else:
        
        return redirect('login')

def credit(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('id') 
        query1= request.GET.get('username') 
        submitbutton= request.GET.get('submit')
        lookupsbill= Q(cusbill__username=query1)


        
        lookups= Q(id__icontains=query) 
        
        results= bills.objects.filter(lookups).distinct()
        lookups1= Q(cusbill__username=query1) 
        
        results1= bills.objects.filter(lookups1).distinct()
       
        context={'results': results,'results1': results1,
                         'submitbutton': submitbutton}



            
        new = bills.objects.get(id=327) 

        if request.method == 'POST':
            if  new.billcoast == (request.POST.get('credit')):
                bills.objects.filter(id=request.POST.get('billid')).update(billstat="55")


            
            bills.objects.filter(id=request.POST.get('billid')).update(credit=request.POST.get('credit'),usercredit=request.POST.get('usercredit'),creditdate=timezone.now().replace(microsecond=0))
            
            return redirect(request.META['HTTP_REFERER'])
        return render(request, "credit.html",context) 

   
    else:
        
        return redirect('login')



def edit_view(request, *args, **kwargs):
    if request.user.is_authenticated():

        query= request.GET.get('username') 
            
        

        submitbutton= request.GET.get('submit')
        
        lookups= Q(username__icontains=query) 
        
        results= customer.objects.filter(lookups).distinct()

        users = User.objects.all()



        context={'results': results,'users': users,
                         'submitbutton': submitbutton}
        if request.method == 'POST':
            if request.POST.get('username'):
                messages.add_message(request, messages.INFO, ' information has been successfully Updated.')
                new = customer.objects.get(username=query)
                new2 = edit_note()
                new2.editreport = new
                new.update=timezone.now().replace(microsecond=0)
                new_arabicname=""
                new_Englishname=" "
                new_Mobile=""
                new_email=""
                new_SecondaryEmail1=""
                new_SecondaryEmail2=""
                new_SecondaryMobile1=""
                new_SecondaryMobile2=""
                new_Fax=""
                new_Nationality=""
                new_city=""
                new_identity=""
                new_address=""
                new_street=""
                main=""


                if request.POST.get('Arabicname') !=new.Arabicname:
                    new_arabicname= '"'+"Arabicname"+'"'+' From '+'"'+new.Arabicname+'"'+" To "+'"'+request.POST.get('Arabicname')+' " '
                    main='Customer changed data:'
                ename=new.Englishname
                if request.POST.get('Englishname') !=new.Englishname:

                    new_Englishname='"'+"Englishname"+'"'+' From '+'"'+ new.Englishname +'"'+" To "+'"'+request.POST.get('Englishname')+' " '
                    main='Customer changed data:'
                if request.POST.get('email') != new.email:
                    new_email='"'+"Email"+'"'+' From '+'"'+ new.email+'"' +" To "+'"'+request.POST.get('email')+'"'
                    main='Customer changed data:'
                if request.POST.get('SecondaryEmail1') != new.SecondaryEmail1:
                    new_SecondaryEmail1='"'+"SecondaryEmail1"+'"'+' From '+'"'+ new.SecondaryEmail1+'"' +" To "+'"'+request.POST.get('SecondaryEmail1')+' " '
                    main='Customer changed data:'
                if request.POST.get('SecondaryEmail2') != new.SecondaryEmail2:
                    new_SecondaryEmail2='"'+"SecondaryEmail2"+ '"'+' From '+'"'+new.SecondaryEmail2+'"' +" To "+'"'+request.POST.get('SecondaryEmail2')+' " '
                    main='Customer changed data:'
                if request.POST.get('mobile') != new.mobile:
                    new_Mobile='"'+"Mobile"+ '"'+' From '+'"'+new.mobile+'"'+" To "+'"'+request.POST.get('mobile')+'"'
                    main='Customer changed data:'
                if request.POST.get('SecondaryMobile2') != new.SecondaryMobile2:
                    new_SecondaryMobile2='"'+"SecondaryMobile2"+ '"'+' From '+'"'+new.SecondaryMobile2+'"' +" To "+'"'+request.POST.get('SecondaryMobile2')+' " '
                    main='Customer changed data:'
                if request.POST.get('SecondaryMobile1') != new.SecondaryMobile1:
                    new_SecondaryMobile1='"'+"SecondaryMobile1"+ '"'+' From ''"'++new.SecondaryMobile1+'"' +" to "+'"'+request.POST.get('SecondaryMobile1')+' " '    
                    main='Customer changed data:'
 
                if request.POST.get('Fax') != new.Fax:
                    new_Fax='"'+"Fax"+ '"'+' From '+'"'+ new.Fax +'"'+" To "+'"'+request.POST.get('Fax')+' " '
                    main='Customer changed data:'
                if request.POST.get('Nationality') != new.Nationality:
                    new_Nationality='"'+"Nationality"+ '"'+' From '+'"'+ new.Nationality +'"' +" To "+ '"'+ request.POST.get('Nationality')+' " '
                    main='Customer changed data:'
                if request.POST.get('city') != new.city:
                    new_city='"'+"City"+ '"'+' From '+'"'+ new.city+'"' +" To "+ '"'+ request.POST.get('city')+' " '
                    main='Customer changed data:'
                if request.POST.get('identity') != new.identity:
                    
                    new_identity='"'+"Identity" + '"'+' From '+'"'+ new.identity+'"' +" To "+ '"'+ request.POST.get('identity')+' " '
                    main='Customer changed data:'
                if request.POST.get('address') != new.address:
                    
                    new_address='"'+"Address" + '"'+' From '+'"'+ new.address+'"' +" To "+ '"'+ request.POST.get('address')+' " ' 
                    main='Customer changed data:'
                if request.POST.get('street') != new.street:
                    main='Customer changed data:'
                    new_street='"'+"Street" + '"'+' From '+'"'+ new.street+'"' +" To "+ '"'+ request.POST.get('street')+' " '        
                new.username=request.POST.get('username')
                 
                new.Arabicname=request.POST.get('Arabicname')
                
                    
                new.Englishname=request.POST.get('Englishname')
                new.SecondaryEmail1=request.POST.get('SecondaryEmail1')
                new.SecondaryEmail2=request.POST.get('SecondaryEmail2')
                new.SecondaryMobile1=request.POST.get('SecondaryMobile1')
                new.Fax=request.POST.get('Fax')
                new.Nationality=request.POST.get('Nationality')
                new.city=request.POST.get('city')
                new.SecondaryMobile2=request.POST.get('SecondaryMobile2')
                new.SecondaryEmail1=request.POST.get('SecondaryEmail1')
                new.identity=request.POST.get('identity')
                new.mobile=request.POST.get('mobile')
                new.address=request.POST.get('address')
                new.email=request.POST.get('email')
                new.status=request.POST.get('status')
                new.cserv=request.POST.get('cserv')
                new.create = request.POST.get('create')
                new.emergency=request.POST.get('emergency')
                new.usercustomer=request.POST.get('usercustomer')
                new.emergencycount=request.POST.get('emergencycount')
                new.street=request.POST.get('street')
                new2.useredit=request.POST.get("useredit")

                new2.editname =main+ new_arabicname+new_Englishname+new_Mobile+new_SecondaryMobile1+new_SecondaryMobile2+new_identity+new_city+new_address+new_street+new_Nationality+new_Fax+new_email+new_SecondaryEmail1+new_SecondaryEmail2
                new2.editdate =timezone.now().replace(microsecond=0)
                new2.useredit=request.POST.get('useredit')
                if new2.editname :
                    new2.save()

    
                new.save()        
               
                return redirect(request.META['HTTP_REFERER'])
               
        return render(request, "edit.html", context)
                      
    else:
        return redirect('login')

def edit_serv_view(request, *args, **kwargs):
    if request.user.is_authenticated():

        query= request.GET.get('username') 
            
        

        submitbutton= request.GET.get('submit')
        
        lookups= Q(username__icontains=query) 
        
        results= customer.objects.filter(lookups).distinct()

        users = User.objects.all()



        context={'results': results,'users': users,
                         'submitbutton': submitbutton}
        if request.method == 'POST':
            if request.POST.get('username'):
                messages.add_message(request, messages.INFO, ' The customer information is changed successfully.')
                new = customer.objects.get(username=query)
                new2 = edit_note()
                new2.editreport = new
                new_bundle=""
                new_speed=""
                new_period=""
                main=""
                
                
                

                if request.POST.get('bundle') != new.bundle:
                    new_bundle='"'+"Bundle"+ '"'+' From '+'"'+ new.bundle +'"'+" To "+'"'+request.POST.get('bundle')+' " '
                    main='Customer Service changed data:'
                if request.POST.get('speed') != new.speed:
                    new_speed='"'+"Speed"+ '"'+' From '+'"'+ new.speed +'"'+" To "+'"'+request.POST.get('speed')+' " '
                    main='Customer Service changed data:'
                if request.POST.get('period') != new.period:
                    new_period='"'+"Period"+ '"'+' From '+'"'+ new.period +'"'+" To "+'"'+request.POST.get('period')+' " '
                    main='Customer Service changed data:'


                new2.editname =main + new_bundle + new_speed + new_period 
                new2.editdate =timezone.now().replace(microsecond=0)
                new2.useredit=request.POST.get('useredit')
                if new2.editname :
                    new2.save()
                
                new.bundle=request.POST.get('bundle')
                new.speed=request.POST.get('speed')
                new.period=request.POST.get('period')    
                new.save()
                
                    
               
                
                        
                       
                 
                       
                



                
               
                return redirect(request.META['HTTP_REFERER'])
                
                
                
                


            
               
        return render(request, "edit_service.html", context)
                      
    else:
        return redirect('login')        

def all_activation(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('username') 
            

        submitbutton= request.GET.get('submit')
        
        if query is not None:
            lookups1= Q(status='Activation')
            results= (customer.objects.filter(lookups1))


            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request,"all_activation.html", context)
    else:
        return redirect('login')  

def all_pending(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('username') 
            

        submitbutton= request.GET.get('submit')
        
        if query is not None:
            lookups1= Q(status='Pending')
            results= (customer.objects.filter(lookups1))


            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request,"all_pending.html", context)
    else:
        return redirect('login')             
           
def all_billing(request):
    if request.user.is_authenticated(): 

        query= request.GET.get('username') 
            

        submitbutton= request.GET.get('submit')
        
        if query is not None:
            lookups1= Q(status='Billing')
            results= (customer.objects.filter(lookups1))


            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request,"all_billing.html", context)
    else:
        return redirect('login')     


def delete_view(request):
    if request.user.is_authenticated():
        if request.method == 'GET':    
   
            query= request.GET.get('username')

        
            if query is not None:
                lookups= Q(username__icontains=query) 

                results= customer.objects.filter(lookups).delete()
    
                context= {'results': results
                    }
    
                return render(request, "home.html",context)
            else:
                return render(request, "home.html")
        else:
            return render(request, "home.html")
    else:
        return redirect('login')
def deletebill_view(request):
    if request.user.is_authenticated():
        if request.method == 'GET': 

   
            query1= request.GET.get('id') 
            lookups1= Q(id__icontains=query1) 
            query= request.GET.get('username')

        
            if query is not None:
                lookups= Q(username__icontains=query) 

                results= customer.objects.filter(lookups).distinct()
                results2 =bills.objects.filter(lookups1).delete()
    
                context= {'results': results,'results2':results2
                    }
    
                return render(request, "search.html",context)
            else:
                return render(request, "search.html")
        else:
            return render(request, "search.html")
    else:
        return redirect('login')        
           




def myopenticket_view(request):
    if request.user.is_authenticated():    

        query= request.GET.get('user')
        submitbutton= request.GET.get('submit')
        ticket.objects.filter(id=request.POST.get('close')).update(tickstatus=request.POST.get('tickstatus'),closedate=timezone.now().replace(microsecond=0),userclose=request.POST.get('userclose'))
        resultsreplay= (replay.objects.all())
        
        if query is not None:
            lookups= Q(useradd=query) & Q(tickstatus='Opened')

                
            results= ticket.objects.filter(lookups).order_by('-tickdate')
            new5=replay()
            new5.replaybody=request.POST.get('replaybody')
                 

            context={'results': results,'resultsreplay':resultsreplay,
            'submitbutton': submitbutton}
                
            if new5.replaybody is not None:
                new9 = ticket.objects.get(id=request.POST.get('close'))  
                new5.replayreport=new9
                new5.replaydate=timezone.now().replace(microsecond=0)
                new5.userreplay=request.POST.get('userreplay')
                new5.save()
                return redirect(request.META['HTTP_REFERER']) 
            return render(request,"myopenticket.html", context)
        
        return redirect(request.META['HTTP_REFERER'])


                
        
    else:
        return redirect('login')

            
def new_customer(request, *args, **kwargs):
    if request.user.is_authenticated():

        if request.method == 'POST':
            if request.POST.get('username'):
                new =customer()
                
                new.username=request.POST.get('username')
                new.Arabicname=request.POST.get('Arabicfirstname')+" "+request.POST.get('Arabicmiddlename')+" "+request.POST.get('Arabicthirdname')+" "+request.POST.get('Arabiclastname')
                
                
            
                new.Englishname=request.POST.get('Englishfirstname')+" "+request.POST.get('Englishmiddlename')+" "+request.POST.get('Englishthirdname')+" "+request.POST.get('Englishlastname')
                
                new.service=request.POST.get('service')
                new.bundle="Hallabeek"
                new.speed=request.POST.get('speed')
                new.period=request.POST.get('period')
                new.SecondaryEmail1=request.POST.get('SecondaryEmail1')
                new.SecondaryEmail2=request.POST.get('SecondaryEmail2')
                new.SecondaryMobile1=request.POST.get('SecondaryMobile1')
                new.Fax=request.POST.get('Fax')
                new.Nationality=request.POST.get('Nationality')
                new.city=request.POST.get('city')
                new.SecondaryMobile2=request.POST.get('SecondaryMobile2')
                new.SecondaryEmail1=request.POST.get('SecondaryEmail1')
                new.identity=request.POST.get('identity')
                new.mobile=request.POST.get('mobile')
                new.address=request.POST.get('address')
                new.street=request.POST.get('street')
                new.email=request.POST.get('email')
                new.status=request.POST.get('status')
                new.cserv=request.POST.get('cserv')
                new.emergencycount=0
                new.usercustomer=request.POST.get('usercustomer')
                new.create = request.POST.get('create')
               
                new.save()
                messages.add_message(request, messages.INFO, ' customer added successfully.')


                

            return render(request, "newcustomer.html", {})
        else:
            return render(request, "newcustomer.html", {})
    else:
        return redirect('login')
            
def all_users(request):
    if request.user.is_authenticated(): 

        users = User.objects.all()
 
        submitbutton= request.GET.get('submit')
        context={'users': users,
                     'submitbutton': submitbutton}
        
       

        return render(request,"allusers.html",context)
    else:
        return redirect('login')
                  
   
def show_service(request):
    if request.user.is_authenticated():
        query= request.GET.get('username') 


        submitbutton= request.GET.get('submit')


        
        if query is not None:
            lookups3= Q(vasreport__username=query)
            #lookups4= Q(sname=vas1.objects.get('sname1'))
            results3= (vas1.objects.filter(lookups3))
        
            results= vas.objects.all()

        
            context={'results': results,'results3':results3,
                     'submitbutton': submitbutton}
            if request.method == 'POST':
                if request.POST.get('username'):
                
                    
                    
                    new = customer.objects.get(username=query)
                    new1=vas1()
                    new1.sname1=request.POST.get('sname1')
                    new1.vasstat=request.POST.get('vasstat')
                    new1.uservas=request.POST.get('uservas')
                    new1.vstartdate=timezone.now().replace(microsecond=0)
                    new1.vasreport=new
                    new1.save()
                    new = customer.objects.get(username=query)
                    new3=bills()
                    new3.cusbill=new
                    new3.billstat='Unpaid'
                    new3.userbill=request.POST.get('userbill')
                    new3.billdate=timezone.now().replace(microsecond=0)
                    new3.instalment='0'
                    new3.prom='0'
                    new3.startdate=timezone.now().replace(microsecond=0)
                    if request.POST.get('sname1') == 'filter':
                        new3.billcoast=10
                    elif request.POST.get('sname1') == 'FixedIP':
                        new3.billcoast=20
                    elif request.POST.get('sname1') =='Anti-Virus':
                        new3.billcoast=25
                    
                    new3.enddate=timezone.now().replace(microsecond=0)+ relativedelta(months=1)

                    if new3.billcoast is not None :
                        new3.save()

                    
                    messages.add_message(request, messages.INFO, 'Vas added successfully.')

                    return render(request, "addservice.html",context )
            return render(request, "addservice.html", context)     
         

        
        else:
            return render(request, "addservice.html", {})
    else:
        return redirect('login')
            
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form
    
    })

from django.contrib.auth import authenticate, login
class Index(TemplateView):
    template_name = 'Index.html'



def my_view(request):
    if request.user.is_authenticated():
        return redirect('home')
  
    
    else: 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            
              
        else:
      

            if username and password:
                user_qs = User.objects.filter(username=username)
                pass_qs = User.objects.filter(password=password)
                if not user_qs.exists() & pass_qs.exists():
                    messages.info(request, 'Please enter a correct Login Name and password. Note that both fields may be case-sensitive.')
                    messages.set_level(request, messages.INFO) 
            if request.POST.get('submit') == 'Log in':                   
                if  (username and not password):
                    messages.error(request, 'This field is required.')
                    messages.set_level(request, messages.ERROR)
                if (password and not username):
                    messages.success(request, 'This field is required.')
                    messages.set_level(request, messages.SUCCESS)
            
                if (not username and not password):
                    messages.warning(request, 'This field is required.')
                    messages.set_level(request, messages.WARNING)   



            return render(request,'login.html')
    
      


    
   
        
       

   


def logout_view(request):
    logout(request)
    return render(request, 'login.html')   


def new_service(request, *args, **kwargs):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if request.POST.get('sname'): 
	            new =vas()
	            new.sname=request.POST.get('sname')
	            new.scoast=request.POST.get('scoast')
	        

	            new.save()
            return render(request, "add_newservice.html", {})
        else:
            return render(request, "add_newservice.html", {})
    else:
        return redirect('login')

def add_employee(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
        
            new =employee1()
            new.ename=request.POST.get('ename')
            new.eid=request.POST.get('eid')
            

            new.save()
            messages.add_message(request, messages.INFO, ' The employee added successfully.')

            return render(request, "add_employee.html", {})
        else:
            return render(request, "add_employee.html", {})
    else:
        return redirect('login')           
from django.core.exceptions import ObjectDoesNotExist
      
def employee(request):
    if request.user.is_authenticated(): 
        #messages.add_message(request, messages.INFO, 'The End Date Can Not Be Before The Start Date! Please Re-enter The End Date.')
        #results= vacations.objects.all().delete()
        employee = employee1.objects.all().order_by('worktime')
        g=31-date.today().day
        date1=date.today().strftime('%m/%d/%Y')
        today=date.today().strftime('%A')
        date2=date.today()+ relativedelta(days=g)
        vacation7=vacations.objects.all()
        f=date.today().day-1
        #next_month=date.today()+ relativedelta(days=g)
        #prev_month=date.today()-relativedelta(days=f)
        #next_month =next_month.strftime('%m/%d/%Y')
        #prev_month =prev_month.strftime('%m/%d/%Y')
        prev_month=date.today()-relativedelta(days=f)
        next_month=date.today()+ relativedelta(days=g)
        next_month =next_month.strftime('%m/%d/%Y')
        prev_month =prev_month.strftime('%m/%d/%Y')
        
        #prev_month =prev_month.strftime('%m/%d/%Y')
        
        if request.method == 'POST':
            next_month=request.POST.get('vend')
            prev_month=request.POST.get('vstart')
        #employee1.worktime().strftime('%H:%M')
            if request.POST.get('vac') is not None:
                #lookups3= Q(id1=150)
                
                vac = request.POST.get('vac')
                eid = request.POST.get('eid')

            
                


            
                try:
                    n = vacations.objects.get(vdate=vac,evdate__eid=eid)
                    messages.error(request, 'The employee already have vacation in this day ! .')
                    messages.set_level(request, messages.ERROR)

                    
                    
                    return redirect('employee')

                except ObjectDoesNotExist:
                    new = employee1.objects.get(eid=request.POST.get('eid'))
                    new1=vacations()
                    new1.evdate =new
                    new1.vdate=request.POST.get('vac')
                    new1.save()
                    messages.success(request, 'Vacation added successfully.')
                    messages.set_level(request, messages.SUCCESS)
                    return redirect('employee')
            
             

            if request.POST.get('wt') is not None: 
                employee1.objects.filter(eid=request.POST.get('eid1')).update(worktime=request.POST.get('wt'),endtime=request.POST.get('et'),vacation=request.POST.get('vaca'))
                return redirect('employee')
        #vacations1 = vacations.objects.all()    
        submitbutton= request.GET.get('submit')
        context={'employee': employee,'date':date1,'today':today,'date2':date2,
                    'prev_month':prev_month,'next_month':next_month,'vacation7':vacation7, 'submitbutton': submitbutton}
        
       
            
        return render(request,"employee.html",context)
    else:
        return redirect('login')
from django.contrib import messages

def employee_prof(request):
    if request.user.is_authenticated():    
        
        
        query= request.GET.get('eid')
        submitbutton= request.GET.get('submit')
        #employee1.objects.filter(id=request.POST.get('close')).update(tickstatus=request.POST.get('tickstatus'),closedate=timezone.now().replace(microsecond=0),userclose=request.POST.get('userclose'))
    
        
        if query is not None:
            lookups= Q(eid=query)
                
            results= employee1.objects.filter(lookups)
            
                 

            context={'results': results,
            'submitbutton': submitbutton}
                
            
            return render(request,"employee_prof.html", context)
        
        return redirect(request.META['HTTP_REFERER'])


                
        
    else:
        return redirect('login')


class AutoLogout:
  def process_request(self, request):
    if not request.user.is_authenticated() :
      #Can't log out if not logged in
      return

    try:
      if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 1, 0):
        auth.logout(request)
        del request.session['last_touch']
        return
    except KeyError:
      pass

    request.session['last_touch'] = datetime.now()

