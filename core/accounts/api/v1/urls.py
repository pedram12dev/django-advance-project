from django.urls import path
from . import views

app_name = 'api-v1'
urlpatterns =[
        #register
        path ('registration/' ,views.RegistrationApiView.as_view() , name= 'registration'),
        
        #login
        path ('token/login/' , views.CustomObtinAuthToken.as_view() , name='token-login'),
]