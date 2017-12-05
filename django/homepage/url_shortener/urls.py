from django.conf.urls import url
from . import views

app_name = 'url_shortener'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save_url/$', views.save_url, name='save_url'),
    url(r'^(?P<code>[a-zA-Z0-9]+)/$', views.redirect, name='redirect')

]


#     url(/redirect/r'^P<char&nums_shortened[a-z][0-9][A-Z]+)/$>, views.redirect, name='redirect')