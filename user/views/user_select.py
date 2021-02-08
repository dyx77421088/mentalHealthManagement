from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user.models import User
from user.views.user_serializers import UserInfoSerializersLogin
from utils.my_encryption import my_encode_token, my_encode
from utils.my_response import response_success_200
from utils.my_swagger import request_body, string_schema


class UserSelectView(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializersLogin

    @swagger_auto_schema(
        operation_summary="登录验证",
        operation_description="用户名或手机号加密码登录，同时优先用户名",
        request_body=request_body(
            required=["password"],
            properties={
                "user_name": string_schema('用户名'),
                "password": string_schema('密码，必填'),
                "phone_number": string_schema('手机号')
            }
        ),
    )
    def login(self, request):
        username = request.data.get("user_name")
        password = request.data.get("password")
        phone_number = request.data.get("phone_number")

        password = my_encode(password)

        if not password or not username and not phone_number:
            return response_success_200(code=400, message="参数错误！！！")
        try:
            if username:
                instance = self.queryset.get(password=password, user_name=username)
            elif phone_number:
                instance = self.queryset.get(password=password, phone_number=phone_number)
            else:
                instance = None
        except User.DoesNotExist:
            return response_success_200(code=400, message="用户名或密码错误")

        # 设置token
        instance.token = my_encode_token(instance.pk, my_encode(instance.user_name))
        # 保存
        instance.save()
        serializer = self.get_serializer(instance)

        return response_success_200(message="成功!!!!", data=serializer.data)
