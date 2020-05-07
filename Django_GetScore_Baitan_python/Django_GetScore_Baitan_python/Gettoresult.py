# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import re
import json

# def gettoresult(myusername='20160310321',mypassword='topL0622'):
def gettoresult(request):
    myusername='20160310321'
    mypassword='topL0622'
    option = webdriver.ChromeOptions() # 后台打开
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option) # chrome_options=option后台打开
    browser.get('http://100.fosu.edu.cn/jsxsd/')
    time.sleep(1)
    username = browser.find_element_by_id("userAccount")
    username.send_keys(myusername)
    psd = browser.find_element_by_id("userPassword")
    psd.send_keys(mypassword)
    commit = browser.find_element_by_id("btnSubmit")
    commit.click()
    time.sleep(1)
    # 判断登录成功
    # 获取cookie
    cookie_list = browser.get_cookies()
    time.sleep(2)

    # # 处理cookie
    # cookie=""
    # for elem in cookie_list : cookie += elem["name"]+"="+elem["value"]+";"

    # url_score='http://100.fosu.edu.cn/jsxsd/xxwcqk/xxwcqkOnkcxz.do'
    # headers_getscore={}
    # cookie_dict = {'cookie':cookie}
    # headers_getscore.update(cookie_dict)
    # r = requests.get(url_score,headers=headers_getscore)
    # print("访问成绩页面成功")
    # html_text = r.text

    browser.get('http://100.fosu.edu.cn/jsxsd/xxwcqk/xxwcqkOnkcxz.do')
    score_html=browser.page_source
    logout = browser.find_element_by_class_name("Nsb_top_menu_exit")
    logout.click()
    time.sleep(1)

    browser.close()
    browser.quit()

    # 处理字段
    ### 此处用BeautifulSoup获取
    soup = BeautifulSoup(score_html, 'html.parser') # 初始化函数，变量 score_html 是我们获取的页面代码，第二个参数是固定的，表示识别html代码
    stdname = str(soup.select('.Nsb_top_menu_nc')[0]) # 获取姓名
    myscore = str(soup.select('.Nsb_layout_r')[0]).replace('<th class="Nsb_r_list_thb" scope="col">备注</th>','').replace('修读中','N').replace('待修读','N').replace('<td>必修</td>','<td align="center">必修</td>').replace('<td>公选</td>','<td align="center">公选</td>').replace('<td>其他</td>','<td align="center">其他</td>').replace('<td>任选</td>','<td align="center">任选</td>').replace('<td>限选</td>','<td align="center">限选</td>').replace('<td>其它</td>','<td align="center">其它</td>').replace('<a href="/jsxsd/framework/main.jsp">首页</a>&gt;&gt;学籍信息&gt;&gt;学习完成情况查看','').replace("color: #000000;","color: #fff;") # 获取类为 Nsb_layout_r 的内容,此处不需要进行".encode('utf-8')"处理

    # 优化页面
    context          = {}
    context['name'] = stdname
    context['score'] = myscore
    # print(stdname)
    return render(request, 'result.html', context)


# def gettoresult(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'Hello.html', context)

if __name__ == '__main__':
    gettoresult()
