# -*- coding: utf-8 -*-
import re
import requests
import string
import json
import time
import os
import xlwt
from urllib import parse

class Get_ss_json_xls(object):
    def __init__(self):
        with open ('friendsjson.json','r') as f :
            html_text = json.load(f)

        # 此处对json文件处理得出好友账号的dict
        pattern = re.compile(r'"friendlist":.*?]')
        match = pattern.match(html_text)

        html_text = html_text.replace(" ","")
        pattern = re.compile(r'"friendlist":.*?]')
        match = pattern.findall(html_text)
        friendstr = match[0][14:-1]

        friendstunple = eval(friendstr)
        # for x in friendstunple :
        #     print(x["label"]) # 好友备注
        #     print(x["data"]) # 好友账号

        with open('cookie.json','r') as f:
            cookie_list = json.load(f)

        cookie = ""
        for elem in cookie_list : cookie += elem["name"]+"="+elem["value"]+";"

        p_skey = cookie[cookie.find('p_skey=')+7:cookie.find(';', cookie.find('p_skey='))]
        # print(p_skey)
        h=5381
        for i in p_skey:
            h+=(h<<5)+ord(i)
        g_tk=h&2147483647



        print("开始获取好友说说...")
        url='https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?'
        params = {
            "sort":0,
            "start":0,
            "num":20,
            "cgi_host": "http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6",
            "replynum":100,
            "callback":"_preloadCallback",
            "code_version":1,
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
            "format":"jsonp",
            "need_private_comment":1,
            "g_tk": g_tk
        }
        url = url + parse.urlencode(params)
        headers_get_friends_ss={
            'host': 'h5.qzone.qq.com',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.8',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'connection': 'keep-alive'
        }
        cookie_dict = {'cookie':cookie}
        headers_get_friends_ss.update(cookie_dict)

    def get_ss_json_xls(self):
        # friendstunple = eval(friendstr)
        # for x in friendstunple :
        #     print(x["label"]) # 好友备注
        #     print(x["data"]) # 好友账号

        if not os.path.exists("./friend_ss_json/"):
            os.mkdir("friend_ss_json/")
        if not os.path.exists("./friend_ss_xls/"):
            os.mkdir("friend_ss_xls/")
        for friend in friendstunple :
            friend_number = friend["data"]
            friend_name = friend["label"]
            if not os.path.exists("./friend_ss_json/"+str(friend_number)+str(friend_name)):
                os.mkdir("friend_ss_json/"+str(friend_number)+str(friend_name))
            t = True
            pos = 0
            file = xlwt.Workbook()
            table = file.add_sheet('emotion_list')
            table.write(0,0,'序号')
            table.write(0,1,'时间')
            table.write(0,2,'内容')
            while (t):
                url_friend_home = url + '&uin=' + str(friend_number) + '&pos=' + str(pos)
                r = requests.get(url=url_friend_home, headers=headers_get_friends_ss)
                html_text = r.text
                print("正在请求：好友",friend["data"],"的第",pos,"~",pos+20,"条说说...")
                if "\"msglist\":null" in r.text or "\"message\":\"对不起,主人设置了保密,您没有权限查看\"" in r.text:
                    t = False
                    break
                else:
                    with open("./friend_ss_json/"+str(friend_number)+str(friend_name)+"/"+str(friend_number)+str(friend_name)+str(pos)+"~"+str(pos+20)+'.json', 'a',encoding='utf-8') as f :
                        json.dump(html_text,f)
                    # print("完成",str(friend_number),str(friend_name),str(friend_name)+str(pos)+"~"+str(pos+20),"存入json")

                    # print(ss_all)
                    # print(type(ss_all))
                    # content
                # 现在保存xls
                ss_all = ''
                with open("./friend_ss_json/"+str(friend_number)+str(friend_name)+"/"+str(friend_number)+str(friend_name)+str(pos)+"~"+str(pos+20)+'.json',"r") as f :
                    ss_all = json.load(f)
                    # print(type(ss_all))
                    ss_all = ss_all[17:-2]
                    # print(type(ss_all))
                    js=json.loads(ss_all)
                    # print(type(js))
                # 正则匹配content
                # patten_content = re.compile(r'"conlist":.*?}')
                # match_content = patten_content.findall(mmss_all)
                # match_content_list = []
                # for x in match_content :
                #     match_content_list.append(x[19:-11].replace(r"\n",''))
                # json引入
                match_content_list = []
                for s in js['msglist']:
                    # print(s)
                    match_content_list.append(s['content'])
                # 正则匹配time
                patten_time = re.compile(r'created_time":.*?,')
                match_time = patten_time.findall(ss_all)
                match_time_list = []
                for x in match_time :
                    timestamp = x[14:-1]
                    timestamp = int(timestamp)
                    time0 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)))
                    match_time_list.append(time0)
                # json引入time错误
                # match_time_list = []
                # for s in js['msglist']:
                #     timestamp = s['created_time']
                #     timestamp = int(timestamp)
                #     time0 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)))
                #     match_content_list.append(time0)
                # print(match_time_list)
                # print(match_content_list)

                save_number = min(len(match_content_list),len(match_time_list))
                for i in range(save_number) :
                    table.write(pos+i+1,0,pos+i+1)
                    table.write(pos+i+1,1,match_time_list[i])
                    table.write(pos+i+1,2,match_content_list[i])

                pos += 20


            file.save("./friend_ss_xls/"+str(friend_number)+str(friend_name)+'.xls')
            print("完成",str(friend_number),str(friend_name),"存入Excel")

            time.sleep(2)
