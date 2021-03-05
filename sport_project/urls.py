"""sport_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from football_app import views as v
from django.contrib.auth import urls
from django.conf.urls.static import static

from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings

urlpatterns = [

    path('', v.user_login, name = 'football_app'),
    path('admin/', admin.site.urls),
    path('register/',v.form_name_view,name = 'form_name'),
    path('',include(urls),name= 'login'),
    path('cricket/',v.cricket,name='cricket'),
    path('homepage/',v.homepage,name='homepage'),
    path('basketball/',v.basketball,name='basketball'),
    path('football/',v.football,name='football'),
    path('p1/',v.p1,name='p1'),
    path('p2/',v.p2,name='p2'),
    path('p3/',v.p3,name='p3'),
    path('p4/',v.p4,name='p4'),
    path('p5/',v.p5,name='p5'),
    path('p6/',v.p6,name='p6'),





]
