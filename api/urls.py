from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('^(?P<version>[v1|v2]+)/holiday/$', views.HolidayView.as_view()),
]
