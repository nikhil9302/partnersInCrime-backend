
from rest_framework import serializers
from main.models import UserInfo
class UserSerialzer(serializers.ModelSerializer):
    batch = serializers.IntegerField(required = False)
    class Meta:
        model = UserInfo
        fields = "__all__"
