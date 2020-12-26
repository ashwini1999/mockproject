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
from information import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projectcount/',views.Projectcount,name='count'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('client/',views.AddClient.as_view(),name='home'),
    path('client/<int:pk>/',views.EditClient.as_view(),name='edit_client'),
    path('client/<int:pk>/delete/',views.DeleteClient,name='delete_client'),
    path('project/',views.AddProject.as_view(),name='add_project'),
    path('user-autocomplete/',views.UserAutocomplete.as_view(),name='user-autocomplete'),
    path('project/',views.AddProject.as_view(),name='add_project'),
    
]
