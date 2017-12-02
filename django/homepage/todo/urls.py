from django.conf.urls import url

from . import views
# the 'from .' is the current directory where this file is located.

app_name = 'todo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'temp/$', views.temp),
    url(r'list/$', views.list),
    url(r'savetodo/$', views.savetodo, name='savetodo'),
]
