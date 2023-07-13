from rest_framework import serializers
from api.models import * 
from django.contrib.auth.models import User

#serializer for Todo list
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['created_at', 'updated_at']
        # fields  = "__all__"
        
#serializer for User Class as this USer modal class is come from django class model 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username','email','id')

