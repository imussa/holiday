from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict
import datetime
from . import models
from . import serializers


class HolidayView(APIView):
    def get(self, request, *args, **kwargs):
        date = request.query_params.get('date', datetime.date.today())
        if not isinstance(date, datetime.date):
            try:
                date = datetime.datetime.strptime(date, '%Y%m%d').date()
            except Exception as e:
                return Response(OrderedDict([('detail', str(e))]), status=status.HTTP_400_BAD_REQUEST)
        instance = models.Date.objects.filter(date=date).first()
        if not instance:
            if date.isoweekday() in [6, 7]:
                instance = OrderedDict([('date', date), ('date_code', models.WEEKEND_CODE), ('date_type', '周末')])
            else:
                instance = OrderedDict([('date', date), ('date_code', models.WORKDAY_CODE), ('date_type', '工作日')])
        serializer = serializers.HolidaySerializer(instance)
        return Response(serializer.data)
