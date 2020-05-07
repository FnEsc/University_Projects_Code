# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

# 接收POST请求数据
def index(request):
    ctx={}
    return render(request,"index.html",ctx)