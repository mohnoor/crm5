"""vv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from crm import views
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
#from pages.views import home_view, contact_view

urlpatterns = [
url(r'^Dashboard/$', views.home_view, name='home'),
url(r'^customer/$', views.customer_view, name='customer'),
url(r'^search/$', views.search_view, name='search'),
url(r'^newcustomer$', views.new_customer, name='newcustomer'),
url(r'^newservice$', views.new_service, name='newservice'),
url(r'^newbill$', views.newbill, name='newbill'),
url(r'^paid$', views.paid, name='paid'),
url(r'^myopenticket$', views.myopenticket_view, name='myopenticket'),
url(r'^edit_serv$',views.edit_serv_view, name='edit_serv'),
url(r'^edit$',views.edit_view, name='edit'),
url(r'^showallservice/$',views.show_service, name='showallservice'),
url(r'^newservice/$',views.new_service, name='newservice'),
url(r'^delete1$',views.delete_view, name='delete1'),
url(r'^deletebill$',views.deletebill_view, name='deletebill'),
url(r'^all$',views.all, name='all'),
url(r'^all_activation$',views.all_activation, name='all_activation'),
url(r'^all_billing$',views.all_billing, name='all_billing'),
url(r'^all_pending$',views.all_pending, name='all_pending'),
url(r'^credit$',views.credit, name='credit'),

url(r'^prom$',views.prom, name='prom'),

url(r'^no$',views.no, name='no'),

url(r'^signup$',views.signup, name='signup'),
url(r'^index/$', views.Index.as_view(), name='index'),
url(r'^$', views.my_view, name='login'),

url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
url(r'^admin/', admin.site.urls),
url(r'^allusers$',views.all_users, name='allusers'),
url(r'^employee$',views.employee, name='employee'),
url(r'^add_employee$',views.add_employee, name='add_employee'),
url(r'^employee_prof$',views.employee_prof, name='employee_prof'),








#url(r'^admin$', admin.site.urls),
#url(r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/exmples.html')),
]
