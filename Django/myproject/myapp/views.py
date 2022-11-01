from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # return HttpResponse('<h1>Hey , Welcome</h1>')
   return render(request,'index.html')