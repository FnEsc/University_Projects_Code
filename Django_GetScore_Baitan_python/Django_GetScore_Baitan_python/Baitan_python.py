# -*- coding: utf-8 -*-

from django.shortcuts import render
from .SqlCon import *
import datetime

db_table = 'bt_problems'    # 设置题目表
q_num = 3
# Create your views here.


def index(request):
    # return HttpResponse(u'这是测试问题页面，请配置SqlCon中的connection配置')
    sql = 'select * from {0} order by rand() limit {1}'.format(db_table, q_num)
    try:
        con = connection.Con()  # con是一个class对象
        cursor = con.con.cursor()   # con.con是数据库连接对象，cursor在class(con)对象里的初始化函数里
        cursor.execute(sql)
        rs = cursor.fetchall()
        i = 1
        exam_div = ''
        for row in rs:
            exam_temp = '''
                <div class="item"><div class="title">
                    <h5>%s、%s
                    <select class="form-control opt opt%s" name="%s">
                        <option value="0">请选择</option>
                        <option value="A">A</option>
                        <option value="B">B</option>
                        <option value="C">C</option>
                        <option value="D">D</option>
                    </select></h5></div>
                    <div class="content">%s</div><br>
                </div>
            ''' % (str(i), row[1], str(i), str(row[0]), row[2])
            exam_div += exam_temp
            i += 1
        return render(request, '../templates/exam.html', {"exam_div": exam_div})
    except Exception as e:
        print(e)
        return render(request, '../templates/exam.html', {"exam_div": '<h3>链接数据库失败，请联系站长：SmLin97@outlook.com</h3></br>'})


def check(request):
    request_dict = {}
    wr_q = []
    total = 0
    message = ''

    if request.method == 'POST':
        concat = request.POST
        # print(concat) # <QueryDict: {'csrfmiddlewaretoken': ['yPX1...GU8'], '1': ['B'], '40': ['A'], '39': ['A']}>
        try:
            con = connection.Con()
            cursor = con.con.cursor()
            for i, j in concat.items():
                if i == 'csrfmiddlewaretoken':
                    continue
                sql = "SELECT * FROM {0} WHERE id='{1}'".format(db_table, i)
                cursor.execute(sql)
                rs = cursor.fetchall()[0]
                if rs[3] == j:
                    total += 1
                else:
                    wr_q.append([rs[0], rs[1], rs[2], rs[3]])  # wr_q = [[id, title, options, flag],]

            dtdemo = '%Y-%m-%d %H:%M:%S'
            sql_insert = "INSERT into bt_record(award, win_date) values ({0}, '{1}')"
            sql_insert = sql_insert.format(total, datetime.datetime.now().strftime(dtdemo))
            print(sql_insert)
            cursor.execute(sql_insert)
            con.con.commit()    # con.con是数据库链接对象

        except Exception as e:
            print(e)
            con.con.rollback()  # con.con是数据库链接对象，回滚
            message = '<h3>链接数据库失败，请联系站长：SmLin97@outlook.com</h3></br>'
        if total > 0:
            message = '<h3>答对了' + str(total) + '道题目哦！</h3></br>'
        else:
            message = '<h3>一道题都没答对。</h3></br>'
    else:
        message = '<h3>同学，想搞事情吗？</h3></br>'
    request_dict.update({'Message': message, 'total': total, 'wr_q': wr_q})
    return render(request, '../templates/check.html', request_dict)

