from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Posts
from rest_framework.decorators import api_view
from .serializers import PostsSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PostList(ListView):
    model = Posts
    template_name = 'watch/posts_list.html'

    def get_queryset(self):
        return Posts.objects.all()

def post_list(request):
    posts = models.Posts.objects.all()
    return render(request, "watch/posts_list.html", {'post':post})

class PostCreate(CreateView):
    model = Posts
    fields = ['image', 'title', 'description']
    success_url = '/'

@api_view(['GET', 'POST'])
def showposts(request):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            posts = Posts.objects.all()
            serializer = PostsSerializer(posts, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = PostsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)