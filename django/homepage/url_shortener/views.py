from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import UrlShortened

import random

charlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def index(request):
    urls = UrlShortened.objects.all()
    context = {'urls': urls}
    return render(request, 'url_shortener/index.html', context)


def redirect(request, code):
    redirection = get_object_or_404(UrlShortened, code=code)
    return HttpResponseRedirect(redirection.long_url)

# make a view to redirect
    # get the code from the path (capture group)
    # look up the row in the database with that code
    # redirect to the corresponding long url



def save_url(request):
    long_url = (request.POST['url_input'])

    gen_code = ''
    i = 0
    while i < 6:
        gen_code += random.choice(charlist)
        i += 1

    item = UrlShortened(long_url=long_url, code=gen_code)
    item.save()

    return HttpResponseRedirect(reverse('url_shortener:index'))

    ### get the long url from the post request
    # generate a short code
    ### create a UrlShortened object from both
    ### save that
    ### redirect to the index page



