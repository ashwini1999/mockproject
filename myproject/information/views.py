from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Information.models import Clientdetails,Projectdetails
from Information.serializers import ClientSerializer,ProjectSerializer,clientDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#display client list
@api_view(['GET'])
def ClientList(request):
    clients = Clientdetails.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


#create client list
@api_view(['POST'])
def clientCreate(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#retrieve info of client with projects 
@api_view(['GET'])
def clientDetails(request,pk):  
    clients = Clientdetails.objects.get(id=pk)
    projects = Projectdetails.objects.filter(clients=clients)
    serializer = clientDetailSerializer(projects, many=True)
    return Response(serializer.data)
   


#update client details
@api_view(['POST'])
def clientUpdate(request,pk):
    clients = Clientdetails.objects.get(id=pk)
    serializer = ClientSerializer(instance=clients,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#delete client details
@api_view(['DELETE'])
def clientDelete(request,pk):
    clients = Clientdetails.objects.get(id=pk)
    clients.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#create projects
@api_view(['POST'])
def projectCreate(request,pk):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        client = Clientdetails.objects.get(id=pk)
        serializer.save(clients=client)      
      
    return Response(serializer.data)


#logging user data
@api_view(['GET'])
def Project(request):
    current_user = request.user
    user_data = current_user.id
    projects = Projectdetails.objects.filter(userdata=user_data)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)













