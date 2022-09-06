from rest_framework import generics
from accounts.models import Profile, User
from .serializers import ChangePasswordSerializer, ProfileSerializer, RegistrationSerializer ,CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated






class RegistrationApiView(generics.GenericAPIView):
    
    serializer_class =  RegistrationSerializer
    
    
    
    def post(self , request , *args , **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
           }
            return Response(data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors ,status = status.HTTP_400_BAD_REQUEST )
    
    
    
class CustomObtinAuthToken(ObtainAuthToken):
    
    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data=request.data,context = ({'request' : request}))
        serializer.is_valid(raise_exception =True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)        
        return Response({
            'token' : token.key,
            'user_id' : user.pk ,
            'email' : user.email,
        })
        
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    
class ChangePasswordAPIView(generics.GenericAPIView):
    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated ]
    
    def get_object(self, queryset=None):
            obj = self.request.user
            return obj
    
    def put(self , request , *args , **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password' : ["wrong password"]} , status = status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail' : 'password changed successfully '} , status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset , user=self.request.user)
        return obj
    
    