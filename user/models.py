from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField("用户名", max_length=255, unique=True)
    password = models.CharField("密码", max_length=255, default="123456")
    phone_number = models.CharField("手机号", max_length=255, unique=True)
    token = models.CharField("token", max_length=255, default="-1")

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'用户名:{self.user_name}, 密码:{self.password}, phoneNumber={self.phone_number}'
