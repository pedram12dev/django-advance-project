from rest_framework import serializers
from accounts.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length = 255 , write_only = True)
    
    class Meta:
        model = User
        fields = ['email' , 'password' , 'password1']