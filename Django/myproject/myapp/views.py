from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # return HttpResponse('<h1>Hey , Welcome</h1>')
   
   #name = 'Haya'
   #return render(request,'index.html',{'name':name})

   # context = {
   # 'name' : 'Patrick',
   # 'age' : 23,
   # 'nationality' : 'British',
   # }
   #return render(request,'index.html',context)
   return render(request,'index.html')


def counter(request):
   # word = request.GET['word'] URL appears without using POST , <form method="" 
   word = request.POST['word']
   amount_of_word = len(word.split())
   return render(request,'counter.html',{'amount':amount_of_word})