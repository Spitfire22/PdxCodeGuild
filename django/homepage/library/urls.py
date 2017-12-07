from django.conf.urls import url
from . import views

app_name = 'library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'savebook/$', views.savebook, name='savebook'),
    url(r'bookhistory/$', views.bookhistory, name='bookhistory'),
    # url(r'/redirect')
]