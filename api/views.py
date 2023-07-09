from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets , status ,filters , generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api.models import *
from rest_framework.parsers import MultiPartParser, FormParser , JSONParser
from api.serializer import *
from rest_framework.authentication import SessionAuthentication , BasicAuthentication 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ListTodoView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodoView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



class TodoViewSet(APIView):
    authentication_classes = [JWTAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    serializers = TodoSerializer

    def get(self,request):
        user = request.user
        print(user)
        query = Todo.objects.filter(user=self.request.user)
      
        serializers = TodoSerializer(query, many=True)
        return Response({
            'status':200,
            'message': 'Success',
            'data': serializers.data
        })
        

    def post(self,request, *args, **kwargs):
        try:
            user = request.user
            data = request.data 
            data['user'] = user.id
            serializer = TodoSerializer(data=data,)

            if not serializer.is_valid():
                return Response({
                    'status':400,
                    'message': 'invalid fields',
                    'data': serializer.data
                })
            
            serializer.save()

            return Response({
                'status': 200,
                'message':'Todo is Created succesfully',
                'data': serializer.data,
                
            })
        except:
            print("")
    
    def patch(self, request,pk):
        try:
            data = request.data 
            if not data.get('uuid'):
                return Response(
                    data={},
                    status=status.status.HTTP_200_OK
                )
            obj = Todo.objects.filter(uuid=pk)
            if not obj.exists():
                return Response(
                    status=status.HTTP_204_NO_CONTENT,
                    data= {}
                )
            serializer = TodoSerializer(obj[0] , data=data, partial=True)
            if not serializer.is_valid():
                return Response({
                    'status':400,
                    'message': 'invalid fields',
                    'data': serializer.data
                })
            
            serializer.save()

            return Response({
                'status': 200,
                'message':'Todo is Created succesfully',
                'data': serializer.data,
                
            })
        except Exception as e:
            print(e)
        # user = self.request.user
        # data = request.data 
        # print(user)
        # data['user'] = user.id 
        # serializer = TodoSerializer(data=data)
        # # ser = self.serializers(data=data)
        # # ser.is_valid()
        # # print(ser.error_messages)
        # # return super().create(request, *args, **kwargs )
        # if not serializers.is_valid():
        #         return Response({
        #             'status':400,
        #             'message': 'invalid fields',
        #             'data': {}
        #         })
        
        # serializer.save()
        # return  Response({
        #         'status': 200,
        #         'message':'Todo is Created succesfully',
        #         'data': serializer.data,
                
        #     })

        
