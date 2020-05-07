# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re
import base64

vpn_url='https://vpn.fosu.edu.cn/por/login_psw.csp/por/login_psw.csp?svpn_name=20160310321&svpn_password=123456798'
vpn_100='https://vpn.fosu.edu.cn/web/1/http/0/100.fosu.edu.cn/jsxsd/xk/LoginToXk'
vpn_100_score='https://vpn.fosu.edu.cn/web/1/http/0/100.fosu.edu.cn/jsxsd/xxwcqk/xxwcqkOnkcxz.do'
vpn_100_logout='https://vpn.fosu.edu.cn/web/1/http/0/100.fosu.edu.cn/jsxsd/xk/LoginToXk?method=exit'
vpn_logout='https://vpn.fosu.edu.cn/por/logout.csp'
headers={'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'} #模拟手机端

# 接收POST请求数据
def main_get(request):
    if request.POST:
        myusername = request.POST['username']
        mypassword = request.POST['password']
        s=requests.session()
        res = s.get(vpn_url,headers=headers,verify=False) # get方法登录vpn
        # std={'encoded':str(base64.b64encode(myusername.encode('utf-8')),'utf-8')+"%%%"+str(base64.b64encode(mypassword.encode('utf-8')),'utf-8')} # 这是py3
        std={'encoded':str(base64.b64encode(myusername.encode('utf-8')))+"%%%"+str(base64.b64encode(mypassword.encode('utf-8')))} # 这是py2
        res2 = s.post(vpn_100,headers=headers,data=std,verify=False) # 登录100学生账号
        # print('登录100网...')
        if 'Nsb_top_menu_nc' in res2.text : # 登录100成功
            # print('登录100网成功...')
            # 处理字段
            ### 此处用BeautifulSoup获取
            res3 = s.get(vpn_100_score,headers=headers,verify=False) # 这里是成绩页面
            score_html=res3.text
            soup = BeautifulSoup(score_html, 'html.parser') # 初始化函数，变量 score_html 是我们获取的页面代码，第二个参数是固定的，表示识别html代码
            stdname = str(soup.select('.Nsb_top_menu_nc')[0]).replace("color: #000000;","color: #fff;") # 获取姓名
            myscore = str(soup.select('.Nsb_layout_r')[0]).replace('<th class="Nsb_r_list_thb" scope="col">备注</th>','').replace('修读中','N').replace('待修读','N').replace('<td>必修</td>','<td align="center">必修</td>').replace('<td>公选</td>','<td align="center">公选</td>').replace('<td>其他</td>','<td align="center">其他</td>').replace('<td>任选</td>','<td align="center">任选</td>').replace('<td>限选</td>','<td align="center">限选</td>').replace('<td>其它</td>','<td align="center">其它</td>').replace('<a href="/web/1/http/1/100.fosu.edu.cn/jsxsd/framework/main.jsp">首页</a>&gt;&gt;学籍信息&gt;&gt;学习完成情况查看','')  # 获取类为 Nsb_layout_r 的内容,此处不需要进行".encode('utf-8')"处理
            # 优化页面
            context          = {}
            context['name'] = stdname
            context['score'] = myscore
            # 准备退出100网和vpn
            res4 = s.get(vpn_100_logout,headers=headers,verify=False)
            res5 = s.get(vpn_logout,headers=headers,verify=False)

            return render(request, 'result.html', context)
        else : # 登录失败
            rlt={}
            rlt['rlt1']='密码错误'
            return render(request, 'index.html', rlt)

    # 没有收到post
    else :
        context          = {}
        context['name'] = '<h3>Who am I？</h3>'
        context['score'] = '<h5><a href="/index">点击访问查询页面Please</a></h5>'
        return render(request, 'result.html', context)