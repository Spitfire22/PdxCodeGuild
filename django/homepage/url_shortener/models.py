from django.db import models

class urlShortener(models.Model):
    url_text = models.CharField(max_length=300)

    def __str__(self):
        return self.url_text
