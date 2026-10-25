from django.shortcuts import render

def welcome(request):
     context = {
          "username": "Anchal",
          "app_name": "My Messaging App"
     }
     return render(request,"messaging_app/index.html",context)