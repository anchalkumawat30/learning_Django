from django.urls import path 
from . import views

urlpatterns = [
     path("", views.welcome, name = "chat_home")
]