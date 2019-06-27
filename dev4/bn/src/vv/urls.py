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
from pages import views
from pages.views import contact_view
from pages.views import emplog
from django.contrib import admin

#from pages.views import home_view, contact_view

urlpatterns = [
url(r'^$', views.home_view, name='home'),
url(r'^contact/$', views.contact_view, name='contact'),
url(r'^emplog$', views.emplog, name='emplog'),
url(r'^search$', views.search, name='search'),
url(r'^newcustumer$', views.new_custumer, name='newcustumer'),
url(r'^index$', views.index, name='index'),
#url(r'^admin$', admin.site.urls),
#url(r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/exmples.html')),
]
