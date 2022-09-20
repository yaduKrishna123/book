from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
from bookapp.models import book


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid login try again")
            return redirect('/adminapp/login')

    return render(request,'login.html')

def register(request):
        if request.method == 'POST':
              username=request.POST['username']
              email=request.POST['email']
              first_name=request.POST['first_name']
              last_name=request.POST['last_name']
              password = request.POST['password']
              cpassword = request.POST['password1']
              if password==cpassword:
                  if User.objects.filter(email=email).exists():
                      messages.info(request,"EmailTaken")
                      return render(request,'register.html')
                  else:
                       user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                       user.save();
                       return redirect('/')




              else:
                  messages.info(request,"invalid signIN try again")
                  return render(request,'register.html')

        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

