from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly 
from rest_framework.response import Response
from .serializers import PostSerializers
from blog.models import Post
# from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView , ListCreateAPIView
# from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView
# from rest_framework.generics import RetrieveAPIView
# from rest_framework.generics import RetrieveUpdateAPIView
# from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import viewsets





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

# class PostList(ListCreateAPIView):
#     permission_classes =[]
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status = True)




""" post detail with APIView """

# class PostDetail(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializers

#     def get(self , request ,id):
#         post = get_object_or_404(Post , pk=id ,status = True)
#         serializer =self.serializer_class(post)
#         return Response(serializer.data)

#     def put(self , request ,id):
#         post = get_object_or_404(Post , pk=id ,status = True)
#         serializer =self.serializer_class(post , data=request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data)





""" detail and show post with GenericAPIView """


# class PostDetail(GenericAPIView):
#     permission_classes = []
#     serializer_class = PostSerializers

#     def get (self , request , id):
#         post = get_object_or_404(Post , pk = id , status = True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)


""" detail post with RetrieveModelMixin """

# class PostDetail(GenericAPIView , mixins.RetrieveModelMixin):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset= Post.objects.filter(status = True)
#     lookup_field = 'id'


#     def get (self , request , *args , **kwargs):
#         return self.retrieve(request , *args , **kwargs)



""" detail post with UpdateModelMixin """ 


# class PostDetail(GenericAPIView , mixins.RetrieveModelMixin , mixins.UpdateModelMixin):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset= Post.objects.filter(status = True)
#     lookup_field = 'id'


#     def get (self , request , *args , **kwargs):
#         return self.retrieve(request , *args , **kwargs)

#     def put (self , request , *args , **kwargs):
#         return self.update(request , *args , **kwargs)

""" detail post with UpdateModelMixin """ 

# class PostDetail(RetrieveUpdateAPIView):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status = True)= []
#     serializer_class = PostSerializers
#     queryset= Post.objects.filter(status = True)
#     lookup_field = 'id'


#     def get (self , request , *args , **kwargs):
#         return self.retrieve(request , *args , **kwargs)

#     def put (self , request , *args , **kwargs):
#         return self.update(request , *args , **kwargs)

#     def delete(self , request , *args , **kwargs):
#         return self.destroy(request , *args , **kwargs)



""" RetriveAPIView in post detail """

# class PostDetail(RetrieveAPIView):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter (status = True)


""" RetrieveUpdateAPIView """

# class PostDetail(RetrieveUpdateAPIView):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status = True)


""" RetrieveDestroyAPIView """

# class PostDetail(RetrieveDestroyAPIView):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter (status = True)


""" RetrieveUpdateDestroyAPIView in post detail """

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     serializer_class = PostSerializers
#     queryset = Post.objects.filter(status = True)


""" ViewSets """

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PostSerializers
    queryset = Post.objects.filter (status = True)

    # def list(self , request):
    #     serializer = self.serializer_class(self.queryset , many= True)
    #     return Response (serializer.data)

    # def retrieve(self , request , pk=None):
    #     post_object = get_object_or_404(self.queryset , pk=pk)
    #     serializer = self.serializer_class(post_object)
    #     return Response(serializer.data)


    # def create(self , request , pk = None):
    #     pass

    # def update(self , request , pk=None):
    #     pass 

    # def partial_update (self , request ,pk = None):
    #     pass

    # def destroy (self , request , pk=None):
    #     pass 