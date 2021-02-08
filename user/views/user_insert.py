from drf_yasg.openapi import FORMAT_PASSWORD
from drf_yasg.utils import swagger_auto_schema

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import serializers, mixins, status, exceptions

from user.models import User
from user.views.urls import check_phone_number, check_user_name
from user.views.user_serializers import UserInfoSerializersLess
from utils.my_encryption import my_encode
from utils.my_info_judge import pd_phone_number
from utils.my_response import response_success_200
from utils.my_status import STATUS_400_BAD_REQUEST, STATUS_200_SUCCESS
from utils.my_swagger import *


class UserInsertView(mixins.CreateModelMixin,
                     GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializersLess

    @swagger_auto_schema(
        operation_summary="添加一条用户数据",
        operation_description="添加一条用户数据",
        request_body=request_body(properties={
            'user_name': string_schema('用户名'),
            'password': string_schema('密码', f=FORMAT_PASSWORD),
            'phone_number': string_schema('手机号'),
        }),
        # deprecated=True
    )
    def create(self, request, *args, **kwargs):

        # 用户名
        user_name = request.data.get('user_name')
        # 手机号
        phone_number = request.data.get("phone_number")
        # 密码
        password = request.data.get("password")

        if not pd_phone_number(phone_number):
            message = "手机号格式错误"
            return response_success_200(code=STATUS_400_BAD_REQUEST, message=message)

        if check_user_name(user_name):
            message = "用户名已存在"
            return response_success_200(code=STATUS_400_BAD_REQUEST, message=message)
        if check_phone_number(phone_number):
            message = "该手机号已被注册"
            return response_success_200(code=STATUS_400_BAD_REQUEST, message=message)

        # 加密
        request.data["password"] = my_encode(password)
        request.data['token'] = "-1"

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # data = serializer.data
        print(f'数据是：{serializer.data}')
        return response_success_200(code=STATUS_200_SUCCESS, data=serializer.data, headers=headers)
