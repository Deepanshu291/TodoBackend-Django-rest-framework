from django.urls import path, include
from .views import *


urlpatterns = [
    #  path("todo/", todo, name="todo"),
     path("auth/",include('rest_framework.urls'), name="auth"), 
     path("todo/", TodoViewSet.as_view()) ,
     path("todo/v2/", ListTodoView.as_view()),
     path('todo/v2/<str:pk>/', DetailTodoView.as_view()),
]


