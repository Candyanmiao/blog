# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.core.paginator import Paginator
from django.shortcuts import render

from models import *

# Create your views here.
def query(request,num=1):
    # num  = request.GET.get('num',1)
    num= int(num)
    print num
    print type(num)
    postList = Post.objects.all().order_by('-created')
    paginator=Paginator(postList,1)
    pageList = paginator.page(num)
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    end = begin + 9
    if end > paginator.num_pages:
        end = paginator.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pagelist = range(begin, end + 1)

    return render(request,'index.html',{'postList':pageList,'pageList':pagelist,'currentNum':num})


def category(request,pid):
    pid = int(pid)
    post= Post.objects.get(id =pid)

    return render(request,'category.html',{'post':post})


def showcategory(request,cid):
    postlist = Post.objects.filter(id = cid)
    return render(request,'showcategory.html',{'postlist':postlist})


def s_showcategory(request,y,m):
    postlist = Post.objects.filter(created__year=y,created__month=m)

    # p = Post.objects.filter(created__year=y)
    # q = Post.objects.filter(created__month=m)
    # print p
    # print q
    return render(request, 'showcategory.html', {'postlist': postlist})