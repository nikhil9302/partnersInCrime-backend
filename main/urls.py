from django.urls import path

from .import views

urlpatterns = [
    path('',views.getRoutes),
    path('getusers', views.getUsers, name='getUsers'),
    path('getuser/<str:pk>', views.getUserDetails, name='getUserDetails'),
    path('addSkills/', views.addSkills, name='addSkills'),
]