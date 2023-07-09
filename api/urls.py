from django.urls import path, include
from .views import *


urlpatterns = [
    #  path("todo/", todo, name="todo"),
     path("auth/",include('rest_framework.urls'), name="auth"), 
     path("todo/", TodoViewSet.as_view()) 
]


