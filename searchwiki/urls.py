from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^search/$', views.search_list, name='search_list'),
    # path('movie/<id>', views.details, name='details')
    re_path(r'^search/(?P<string>.+)/$', views.download, name='details'),
    re_path(r'^download/(?P<string>.+)/$', views.download, name='download')
]