from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clientdetails(models.Model):
    clientname = models.CharField(max_length=100, verbose_name ='Name')  
    is_active = models.BooleanField(default=1,verbose_name ='Active')
    created_at = models.DateTimeField(auto_now_add=True,null=True,verbose_name ='Created at')
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    created_by = models.ForeignKey(User, related_name='+',on_delete=models.CASCADE,verbose_name ='Created by')
 
    def __str__(self):
        return self.clientname


class Projectdetails(models.Model):
    projectname = models.CharField(max_length=100, unique=True,verbose_name ='Name') 
    clients = models.ForeignKey(Clientdetails, related_name='projects',on_delete=models.CASCADE,null=True)
    userdata = models.ForeignKey(User, related_name='projects',on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=1,verbose_name ='Active')
    created_at = models.DateTimeField(auto_now_add=True,null=True,verbose_name ='Created at')
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    created_by = models.ForeignKey(User, related_name='+',on_delete=models.CASCADE,verbose_name ='Created by')
  	
    def __str__(self):
        return self.projectname

    

