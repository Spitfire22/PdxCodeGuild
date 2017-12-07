from django.contrib import admin

from .models import Book, UserCheckout



admin.site.register(Book)
admin.site.register(UserCheckout)
