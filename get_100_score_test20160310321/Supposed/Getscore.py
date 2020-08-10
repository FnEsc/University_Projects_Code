#-*-coding:utf-8-*-
import requests
import time
from selenium import webdriver
import re
import json

def getscore(myusername='study number',mypassword='******'):
    url='http://100.fosu.edu.cn/jsxsd/'
    print("正在登录100网...")
    options = webdriver.ChromeOptions() # 后台打开
    options.add_argument('headless')
    browser = webdriver.Chrome() # chrome_options=options后台打开
    browser.get(url)
    time.sleep(1)
    username = browser.find_element_by_id("userAccount")
    username.send_keys(myusername)
    psd = browser.find_element_by_id("userPassword")
    psd.send_keys(mypassword)
    commit = browser.find_element_by_id("btnSubmit")
    commit.click()
    time.sleep(1)
    # 判断登录成功
    if (browser.current_url=='http://100.fosu.edu.cn/jsxsd/framework/xsMain.jsp') :
        print("登录成功！")
    else :
        print("登录失败！")
    # 获取cookie
    cookie_list = browser.get_cookies()
    time.sleep(2)

    with open('cookie.json','w',encoding='utf-8') as f:
        json.dump(cookie_list,f)

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
    html_text=browser.page_source
    print("获取成绩成功")
    logout = browser.find_element_by_class_name("Nsb_top_menu_exit")
    logout.click()
    time.sleep(1)

    browser.close()
    browser.quit()

    with open('myscore.html','w',encoding='utf-8') as f:
        f.write(html_text)
    print("Done")

if __name__ == '__main__':
    getscore()
    print("Getscore->Done")
