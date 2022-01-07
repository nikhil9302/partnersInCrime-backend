from rest_framework.response import Response
from . models import UserData
from . serializers import UserDataSerializer

def createUser(request):
    data = request.data 
    user = UserData.objects.create(
        body = data["body"]
    )
    serializer = UserDataSerializer(user, many = False)
    return Response(serializer.data)

def getUserDetails(request, pk):
    user = UserData.objects.get(id = pk) 
    serializer = UserDataSerializer(user, many = False)
    return Response(serializer.data)

def getAllUsers(request):
    users = UserData.objects.all().order_by("-createdAt") 
    serializer = UserDataSerializer(users, many = True)
    return Response(serializer.data)

def updateUser(request, pk):
    data = request.data
    user = UserData.objects.get(id = pk)
    serializer = UserDataSerializer(instance = user, data = data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)    

def deleteUser(request, pk):
    note = UserData.objects.get(id = pk)
    note.delete()
    return Response("User was deleted!")