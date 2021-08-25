"""photoproject URL Configuration

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
from django.urls import path
from photo import views
from django.views import static 
from django.conf import settings 
from django.conf.urls import url 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.searchfile),
    path('searchfile/', views.searchfile),
    path('searchfileinfo/', views.serchfileinfo),
    path('selectfiletype/', views.selectfiletype),
    url(r'^static/(?P<path>.*)$', 
    static.serve,{'document_root': settings.STATIC_ROOT }, name='static'),
    url(r'^images/(?P<path>.*)$', 
    static.serve, {'document_root': settings.MEDIA_ROOT }, name='images'),
    url(r'^imageshaibao/(?P<path>.*)$', 
    static.serve, {'document_root': settings.MEDIAHB_ROOT }, name='imageshaibao'), 
    url(r'^imagesmaijiaxiu/(?P<path>.*)$', 
    static.serve, {'document_root': settings.MEDIAMJX_ROOT }, name='imagesmaijiaxiu'),  #imagespinpaidarentu
    url(r'^imagespinpaidarentu/(?P<path>.*)$', 
    static.serve, {'document_root': settings.MEDIAPPDRT_ROOT }, name='imagespinpaidarentu'),
    url(r'^imageszhutu/(?P<path>.*)$', 
    static.serve, {'document_root': settings.MEDIAZHUTU_ROOT }, name='imageszhutu'),
    url(r'^imagesother/(?P<path>.*)$', 
    static.serve, {'document_root': settings.MEDIAOTHER_ROOT }, name='imagesother'),
    url(r'^imagesshiti/(?P<path>.*)$', 
    static.serve, {'document_root': settings.MEDIASHITI_ROOT }, name='imagesshiti'),
]

