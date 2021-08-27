from django.shortcuts import render,redirect
from .models import players , team
from django.contrib.auth.models import User , auth
from django.contrib import messages;
from django.http import HttpResponse

# Create your views here.

def enter(request):
  return render(request, 'enter.html')

def home(request):
  data = players.objects.all()
  return render(request , 'home.html',{'data':data})

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        password=request.POST.get('password')
        email=request.POST.get('email')
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
        user.save()
        messages.success(request,"Registration Complete")
        return redirect("/home")
    else:
        return render(request,'signup.html')
    
def login(request):
     username=request.POST.get('username')
     password=request.POST.get('password')
     user=auth.authenticate(username=username,password=password)
     if user is not None:
        auth.login(request , user)
        return redirect('/home')   
     else:
        return render(request ,'login.html')

def logout(request):
  auth.logout(request)
  messages.info(request , "Logged Out")
  return redirect('/home')

def teams(request):
  if request.method == 'POST':
    someobj = request.POST.get('players')
    userid = request.POST.get('user')
    someobj = someobj[1:-1:1]
    someobj = someobj.split(",")
    someobj = [int(i) for i in someobj]
    userid = int(userid)

    for i in someobj:
      playerobj = players.objects.get(pk = i)
      finale = team(userid = userid , playerid = playerobj.id)
      finale.save()
    
    return render(request , 'userTeam.html')