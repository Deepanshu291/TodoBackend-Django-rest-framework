
from rest_framework.response import Response
from rest_framework import viewsets , status ,filters, generics,views
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

class RegisterView(views.APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer =UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(username,password)
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not Found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password :(')
        
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
        },
        status=status.HTTP_202_ACCEPTED
        )

@api_view(["GET"])
def logOutUser(request):
    logout(request)
    return Response({
        "logout": "success"
    },
    status=status.HTTP_202_ACCEPTED)


#use ModelViewset for CRUD but i do some tweaks in there  
class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication , BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    search_fields= ['title','desc']
    filter_backends = (filters.SearchFilter,)

    #when a post request perform then it save user in todo model class
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

    # when a get request perform then it return All Todo data..
    def get_queryset(self):
        user = self.request.user
        query = Todo.objects.filter(user=user) #here use user to get only current user Todo list 
        return query
    
    # it used to Create new Todo in Database
    def create(self, request, *args, **kwargs):
        user = request.user
        data =request.data
        data['user'] = user.id
        ser = self.serializer_class(data=data)
        ser.is_valid()
        print(ser.error_messages)
        return super().create(request, *args, **kwargs)
    
    # it for patch request and for update Todo in Database 
    def update(self, request, *args, **kwargs):
        data = request.data 
        instance = self.get_object()
        ser = self.get_serializer(instance , data= data, partial=True)
        ser.is_valid(raise_exception = True)
        print(ser.errors)
        ser.save()
        return super().update(request, *args, **kwargs)
    
    #And delete request is by default from ModelViewSet.... 
    
