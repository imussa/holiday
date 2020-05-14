from rest_framework.serializers import *
from . import models


class AuthSerializer(ModelSerializer):
    token = ReadOnlyField(source='token.token')
    password = CharField(write_only=True)
    class Meta:
        model = models.UserInfo
        fields = ['username', 'password', 'token']


class UserSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='user-detail', read_only=True, lookup_field='username', lookup_url_kwarg='username')
    token = ReadOnlyField(source='token.token')
    password = CharField(write_only=True)
    class Meta:
        model = models.UserInfo
        lookup_field = 'username'
        fields = ['url', 'username', 'password', 'token']


class UserDetailSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='user-detail', read_only=True, lookup_field='username', lookup_url_kwarg='username')
    class Meta:
        model = models.UserInfo
        fields = ['url', 'username', 'password']


class WordsSerializer(ModelSerializer):
    # translates = SerializerMethodField()
    translates = SlugRelatedField(many=True, queryset=models.Translates.objects.all(), slug_field='translate')

    def get_translates(self, row):
        translates_obj_list = row.translates.all()
        print(translates_obj_list)
        ret = []
        for item in translates_obj_list:
            ret.append(item.translate)
        return ret
    class Meta:
        model = models.Words
        fields = ['word', 'translates']
