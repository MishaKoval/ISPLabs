from django.contrib import admin
from django.urls import path, include

from mainblog.views import HomeView, create_post, DetailPostView, delete_post,UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', create_post, name='create_post'),
    path('post/<slug:slug>', DetailPostView.as_view(), name='detail_post'),
    path('post/<slug:slug>/remove', delete_post, name='remove_post'),
    path('post/<slug:slug>/update', UpdatePostView.as_view(), name='update_post')
]