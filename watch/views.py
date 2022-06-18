from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Posts

Create your views here.
class PostList(ListView):
    model = Posts
    template_name = 'watch/posts_list.html'

    def get_queryset(self):
        return Posts.objects.all()

# def post_list(request):
#     posts = models.Posts.objects.all()
#     return render(request, "watch/posts_list.html", {'post':post})

# class PostCreate(CreateView):
#     model = Posts
#     fields = ['image', 'title', 'description']
#     success_url = '/'