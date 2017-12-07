from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Book, UserCheckout
from django.utils import timezone

def index(request):
    library_books = Book.objects.all()
    books_checkedout = UserCheckout.objects.all()
    this_book = {'library_books': library_books,'books_checkedout':books_checkedout}

    return render(request, 'library/index.html', this_book)

def savebook(request):
    library_books = Book.objects.all()
    user = request.POST['user_checkout']
    for book in library_books:
        if 'book'+str(book.id) in request.POST:
            print(book.id, ' is checked')
            if book.available == True:
                book.available = False
                checkout_book = UserCheckout(checkout=True, book=book, user=user, timestamp=timezone.now())
                checkout_book.save()
        else:
            print(book.id, ' is unchecked')
            if book.available == False:
                book.available = True
                checkin_book = UserCheckout(checkout=False, book=book, user=user, timestamp=timezone.now())
                checkin_book.save()
        book.save()

    # iterate through the books to see if the ID is contained within the POST dict

    return HttpResponseRedirect(reverse('library:index'))

def bookhistory(request):
    books_checkedout = UserCheckout.objects.all()
    this_book = {'books_checkedout':books_checkedout}
    return render(request, 'library/bookhistory.html', this_book)
