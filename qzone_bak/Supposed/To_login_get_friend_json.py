# -*- coding: utf-8 -*-
import configparser
import re
import time
import json
import requests
from selenium import webdriver

class Login_get_friends_json(object):
    def __init__(self):
        print("正在获取QQ信息...")
    def login_get_friend_json(self):
        # 读取qq账号密码模块
        config = configparser.ConfigParser()
        config.read(u"userinfo.ini")
        qq_number = config.get("user_info","qq_number")
        qq_password = config.get("user_info","qq_password")
        print("获取QQ账号密码成功！")
        time.sleep(2)
        # 浏览器登录模块
        print("正在登录QQ空间...")
        browser = webdriver.Chrome()
        browser.get("http://i.qq.com")
        time.sleep(3)
        browser.switch_to_frame("login_frame")
        loginclick = browser.find_element_by_id("switcher_plogin")
        loginclick.click()
        username = browser.find_element_by_id("u")
        username.send_keys(qq_number)
        psd = browser.find_element_by_id("p")
        psd.send_keys(qq_password)
        commit = browser.find_element_by_id("login_button")
        commit.click()
        time.sleep(5)
        # 判断登录成功
        url_now = browser.current_url
        pattern = re.compile("^https://user.qzone.qq.com/")
        if bool(re.match(pattern,url_now)) :
            print("登录QQ空间成功！")
        else :
            print("登录QQ空间失败！")
            raise TimeoutError("登录失败，可能需要验证，未能跳过！")
        # 获取cookie
        cookie_list = browser.get_cookies()

        browser.close()
        browser.quit()
        print("获取cookie成功")

        with open('cookie.json','w',encoding='utf-8') as f:
            json.dump(cookie_list,f)

        cookie = ""
        for elem in cookie_list : cookie += elem["name"]+"="+elem["value"]+";"

        p_skey = cookie[cookie.find('p_skey=')+7:cookie.find(';', cookie.find('p_skey='))]
        # print(p_skey)
        h=5381
        for i in p_skey:
            h+=(h<<5)+ord(i)
        g_tk=h&2147483647

        # print(g_tk)

        print("现在开始获取好友账号...")
        # 下载好友账号文件
        friends_url_demo = """https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/right/get_entryright.cgi?uin={}&ver=1&g_tk={}"""
        friends_url = friends_url_demo.format(qq_number,g_tk)
        # print(friends_url)
        # 得到好友的header
        headers_getfriends = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'cache-control':'no-cache',
            'pragma':'no-cache',
            'referer':'https://qzs.qzone.qq.com/qzone/v5/loginsucc.html?para=izone&from=iqq',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
            }
        cookie_dict = {'cookie':cookie}
        headers_getfriends.update(cookie_dict)

        r = requests.get(friends_url,headers=headers_getfriends)
        html_text = r.text
        html_text = html_text.replace('\n','')
        # print(html_text)
        # 判断能否访问json
        if "\"friendlist\"" in html_text:
            with open ('friendsjson.json','w',encoding='utf-8') as f :
                json.dump(html_text,f)
            print("成功获取好友列表！")
        else :
            raise TimeoutError("获取好友列表失败...")