from django.shortcuts import render

def welcome(request):
     return render(request,"messaging_app/index.html")