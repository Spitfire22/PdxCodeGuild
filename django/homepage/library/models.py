from django.db import models

class TheLibrary(models.Model):
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=60)

    def __str__(self):
        return self.author + ' ' + self.book
