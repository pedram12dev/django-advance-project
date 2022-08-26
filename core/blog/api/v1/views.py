from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly 
from rest_framework.response import Response
from .serializers import PostSerializers
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView , ListCreateAPIView
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView


# """ list and create post from APIView  """
# class PostList(APIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializers
#     def get(self , request):
#         posts = Post.objects.filter(status = True)
#         serializer = PostSerializers(posts , many =True)
#         return Response(serializer.data)

#     def post(self , request):
#         serializer =PostSerializers(data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data)


# """ list and create post from GenericAPIView """

# class PostList(GenericAPIView):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status = True)

#     def get (self , request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset , many=True)
#         return Response(serializer.data)

#     def post(self , request):
#         serializer =self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data)




# """ list and create post from ListModelMixin and CreateModelMixin """

# class PostList(GenericAPIView , mixins.ListModelMixin , mixins.CreateModelMixin):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter (status = True)

#     def get(self , request , *args , **kwargs):
#         return self.list(request , *args , **kwargs)

#     def post(self ,request , *args , **kwargs):
#         return self.create(request , *args , **kwargs)


""" list and create post from ListCreateAPIView """

class PostList(ListCreateAPIView):
    permission_classes =[]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status = True)






class PostDetail(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializers

    def get(self , request ,id):
        post = get_object_or_404(Post , pk=id ,status = True)
        serializer =self.serializer_class(post)
        return Response(serializer.data)

    def put(self , request ,id):
        post = get_object_or_404(Post , pk=id ,status = True)
        serializer =self.serializer_class(post , data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)





""" detail and show post with GenericAPIView """


class PostDetail(GenericAPIView):
    permission_classes = []
    serializer_class = PostSerializers

    def get (self , request , id):
        post = get_object_or_404(Post , pk = id , status = True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)


