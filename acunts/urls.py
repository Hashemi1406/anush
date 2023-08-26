from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token

app_name = 'acunts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('api-token-auth/', auth_token.obtain_auth_token),
]