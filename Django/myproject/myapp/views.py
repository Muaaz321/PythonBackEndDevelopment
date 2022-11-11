from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import Feature

def index(request):
   features = Feature.objects.all()
   return render(request,'index.html', {'features': features})
   # return HttpResponse('<h1>Hey , Welcome</h1>')
   
   #name = 'Haya'
   #return render(request,'index.html',{'name':name})

   # context = {
   # 'name' : 'Patrick',
   # 'age' : 23,
   # 'nationality' : 'British',
   # }
   #return render(request,'index.html',context)

   # feature1 = Feature()
   # feature1.name = 'Muaaz'
   # feature1.id = 1
   # feature1.is_true = True
   # feature1.details = "Your service is quick"

   # feature2 = Feature()
   # feature2.name = 'Haya'
   # feature2.id = 2
   # feature1.is_true = True
   # feature2.details = "Your service is responsible"

   # feature3 = Feature()
   # feature3.name = 'Fiwaza'
   # feature3.id = 3
   # feature3.is_true = True
   # feature3.details = "Your service is good"

   # feature4 = Feature()
   # feature4.name = 'Farah'
   # feature4.id = 4
   # feature4.is_true = False
   # feature4.details = "Your service is better"

   # features = [feature1,feature2,feature3,feature4]


  # return render(request,'index.html',{'feature1':feature1,'feature2':feature2 , 'feature3':feature3})
   

def counter(request):
   # word = request.GET['word'] URL appears without using POST , <form method="" 
   # word = request.POST['word']
   # amount_of_word = len(word.split())
   posts = [1,2,3,4,5,'time','tom','John']

   return render(request,'counter.html',{'posts':posts})

def register(request):
   if request.method == 'POST':

      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']

      if password == password2:
         if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already exists')
            return redirect('register')
         elif User.objects.filter(username=username).exists():
            messages.info(request,'User name already exists')
            return redirect('register')
         else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login')
      else:
         messages.info(request,'Password not the same')
         return redirect('register')
   else:
      return render(request,'register.html')



def Login(request):
   if request.method =='POST':
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username = username,password = password)

      if user is not None:
         auth.login(request,user)
         return redirect('/')
      else:
         messages.info(request,'Credentials are invalid')
         return redirect('login')
   else:
      return render (request,'login.html')

   
def Logout(request):
      auth.logout(request)
      return redirect('/')

def post(request,pk):
   return render(request,'post.html',{'pk':pk})

