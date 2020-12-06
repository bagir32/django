"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from .views import *

from django.conf.urls import url, include, static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('redirect/', data_flair),
    path('dataflair/', index),
    path('djangotutor/', tutorial.as_view()),
    path('setcookie', setcookie),
    path('getcookie', showcookie),
    path('deleteco', delete_co),
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),
    path('create/', create_session),
    path('access', access_session),
    path('delete/', delete_session),
    path('subscribe/', include('subscribe.urls')),
    path('upload/', include('profile_maker.urls')),
    path('', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('cms.urls')),
]  # + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
