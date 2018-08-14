#coding=utf-8
from django.db.models import Count

from wordpress.models import Post


def getRightInfo(request):
    r_catepost=Post.objects.values('category__cname','category').annotate(c =Count('*')).order_by('-c')
    r_recpost = Post.objects.all().order_by('-created')[:3]

    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT created,COUNT('*') c FROM t_post GROUP BY DATE_FORMAT(created,'%Y-%m') ORDER BY c desc,created desc")
    rfilepost = cursor.fetchall()
    return {'r_catepost':r_catepost,'r_recpost':r_recpost,'rfilepost':rfilepost}