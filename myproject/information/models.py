from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clientdetails(models.Model):
    clientname = models.CharField(max_length=100, verbose_name ='Name')  
    contact = models.CharField(max_length=12,verbose_name ='Contact no.')
    requirements = models.TextField(verbose_name ='Requirements',max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name ='Budget')
    is_active = models.BooleanField(default=1,verbose_name ='Active')
    created_at = models.DateTimeField(auto_now_add=True,null=True,verbose_name ='Created at')
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    created_by = models.ForeignKey(User, related_name='+',on_delete=models.CASCADE,null=True,verbose_name ='Created by',blank=True)
    updated_by = models.ForeignKey(User, null=True,blank=True, related_name='+',on_delete=models.CASCADE)
	
    def __str__(self):
        return self.clientname


class Projectdetails(models.Model):
    projectname = models.CharField(max_length=100, unique=True,verbose_name ='Name') 
    description = models.TextField(max_length=255,verbose_name ='Description')
    complete_date = models.DateField(verbose_name='Completion Date')
    clients = models.ForeignKey(Clientdetails, related_name='projects',on_delete=models.CASCADE)
    userdata = models.ManyToManyField(User,related_name='userdata',verbose_name ='Users',blank=True)
    is_active = models.BooleanField(default=1,verbose_name ='Active')
    created_at = models.DateTimeField(auto_now_add=True,null=True,verbose_name ='Created at')
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    created_by = models.ForeignKey(User, related_name='+',on_delete=models.CASCADE,null=True,verbose_name ='Created by',blank=True)
    updated_by = models.ForeignKey(User, null=True,blank=True, related_name='+',on_delete=models.CASCADE)
	
    def __str__(self):
        return self.projectname

    
