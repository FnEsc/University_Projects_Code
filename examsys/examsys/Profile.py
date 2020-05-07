# -*- coding: utf-8 -*-

from django.shortcuts import render
from examLibrary import DB_con,examContext
from django.shortcuts import HttpResponse
from examLibrary import DapLoggerFunc

profile_DB_Con = DB_con.DB_con()


def examExit(errorCode, ErrorMsg):
    examContext.errorCode, examContext.errorMsg = errorCode, ErrorMsg
    return False if errorCode!="0000" else True


def profile(request):
    ctx={}
    ctx.update({"errorMsg": examContext.errorMsg})
    return render(request, "profile.html", ctx)

def setmyinfo(request):
    ctx={}
    ctx.update({"errorMsg":examContext.errorMsg,"username":examContext.username,"nickname":examContext.nickname})
    return render(request, "setmyinfo.html", ctx)

def setmyinfoPage(request):
    ctx={}
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    newnickname = request.POST['nickname']
    print(examContext.username)
    try:
        rs = profile_DB_Con.DB_Userinfo_Select(examContext.username, oldpassword)
        if rs:
            DapLoggerFunc.examInfo("验证旧密码通过: username=%s verify access!" % examContext.username)
            # 更新密码
            rs = profile_DB_Con.DB_Userinfo_Password_Update(examContext.username, newpassword)
            # 更新Nickname
            if rs:
                if newnickname == examContext.nickname:
                    examContext.errorMsg = "新旧账号昵称一致，无需修改..."
                    DapLoggerFunc.examInfo(examContext.errorMsg)
                    ctx.update({"errorCode": "0000", "errorMsg": examContext.errorMsg,"refresh_url": "profile"})
                    return render(request, "SysInfomation.html", ctx)
                else:
                    rs = profile_DB_Con.DB_Userinfo_Nickname_Update(examContext.username, newnickname)
                    if rs:
                        examContext.nickname = newnickname
                        examContext.errorMsg = "setmyinfo succeed!"
                        DapLoggerFunc.examInfo(examContext.errorMsg)
                        ctx.update({"errorCode": examContext.errorCode, "errorMsg": examContext.errorMsg,
                                    "refresh_url": "profile"})
                        return render(request, "SysInfomation.html", ctx)
                    else:
                        examContext.errorCode, examContext.errorMsg = "0009", "Something error:..."
                        DapLoggerFunc.examError(examContext.errorMsg)
                        ctx.update({"errorCode": examContext.errorCode, "errorMsg": examContext.errorMsg,"refresh_url": "setmyinfo"})
                        return render(request, "SysInfomation.html", ctx)

            else:
                DapLoggerFunc.examError(examContext.errorMsg)
                ctx.update({"errorCode": examContext.errorCode, "errorMsg": examContext.errorMsg, "refresh_url": "setmyinfo"})
                return render(request, "SysInfomation.html", ctx)
        else:
            examContext.errorCode, examContext.errorMsg = "0008", "Something error: 验证旧密码失败!"
            DapLoggerFunc.examError(examContext.errorMsg)
            ctx.update({"errorCode": examContext.errorCode, "errorMsg": examContext.errorMsg, "refresh_url": "setmyinfo"})
            return render(request, "SysInfomation.html", ctx)

    except Exception as e:
        examContext.errorCode,examContext.errorMsg = "0007","Something error: "+str(e)
        DapLoggerFunc.examError(examContext.errorMsg)
        ctx.update({"errorCode": examContext.errorCode, "errorMsg": examContext.errorMsg, "refresh_url": "setmyinfo"})
        return render(request, "SysInfomation.html", ctx)