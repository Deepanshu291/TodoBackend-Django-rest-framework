from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets , status ,filters
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api.models import *
from rest_framework.parsers import MultiPartParser, FormParser , JSONParser
from api.serializer import *
from rest_framework.authentication import SessionAuthentication , BasicAuthentication 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication , BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    search_fields= ['title','desc']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        user = self.request.user
        query = Todo.objects.filter(user=user)
        return query
    

    def create(self, request, *args, **kwargs):

        user = request.user
        data =request.data
        data['user'] = user.id
        ser = self.serializer_class(data=data)
        ser.is_valid()
        print(ser.error_messages)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        data = request.data 
        instance = self.get_object()
        ser = self.get_serializer(instance , data= data, partial=True)
        ser.is_valid(raise_exception = True)
        print(ser.errors)
        ser.save()
        return super().update(request, *args, **kwargs)
     