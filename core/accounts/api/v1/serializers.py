from dataclasses import fields
from accounts.models import Profile, User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import password_validation
 



class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length = 255 , write_only = True)
    
    class Meta:
        model = User
        fields = ['email' , 'password' , 'password1']
        
        
    def validate(self , attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail' : 'password doesnt match'})
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password' : list(e.messages)})
        return super().validate(attrs)
    
    
    def create (self , validated_data):
        validated_data.pop('password1' , None)
        return User.objects.create_user(**validated_data)
    


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self , attrs):
        validated_data = super().validate(attrs)
        validated_data["email"] = self.user.email
        validated_data["user_id"] = self.user.id
        return validated_data
    
    
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    
    
    old_password = serializers.CharField(required =True)
    new_password = serializers.CharField(required = True)
    new_password1 = serializers.CharField(required = True)
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value
    
    def validate(self, data):
        if data['new_password'] != data['new_password1']:
            raise serializers.ValidationError({'new_password1': _("Password doesnt match")})
        password_validation.validate_password(data['new_password'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user
    
    
class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source = 'user.email' , read_only = True)
    
    
    class Meta : 
        model = Profile
        fields = ('id' , 'email' , 'firstname' , 'lastname' ,'image', 'description')
        