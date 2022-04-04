from unicodedata import name
from django.urls import path, re_path
from . import views
# from django.conf.urls import re_path
from django.contrib.auth.decorators import login_required
 
from . import views
from .models import BookmarkArticle

app_name = 'ajax'
urlpatterns = [
    path('home', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('bookmarks', views.bmk, name='bookmarks'),
]