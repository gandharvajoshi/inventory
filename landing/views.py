from django.shortcuts import render

def index(request):
    return render(request,"landing/landing.html")
# Create your views here.
