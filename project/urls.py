"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login, logout
from django.conf.urls import include
from django.views.generic.base import RedirectView
from rango import views
from rango.forms import LoginForm


urlpatterns = [
    #
    #url(r'^rango/', include('rango.urls')), 
    #(r'^logout/$', logout,{'template_name':'logout.html'}),
    #url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('rango.urls',namespace="rango")),
    #url(r'^rango/', include('rango.urls')),
    #url(r'^rango/', include('rango.urls', namespace="rango")),
    #url(r'^$', RedirectView.as_view(url='/rango/')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^register/$', auth_views.logout, {'next_page': '/login'}),
    #url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    #url(r'^basic/', include('basic.urls')),
]
