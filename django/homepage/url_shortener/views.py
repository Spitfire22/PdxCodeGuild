from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import random


def url_shortener(request):
    return render(request, 'url_shortener/index.html')


def save_url(request):
    print(request.POST['url_input'])
    return HttpResponse('alrighty then')

def create_short():
    char_list = []