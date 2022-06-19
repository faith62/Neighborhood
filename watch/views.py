from email import message
from django.shortcuts import render
<<<<<<< HEAD
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Business

from .serializer import BusinessSerializer
from rest_framework import status

# Create your views here.
class BusinessList(APIView):
    def get(self, request, format=None):
        all_business = Business.objects.all()
        serializers = BusinessSerializer(all_business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def business(request):
        business =Business.objects.all()
        
        return render(request,'', {'business':business})

    def search_business(request):
        if 'business' in request.GET and request.GET["business"]:
            business_name = request.GET.get("business")
            searched_business = Business.find_business(business_name)
            message = f"{business_name}"

            return render(request, '',{"message":message,"businesses": searched_business})

        else:
            message = "You haven't searched for any term"
            return render(request, '',{"message":message})
=======
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
>>>>>>> 8b42fc756cdd53586df8844f3d316211bc29cb45
