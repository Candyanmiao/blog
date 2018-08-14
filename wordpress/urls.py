#coding=utf-8
from django.conf.urls import url

from wordpress import views

urlpatterns = [

    url(r'^$', views.query),
    url(r'^page/(\d+)', views.query),
    url(r'^post/(\d+)', views.category),
    url(r'^category/(\d+)', views.showcategory),
    url(r'^archive/(\d+)/(\d+)', views.s_showcategory),

]