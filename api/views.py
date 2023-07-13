import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets , status ,filters, generics
from rest_framework.decorators import api_view
from api.models import *
from rest_framework.parsers import MultiPartParser, FormParser , JSONParser
from api.serializer import *
from rest_framework.authentication import SessionAuthentication , BasicAuthentication 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import *
# Create your views here.

class RegisterView(generics.GenericAPIView):
    def post(self, request):
        serializer =UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(username,password)
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not Found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password :(')
        
        # payload ={
        #     'id':user.id,
        #     'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     'iat':datetime.datetime.utcnow()
        # }

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user=user)
            print("user is here ")
        
        print(request.user)
        refresh = RefreshToken.for_user(user=user)
        return Response({
            'message': 'login successful',
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        })

@api_view(["GET"])
def logOutUser(request):
    logout(request)
    return Response({
        "logout": "success"
    })

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication , BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    search_fields= ['title','desc']
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

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
    
