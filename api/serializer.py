from rest_framework import serializers
from api.models import * 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['created_at', 'updated_at']
        # fields  = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('username','email','id')


# class RegisterUser(serializers.Serializer):
#     class Meta:
#         model = User 
#         fields = ('username','email','id','password')
#         extra_kwargs={'password':{
#             'write_only' : True
#         }}

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             validated_data['username'],
#             validated_data['email'],
#             validated_data['password'],
#         )
#         return user  #super().create(validated_data)
    
# class LoginUserSer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         user = authenticate(**attrs)
#         if User and user.is_active:
#             return user 
#         return ValidationError("incorrect password")