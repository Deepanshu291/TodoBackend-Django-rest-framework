from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', TodoView)

urlpatterns = [
    #  path("todo/", todo, name="todo"),
     path("auth/",include('rest_framework.urls'), name="auth"),
     path('', include(router.urls)),
     path('register/', RegisterView.as_view()),
     path('login/', LoginView.as_view()),
     path('logout/', logOutUser)
    #  path("todo/", TodoViewSet.as_view()) 
]


