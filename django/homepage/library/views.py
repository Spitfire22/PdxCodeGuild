from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import TheLibrary
from datetime import datetime

def index(request):
    library_books = TheLibrary.objects.all()

    this_book = {'library_books': library_books}

    return render(request, 'library/index.html', this_book)

def savebook(request):
    user_checkout = (request.POST['user_checkout'])

    ## have datestamp change when checked in or out
    ## change

    library_books = TheLibrary.objects.all()
    for book in library_books:
        if 'book'+str(book.id) in request.POST:
            print(book.id, ' is checked')
            if book.available == True:
                book.timestamp = datetime.now()
            book.available = False
        else:
            print(book.id, ' is unchecked')
            if book.available == False:
                book.timestamp = datetime.now()
            book.available = True
        book.save()

    # iterate through the books to see if the ID is contained within the POST dict

    return HttpResponseRedirect(reverse('library:index'))


