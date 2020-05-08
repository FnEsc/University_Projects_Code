#-*-coding:utf-8-*-
import requests
import re

# 匹配样例
title_pattern = '<div class="single-newstitle">.+</div>'
date_pattern = '<div class="single-newstime">.+</div>'

for index in range(15870, 15901):
    url = 'http://web.fosu.edu.cn/xueyuan-news/' + str(index) + '.html'
    r = requests.get(url)
    if r.status_code == 200 :
        # url正确，获取内容
        html_text = r.text
        # 开始搜索标题
        match_title = re.search(title_pattern,html_text).group()
        l = len(match_title)
        title = match_title[30:l-6]
        print title
        # 开始搜索时间
        match_date = re.search(date_pattern,html_text).group()
        l = len(match_date)
        date = match_date[29:l-6]
        print  date
        # 换行循环
        print ''





