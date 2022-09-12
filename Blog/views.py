from http.client import HTTPResponse
from sqlite3 import IntegrityError
from turtle import title
from django.shortcuts import render, redirect
from .model.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def signup(request):

    if request.method == 'GET':
        return render(request, 'registration/register.html',{
        'form': UserCreationForm
    })  
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                        username=request.POST['username'], 
                        password=request.POST['password1'])
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect("home")
            except IntegrityError:
                return render(request, 'registration/login.html',{
                                'form': UserCreationForm,
                                'error': 'user already exist' 
                                })  
        return HttpResponse('password do not match')


def home(request):
    return render(request, 'index.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')



def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')


def viewclass(request):
    user = User.objects.create(username='1122', 
                        password='password11221')
    post = Post.objects.create(user = user, title= 'pruebqwa', content= 'hqwola')
    print(Post.objects.all())
    return HttpResponse('post create')
    # que es una view
    # ¿Qué son las vistas en Python?
    # Un función de vista o una vista, como es conocida generalmente, 
    # es una función en Python que hace una solicitud Web y devuelve una respuesta Web, 
    # esta respuesta puede ser el contenido de una página, un error 404, una imagen, 
    # un documento XML, entre muchas cosas más .