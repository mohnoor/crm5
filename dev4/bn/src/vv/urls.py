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
from crm.views import emplog
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

#from pages.views import home_view, contact_view

urlpatterns = [
url(r'^$', views.home_view, name='home'),
url(r'^custumer/$', views.custumer_view, name='custumer'),
url(r'^emplog$', views.emplog, name='emplog'),
url(r'^search/$', views.search_view, name='search'),
url(r'^newcustumer$', views.new_custumer, name='newcustumer'),
url(r'^login/$',views.emplog, name='login'),
url(r'^edit/$',views.edit_view, name='edit'),
url(r'^showallserves/$',views.show_serves, name='showallserves'),
url(r'^newserves/$',views.new_serves, name='newserves'),
url(r'^delete1$',views.delete_view, name='delete1'),





#url(r'^admin$', admin.site.urls),
#url(r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/exmples.html')),
]
