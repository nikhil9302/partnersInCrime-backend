from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerialzer
from .models import UserInfo
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/main/getUsers',
        '/main/getUsers/<str:pk>'
    ]

    return Response(routes)
@api_view(['GET'])
def getUsers(request):
    users = UserInfo.objects.all()
    serializer = UserSerialzer(users,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getUserDetails(request,pk):
    user = UserInfo.objects.get(username = pk)
    serializer = UserSerialzer(user,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def addSkills(request):
    data = request.data
    serializer = UserSerialzer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)