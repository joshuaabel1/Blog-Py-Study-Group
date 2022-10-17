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

# Las vistas son los controladores de nuestras templates por aca pasa la logica 
# de estas y los modelos.

def signup(request):

    # Aca haremos uso de los formularios de django en forms.py veremos mas.
    if request.method == 'GET':
        # Comprobamos el tipo de request
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
                # Guardamos nustro nuevo objeto.
                # Con login le damos una sesion a el usuario logueado.
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # Chequiamos el modelo del que estamos autenticando. 
                return redirect("home")
            except IntegrityError:
                return render(request, 'registration/login.html',{
                                'form': UserCreationForm,
                                'error': 'user already exist' 
                                })  
        return HttpResponse('password do not match')
        # Integrated registration form in django


def home(request):
    # Con la libreria render definimos la template que usaremos en la vista
    return render(request, 'index.html')


# Con el decorador @login_required podemos exigir que el usuario este logueado
@login_required
def signout(request):
    logout(request)
    # Usamos la libreria integrada de logout en django.
    return redirect('home')
    # Con redirect elejimos donde nos enviara la vista cuando efectuamos la tarea.


def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
            # Con autenticate validamos nuestro usuario
        if user is None:
            return render(request, 'registration/login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')


# Armamos nuestra propia template de error para proteger nuestras rutas.
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
            return render(request, 'post.html', {"form": PostForm, "error": "Error creating post."})


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
        post = get_object_or_404(Post, pk=post_id, user=request.user, )
        form = PostForm(request.FILES, instance=post)
        return render(request, 'detaillpost.html', {'posts': post, 'form': form})
    else:
        try:
            post = get_object_or_404(Post, pk=post_id, user=request.user)
            form = PostForm(request.POST, request.FILES, instance=post)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'detaillpost.html', {'posts': post, 'form': form, 'error': 'Error updating post.'})


def chat(request):
    return render(request, 'chat.html')


def chatroom(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })