from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
#from .models import Room, Topic
#from .forms import RoomForm




def loginPage(request):
    page='login.html'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            messages.error(request, 'El usuario o la contraseña es incorrecta')

    context = {'page': page}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')
    

