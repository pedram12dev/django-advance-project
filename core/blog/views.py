from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Post


class IndexView (TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "pedram"
        return context 


class PostList(ListView):
   # model = Post
    context_object_name = 'posts'
    paginate_by = 3
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts
    
 


