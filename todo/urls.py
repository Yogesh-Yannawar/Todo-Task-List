"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('logout/',logout_view,name='logout'),
    path('delete/<sno>/',delete_task,name='delete'),
    path('update/<sno>/',update_task,name='update')
]
