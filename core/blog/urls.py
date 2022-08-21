from django import views
from django.urls import path , include
from .views import IndexView , PostList

urlpatterns = [
    path('' ,IndexView.as_view() , name='index'),
    path('post/' ,PostList.as_view() , name= 'post-list'),
    path ('api/v1/' , include('blog.api.v1.urls')),
]
