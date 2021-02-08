import re

from coreapi import exceptions
from rest_framework.response import Response

from user.models import User
from utils.my_response import response_success_200

"""
一些信息的验证
"""


# 判断身份证的合法性
def pd_card(card: str) -> bool:
    if not card:
        return False
    regular_expression = "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$)|" + \
                         "(^[1-9]\\d{5}\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}$)"
    # 假设18位身份证号码: 41000119910101123

    matches = re.match(regular_expression, card) is not None

    print(matches)
    print(len(card))

    # 判断第18位校验值
    if matches:
        if len(card) == 18:
            try:
                # 前十七位加权因子
                id_card_wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
                # 这是除以11后，可能产生的11位余数对应的验证码
                id_card_y = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
                s = 0
                for i in range(0, len(id_card_wi)):
                    current = int(card[i:i + 1])
                    s += current * id_card_wi[i]
                id_card_last = card[-1:]
                id_card_mod = s % 11
                if id_card_y[id_card_mod].upper() == id_card_last.upper():
                    return True
                else:
                    return False
            except exceptions:
                print("cwu")
                return False
    return matches


# 判断手机号的合法性
def pd_phone_number(phone) -> bool:
    return re.match(r'^1[345678]\d{9}$', phone) is not None


# 密码复杂度
def pd_password(password: str) -> str:
    # 去掉首尾空格后判断密码长度,
    return None if len(password.strip()) >= 6 else "密码长度需要大于等于6位"


# 判断邮箱
def pd_email(email: str) -> bool:
    s = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    return re.match(s, email) is not None


# 判断qq号
def pd_qq(qq: str) -> bool:
    # s = r'[1-9][0-9]{5,9}'
    s = '[1-9]\d{4,11}$'
    return re.match(s, qq) is not None
