from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . utils import deleteUser, updateUser, getUserDetails, getAllUsers, createUser

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        "/users/",
        "/user/id"
    ]
    
    return Response(routes)

@api_view(['GET', 'POST'])
def getUsers(request):
    if request.method == "GET":
        return getAllUsers(request)
    
    if request.method == "POST":
        return createUser(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getUser(request, pk):
    
    if request.method == "GET":
        return getUserDetails(request, pk)
    
    if request.method == "PUT":
        return updateUser(request, pk)
    
    if request.method == "DELETE":
        return deleteUser(request, pk)
 