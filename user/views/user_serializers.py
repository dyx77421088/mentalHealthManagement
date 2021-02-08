from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import User


# 不显示token的
class UserInfoSerializersLess(ModelSerializer):
    class Meta:
        model = User
        exclude = ['token']


class UserInfoSerializersLogin(ModelSerializer):
    password = serializers.CharField(write_only=True, label="密码")

    class Meta:
        model = User
        fields = "__all__"
        depth = 1
