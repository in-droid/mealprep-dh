from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

def index(request):
    user = request.user
    template = loader.get_template('user/index.html')
    print(template)
    context = {
        'user': user
    }

    return HttpResponse(template.render(context, request))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(index)
               
        
        return redirect('login')

    else:
        return render(request, 'user/login.html')
  
        

def register(request):
    if request.method == 'POST':
     
        username = request.POST.get('username')
        password = request.POST.get('psw')
        password2 = request.POST.get('psw-repeat')
        try:
            if User.objects.get(username=username):
                return render(request, 'user/register.html')
        except:
            pass
        
        if password != password2:
            return render(request, 'user/register.html')

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect(login)

    else:
        return render(request, 'user/register.html')


def logout(request):
    auth_logout(request)
    return redirect(index)
