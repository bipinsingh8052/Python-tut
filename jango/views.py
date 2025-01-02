from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    name = "guest"
    return render(request,"index.html",{'name':name})