from django.db import models


class UserInfo(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, '管理员'),
    )
    user_type = models.IntegerField(choices=user_type_choices, default=1)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE, related_name='token')
    token = models.CharField(max_length=64)


class Words(models.Model):
    word = models.CharField(max_length=32, unique=True)


class Translates(models.Model):
    translate = models.CharField(max_length=128)
    word = models.ForeignKey(Words, related_name='translates', on_delete=models.CASCADE)
