import datetime

from django.db import models
from django.utils import timezone

class TheLibrary(models.Model):
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    available = models.BooleanField(default=True)
    user = models.CharField(max_length=60)
    timestamp = models.DateTimeField('Last Check In/Out:', auto_created=True)

    def __str__(self):
        return f'{self.author}  by: {self.book} is available: {self.available}'

    def checkout_timestamp(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.timestamp <= now