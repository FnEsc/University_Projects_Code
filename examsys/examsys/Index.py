# -*- coding: utf-8 -*-

from django.shortcuts import render
from examLibrary import DB_con,examContext
from django.shortcuts import HttpResponse

index_DB_Con = DB_con.DB_con()

# 接收POST请求数据
def index(request):
    ctx={}
    return render(request,"index.html",ctx)

def verify(request):
    ctx={}
    username = request.POST['username']
    password = request.POST['password']
    rs = index_DB_Con.DB_Userinfo_Select(username,password)
    if rs:

        # return HttpResponse("SysInfomation: DB_Userinfo_Select-> Verify Succeed! uid=%s,username=%s,nickname=%s,ismaster=%s" % rs[0])
        ctx.update({"errorCode":examContext.errorCode,"errorMsg":examContext.errorMsg,"refresh_url":"profile"})
        return render(request, "SysInfomation.html", ctx)
    else:
        # return HttpResponse("SysInfomation: DB_Userinfo_Select-> Verify Failed! username=%s,password=%s" % (username, password))
        examContext.errorCode, examContext.errorMsg = "0001", "SysInfomation: DB_Userinfo_Select-> Verify Failed!"
        ctx.update({"errorCode": examContext.errorCode, "errorMsg": examContext.errorMsg, "refresh_url": "index"})
        return render(request, "SysInfomation.html", ctx)
def register(request):
    ctx={}
    return render(request,"register.html",ctx)

def registerPage(request):
    ctx={}
    username = request.POST['username']
    password = request.POST['password']
    nickname = request.POST['nickname']
    ismaster = request.POST['ismaster'] if 'ismaster' in request.POST else '0'
    rs = index_DB_Con.DB_Userinfo_Insert(username, password,nickname,ismaster)
    if rs:
        ctx.update({"errorCode": "0000", "errorMsg": examContext.errorMsg, "refresh_url": "index"})
        return render(request,"SysInfomation.html",ctx)
    else:
        ctx.update({"errorCode":"0002","errorMsg":examContext.errorMsg,"refresh_url":"register"})
        return render(request,"SysInfomation.html",ctx)

