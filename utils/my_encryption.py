"""
加密解密工具
"""
import time
from django.core import signing


# 加密token
def my_encode_token(pk, password):
    # id+空格+password+空格+时间进行加密
    return signing.b64_encode((str(pk) + " " + password + " " + str(time.time())).encode()).decode()


# 解密token(返回id和时间)
def my_decode_token(token):
    try:
        s = my_decode(token).split()
        return [s[0], s[-1]]
    except UnicodeDecodeError:
        print("UnicodeDecodeError")
        return None


# 加密
def my_encode(value):
    return signing.b64_encode(value.encode()).decode()


# 解密
def my_decode(value):
    return signing.b64_decode(value.encode()).decode()


# 转换成秒
def get_time(day=0, hour=0, minute=0, second=0):
    return day * (60 * 60 * 24) + hour * (60 * 60) + minute * 60 + second


# token 7天后过期
def get_expiration_time():
    return get_time(day=7)


# 检测token是否过期(true没过期,false过期)
def check_token(token) -> bool:
    if not my_decode_token(token):
        return False
    f = float(my_decode_token(token)[-1])
    print(time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(f)))
    return time.time() - f <= get_expiration_time()
