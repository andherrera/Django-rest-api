from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('user/', views.UserCreateView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),    
    path('movie/', views.MovieListCreateView.as_view()),    
    path('movie/<int:pk>/', views.MovieRetrieveUpdateView.as_view()),
    path('randNum/', views.random_number_retrieve_view)
]

