from django.db import models

class UrlShortened(models.Model):
    long_url = models.CharField(max_length=300)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code + ' ' + self.long_url
