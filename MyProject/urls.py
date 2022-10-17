"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from Blog.views import *
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from MyProject.settings.base import DEBUG

handler404 = 'Blog.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_post_user, name='home'),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
    path('<str:room_name>/', chatroom, name='room'),
    path('chat', chat, name="chat"),
    path('create_post', create_post, name="create_post"),
    path('list', view_post, name="list"),
    path('post_detail/<int:post_id>', post_detail, name="post_detail"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('post/<int:post_id>/delete', delete_post, name='delete_post'),
    path('social-auth/', include('social_django.urls', namespace='social')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]


if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# else:

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# url que hace?
# las url son las direciones donde apuntan nuestras views,
# aqui importamos nuestras views y le damos una url para que se direcciones .