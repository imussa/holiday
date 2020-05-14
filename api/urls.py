from django.urls import path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'auth')


urlpatterns = [
    re_path('^(?P<version>[v1|v2]+)/user/$', views.UserView.as_view()),
    re_path('^(?P<version>[v1|v2]+)/words/$', views.WordsView.as_view()),
    re_path('^(?P<version>[v1|v2]+)/user/(?P<username>\w+)/$', views.UserDetailView.as_view(), name='user-detail'),
]
