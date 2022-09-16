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
from django.urls import path
from Blog.views import *
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
    # path('viewclass', viewclass, name="viewclass"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# url que hace?
# las url son las direciones donde apuntan nuestras views,
# aqui importamos nuestras views y le damos una url para que se direcciones .