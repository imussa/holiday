from rest_framework.serializers import *
from . import models


class HolidaySerializer(ModelSerializer):
    class Meta:
        model = models.Date
        fields = ['date', 'date_code', 'date_type']
