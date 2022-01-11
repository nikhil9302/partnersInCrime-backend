from rest_framework.serializers import ModelSerializer
from . models import UserData

#serializer for "UserData" model
class UserDataSerializer(ModelSerializer):
    class Meta:
        model = UserData
        exclude = ["actualName", "createdAt"]