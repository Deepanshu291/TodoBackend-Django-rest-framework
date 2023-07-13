from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter() #use router which is come from rest_framework 
router.register(r'todo', TodoView) #regiter todoView in router 

urlpatterns = [
     path('', include(router.urls)),
     path('register/', RegisterView.as_view()), # create register router link from RegisterView
     path('login/', LoginView.as_view()), # create Login router link from LoginView
     path('logout/', logOutUser)  # create Logout router link from LogoutView
]


