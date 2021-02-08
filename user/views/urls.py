from django.core.cache import cache

from user.models import User
from utils.my_encryption import my_decode_token


def send_code(phone_number: str) -> bool:
    cache.set(f'{phone_number}_code', phone_number[-6:], 600)
    return True


# 从cache中验证验证码
def judge_code(phone_number: str, code: str) -> bool:
    if code:
        return cache.get(f'{phone_number}_code') == code
    return False


# 判断手机号是否存在
def check_phone_number(phone_number) -> bool:
    return User.objects.filter(phone_number=phone_number).exists()


# 判断用户名是否存在
def check_user_name(user_name) -> bool:
    return User.objects.filter(user_name=user_name).exists()


# 根据token获得详细信息
def get_info_by_token(token):
    dk = my_decode_token(token)
    if not dk:
        return None
    return get_info(int(dk[0]), int(dk[1]))