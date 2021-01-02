from rest_framework import serializers
from Information.models import Clientdetails,Projectdetails


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientdetails
        fields = ('id', 'clientname','created_at', 'updated_at', 'created_by')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projectdetails
        fields = ('id', 'projectname','clients','userdata', 'created_at', 'updated_at', 'created_by')


class clientDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projectdetails
        fields = ('id', 'projectname','clients', 'created_at', 'updated_at', 'created_by')