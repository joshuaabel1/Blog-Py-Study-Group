from http.client import HTTPResponse
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .model.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import PostForm

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
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')# check 
                return redirect("home")
            except IntegrityError:
                return render(request, 'registration/login.html',{
                                'form': UserCreationForm,
                                'error': 'user already exist' 
                                })  
        return HttpResponse('password do not match')
        #integrated registration form in django


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


def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response


@login_required
def create_post(request):
    if request.method == "GET":
        return render(request, 'post.html', {"form": PostForm})
    else:
        try:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                new_task = form.save(commit=False) 
                new_task.user = request.user
                print(new_task.image)
                new_task.save()
                return redirect('home')
        except ValueError:
            return render(request, 'post.html', {"form": PostForm, "error": "Error creating task."})

    # ¿Qué son las vistas en Python?
    # Un función de vista o una vista, como es conocida generalmente, 
    # es una función en Python que hace una solicitud Web y devuelve una respuesta Web, 
    # esta respuesta puede ser el contenido de una página, un error 404, una imagen, 
    # un documento XML, entre muchas cosas más .


def view_post(requests):
    posts = Post.objects.all()
    return render(requests, 'list.html', {"posts": posts})


@login_required
def view_post_user(requests):
    posts = Post.objects.filter(user=requests.user)
    return render(requests, 'listuser.html', {"posts": posts})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')


@login_required
def post_detail(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id, user=request.user)
        form = PostForm(instance=post)
        return render(request, 'detaillpost.html', {'posts': post, 'form': form})
    else:
        try:
            post = get_object_or_404(Post, pk=post_id, user=request.user)
            form = PostForm(request.POST, instance=post)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'detaillpost.html', {'posts': post, 'form': form, 'error': 'Error updating post.'})