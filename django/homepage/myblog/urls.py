from django.conf.urls import url
from . import views

appname = 'myblog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new_user/$', views.new_user, name='new_user')
]