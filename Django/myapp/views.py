from django.http import HttpResponse
from django.shortcuts import render
from .models import Feature

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
   feature1 = Feature()
   feature1.name = 'Muaaz'
   feature1.id = 1
   feature1.is_true = True
   feature1.details = "Your service is quick"

   feature2 = Feature()
   feature2.name = 'Haya'
   feature2.id = 2
   feature1.is_true = True
   feature2.details = "Your service is responsible"

   feature3 = Feature()
   feature3.name = 'Fiwaza'
   feature3.id = 3
   feature1.is_true = True
   feature3.details = "Your service is good"

   feature4 = Feature()
   feature4.name = 'Farah'
   feature4.id = 4
   feature1.is_true = False
   feature4.details = "Your service is better"

   features = [feature1,feature2,feature3,feature4]


  # return render(request,'index.html',{'feature1':feature1,'feature2':feature2 , 'feature3':feature3})
   return render(request,'index.html', {'features': features})

def counter(request):
   # word = request.GET['word'] URL appears without using POST , <form method="" 
   word = request.POST['word']
   amount_of_word = len(word.split())
   return render(request,'counter.html',{'amount':amount_of_word})