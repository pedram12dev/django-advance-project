from django import views
from django.urls import path 
from .views import IndexView , PostList

urlpatterns = [
    path('' ,IndexView.as_view() , name='index'),
    path('post/' ,PostList.as_view() , name= 'post-list'),
]