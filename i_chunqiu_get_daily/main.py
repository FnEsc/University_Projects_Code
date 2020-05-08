# -*- coding: utf-8 -*-
"""
Date: 2018-12-08
Version: 2.0
Author: FnEsc
"""
import configparser
import time
from selenium import webdriver

class Login_i(object):
    """To login in www.ichunqiu.com"""
    def __init__(self):
        print("To login in www.ichunqiu.com...")
        time.sleep(2)
    def get_info(self):
        # 读取用户信息
        # config = configparser.ConfigParser()
        # config.read(u"userinfo.ini")
        # i_user = config.get("user_info","i_user")
        # i_password = config.get("user_info","i_password")
        i_user = "18218431031"
        i_password = "topL0622"
        print("获取i春秋账号密码成功！")
        time.sleep(2)
        # 浏览器登录模块
        print("正在打开浏览器模拟登录i春秋...")
        time.sleep(2)
        # 修改后台打开
        # options = webdriver.ChromeOptions() # 后台打开
        # options.add_argument('--disable-extensions')
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--no-sandbox')
        # browser = webdriver.Chrome(chrome_options=options) # chrome_options=option后台打开
        # end修改
        browser = webdriver.Chrome()
        browser.get("https://user.ichunqiu.com/login")
        time.sleep(5)
        # usename = browser.find_element_by_id("username")
        # usename.send_keys(i_user)
        usename = browser.find_elements_by_class_name("input_account")[0]
        usename.send_keys(i_user)
        # psd = browser.find_element_by_id("password")
        # psd.send_keys(i_password)
        psd = browser.find_elements_by_class_name("input_password")[0]
        psd.send_keys(i_password)

        time.sleep(2)
        commit = browser.find_elements_by_class_name("login_btn")[0]
        commit.click()
        time.sleep(8)
        # 判断登录成功
        if browser.current_url=="https://www.ichunqiu.com/" :
            print("登录成功！")
        # 检查有没有小提示
        # if (browser.find_element_by_class_name("robot-Img-maskimg")):
        #     browser.find_element_by_class_name("robot-Img-maskimg").click()
        #     print("关闭小提示成功！")
        # 开始获取经验
        # browser.find_element_by_class_name("robot-Img").click()
        browser.find_element_by_id("robot-unnormal").click()
        time.sleep(5)
        print("获取任务列表成功！")
        task_list_0 = browser.find_element_by_id("getAward")
        task_list_0.click()
        print("获取泉币成功！")
        time.sleep(1)
        browser.close()
        browser.quit()
        print("Finish!")


if __name__ == '__main__':
    Login_i_obj = Login_i()
    Login_i_obj.get_info()
