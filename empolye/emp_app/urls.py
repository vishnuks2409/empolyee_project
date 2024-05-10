"""
URL configuration for empolye project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views
app_name="emp_app"

urlpatterns = [
    path('',views.home,name='home'),
    path('view/',views.get_empolye,name='view'),
    path('add/', views.add_empolye, name='add'),
    path('update/<int:pk>', views.update_employe, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),

]
