import datetime

from django.db import models
from django.utils import timezone

class Book(models.Model):
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    available = models.BooleanField(default=True)
    published = models.DateTimeField()

    def __str__(self):
        return f'{self.author}  by: {self.book} is available: {self.available}'



class UserCheckout(models.Model):
    user = models.CharField(max_length=60)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateTimeField('Last Check In/Out:', auto_created=True)

    def checkout_timestamp(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.timestamp <= now

    def __str__(self):
        return f'{self.user} selected: {self.book} on: {self.timestamp} user has book: {self.checkout}'


