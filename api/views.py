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
from django.contrib.auth import login, logout
# Create your views here.



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
    
# class RegisterUserView(generics.GenericAPIView):
#     serializer_class = RegisterUser

#     def post(self, request,*args, **kwargs):
#         serializer = self.get_serializer(data= request.data)
#         serializer.is_valid(raise_exception= True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user,context = self.get_serializer_context()).data
#         })
    
# class LoginUserView(generics.GenericAPIView):
#     serializer_class = LoginUserSer 
#     def post(self, request,*args, **kwargs):
#         serializer = self.get_serializer(data= request.data)
#         if not serializer.is_valid():
#             # messages.warning(request,"invalid username,password")
#             return Response({
#                 "error":"invalid username password"
#             }, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             user = serializer.validated_data
#             login(request,user)
#             return Response({
#             "user": UserSerializer(user,context = self.get_serializer_context()).data
#             })

@api_view(['POST'])
def login(reques):
    return Response()


@api_view(['POST'])
def signup(request):
    serializer =UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.object.get(username = request.data['username'])
    return Response()

@api_view(["POST"])
def logOutUser(request):
    logout(request)
    return Response({
        "Logout":"success"
    }, status=status.HTTP_202_ACCEPTED)