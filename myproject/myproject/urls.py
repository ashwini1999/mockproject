"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Information import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('client-list/', views.ClientList, name='client-list'),
    path('client-create/', views.clientCreate, name='client-create'),
    path('client-detail/<str:pk>/', views.clientDetails, name='client-detail'),
    path('client-update/<str:pk>/', views.clientUpdate, name='client-update'),
    path('client-delete/<str:pk>/', views.clientDelete, name='client-delete'),
    path('project-create/<str:pk>/projects', views.projectCreate, name='project-create'),
    path('projects/', views.Project, name='project'),
]
