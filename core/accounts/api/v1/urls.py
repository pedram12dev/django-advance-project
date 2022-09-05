from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'api-v1'
urlpatterns =[
        #register
        path ('registration/' ,views.RegistrationApiView.as_view() , name= 'registration'),
        
        #login
        path ('token/login/' , views.CustomObtinAuthToken.as_view() , name='token-login'),
        
        
        #jwt login
        path ('jwt/create/' , views.CustomTokenObtainPairView.as_view() , name='jwt-create'),
        path ('jwt/refresh/' ,TokenRefreshView.as_view() , name = 'jwt-refresh'),
        path ('jwt/verify/' ,TokenVerifyView.as_view() , name= 'jwt-verify' )
]