from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())

    m =hashlib.md5(bytes(user, encoding='utf8'))
    m.update(bytes(ctime, encoding='utf8'))

    return m.hexdigest()


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': '登录成功'}
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            action = request.query_params.get('action', 'login')
            token = md5(username)
            obj = models.UserInfo.objects.filter(username=username, password=password).first()
            if action == 'login' and not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            elif action == 'signup' and obj:
                ret['code'] = 1003
                ret['msg'] = '用户已存在'
            elif action == 'signup' and not obj:
                obj = models.UserInfo.objects.create(username=username, password=password)
                ret['code'] = 1002
                ret['msg'] = '创建用户成功'
                ret['token'] = token
            else:
                raise Exception()
            models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
        except Exception as e:
            ret['code'] = 1004
            ret['msg'] = str(e)
        return Response(ret, status=status.HTTP_200_OK)


class UserView(generics.ListCreateAPIView):
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        obj = serializer.save()
        models.UserToken.objects.create(user=obj, token=md5(obj.username))


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserDetailSerializer


class WordsView(generics.ListAPIView):
    queryset = models.Words.objects.all()
    serializer_class = serializers.WordsSerializer
