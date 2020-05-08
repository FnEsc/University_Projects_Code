# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

# item0模板
demo='''
    <html>
    <!DOCTYPE html>
    <html lang="en" class="no-js">
        <head>
            <meta charset="utf-8">
            <title>成绩(Score)</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="">
            <meta name="author" content="">
            <!-- CSS -->
            <link rel="stylesheet" href="assets/css/reset.css">
            <link rel="stylesheet" href="assets/css/supersized.css">
            <link rel="stylesheet" href="assets/css/style.css">
            <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
            <!--[if lt IE 9]>
                <script src="assets/js/html5.js"></script>
            <![endif]-->
        </head>
        <body>
            <div class="page-container">
                <h1>成绩(Score)</h1>
                <form action="" method="get">
                    <div class="error"><span></span></div>
                </form>
                <div class="connect">
                    <!-- <p>快捷</p> -->
                </div>
                <div>
        {}
        {}
                </div>
            </div>
            <!-- Javascript -->
            <script src="assets/js/jquery-1.8.2.min.js" ></script>
            <script src="assets/js/supersized.3.2.7.min.js" ></script>
            <script src="assets/js/supersized-init.js" ></script>
            <script src="assets/js/scripts.js" ></script>
        </body>
    <div style="text-align:center;margin:20 0;">
        <p>来源：<a href="http://www.linkeos.xin/" title="G.E.M邓紫棋" target="_blank">G.E.M邓紫棋&nbsp;&nbsp;粉丝制作</a></p>
    </div>
    </html>
'''

def toresult():
    with open('./myscore.html','r',encoding='utf-8') as f1:
        score_html=f1.read()

    # 处理字段
    ### 此处用BeautifulSoup获取
    soup = BeautifulSoup(score_html, 'html.parser') # 初始化函数，变量 score_html 是我们获取的页面代码，第二个参数是固定的，表示识别html代码
    stdname = soup.select('.Nsb_top_menu_nc')[0] # 获取姓名
    match_content = soup.select('.Nsb_layout_r')[0] # 获取类为 Nsb_layout_r 的内容,此处不需要进行".encode('utf-8')"处理
    myscore=match_content

    myscore_html=demo.format(stdname,myscore)

    # 优化页面
    myscore_html=myscore_html.replace('<th class="Nsb_r_list_thb" scope="col">备注</th>','').replace('修读中','N').replace('待修读','N').replace('<td>必修</td>','<td align="center">必修</td>').replace('<td>公选</td>','<td align="center">公选</td>').replace('<td>其他</td>','<td align="center">其他</td>').replace('<td>任选</td>','<td align="center">任选</td>').replace('<td>限选</td>','<td align="center">限选</td>').replace('<td>其它</td>','<td align="center">其它</td>').replace('<a href="/jsxsd/framework/main.jsp">首页</a>&gt;&gt;学籍信息&gt;&gt;学习完成情况查看','').replace("color: #000000;","color: #fff;")

    with open('./html5_login/templet.html','w',encoding='utf-8') as f2:
        f2.write(myscore_html)

if __name__ == '__main__':
    toresult()
    print("Toresult->Done")
