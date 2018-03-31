from django.urls import path
from django.conf.urls import url

from frontend import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    #url(r'^article/$',views.article ,name='article'),
]
