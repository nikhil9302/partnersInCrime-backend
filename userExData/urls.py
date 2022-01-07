from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = "routes"),
    path('users/', views.getUsers, name = "usersAll"),
    path('user/<str:pk>/', views.getUser, name = "user"),
]