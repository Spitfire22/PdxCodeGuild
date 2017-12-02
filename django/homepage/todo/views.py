from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import TodoItem

def index(request):

    todo_items = TodoItem.objects.all()

    # output = '<html><head></head><body>'
    # output += '<ul>'
    #
    # for todo_items in todo_items:
    #     print(todo_items.todo_text)
    #     output += f'<li>{todo_items.todo_text}</li>'
    # output += '</ul>'
    # output += '</body></html>'
    #
    # return HttpResponse(output)

    context = {'todo_items': todo_items}

    return render(request, 'todo/index.html', context)

def temp(request):
    return HttpResponse('Temperature')

def list(request):
    return HttpResponse('This isn\'t a list...')

def savetodo(request):

    todo_text = (request.POST['todo_text'])

    todo_item = TodoItem(todo_text=todo_text)
    todo_item.save()

    return HttpResponseRedirect(reverse('todo:index'))

