from django.db import models


WORKDAY_CODE = 1
HOLIDAY_CODE = 2
WEEKEND_CODE = 3


class Date(models.Model):
    DATE_TYPE_CHOICES = (
        (1, "元旦"),
        (2, "春节"),
        (3, "清明节"),
        (4, "劳动节"),
        (5, "端午节"),
        (6, "中秋节"),
        (7, "国庆节"),
        (8, "调休"),
    )
    date = models.DateField()
    store_date_type = models.IntegerField(choices=DATE_TYPE_CHOICES)
    date_code = models.IntegerField(default=HOLIDAY_CODE)

    @property
    def date_type(self):
        return self.get_store_date_type_display()

    @date_type.setter
    def date_type(self, data):
        self.store_date_type = data
        if data == 8:
            self.date_code = WORKDAY_CODE
