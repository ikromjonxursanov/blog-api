from django.shortcuts import render
from blogapi.serializers import PostSerializer
from posts.models import Post
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly

class PostListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

