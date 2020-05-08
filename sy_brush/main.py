# -*- coding: utf-8 -*-
'''
url: http://learn.shengyuan.com
Date: 2018-10-10
Author: FnEsc
Email: SmLin97@outlook.com
Version：2.2
describe：Use the package "selenium" to request web pages automatically, and get questions' pages and answers' pages, then save them to xls!
'''
import re
import time
import xlwt
from selenium import webdriver
from bs4 import BeautifulSoup
# V2.2 xls using the adding function
from xlrd import open_workbook
from xlutils.copy import copy

a = time.clock()

print("This procedure is to obtain the answers to the current purpose of Sy Online Examination.，Please contact us：SmLin97@outlook.com")
username=input("Please enter your username：")
password=input("Please enter your password：")

host="http://learn.shengyuan.com"

# browser window maximizing
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(host)
time.sleep(0.5)

user = browser.find_element_by_id("user")
user.send_keys(username)
psd = browser.find_element_by_id("pwd")
psd.send_keys(password)
code = browser.find_element_by_id("code")
code.send_keys("1")

commit =browser.find_elements_by_class_name("login_btn2")[0]
commit.click()
time.sleep(0.5)

if browser.current_url=='http://learn.shengyuan.com/OnLStuExmPt/learn/index.jsp':
    print("Login!")
else:
    print("Login false!")
    raise ZeroDivisionError("Please contact us：SmLin97@outlook.com")

# get the username
soup = BeautifulSoup(browser.page_source, 'html.parser')
username_ = soup.select('.top_info')[0]
pattern_username=re.compile(r'(?<=<p>)(.*?)(?=<a)')
username_name=re.findall(pattern_username,str(username_))[0]
print(username_name.strip()) # print out the welcome speech


browser.get(host+"/OnLStuExmPt/le/leac!findAllExam")
exams_page=browser.page_source
pattern=re.compile(r'onclick="check(.*?,.*?)"')
exam_num=re.findall(pattern,exams_page)[0].split(",")[0][1:]
time.sleep(0.5)

flag=False

for i in range(5):
    exam_url=host+"/OnLStuExmPt/le/leac!goExam?ecid="+exam_num
    browser.get(exam_url)
    time.sleep(2)
    exam_page=browser.page_source
    # get the current checkpoint, only once
    if flag==False:
        soup = BeautifulSoup(exam_page, 'html.parser')
        c_ = str(soup.select('.sjtitlebox')[0])
        print(c_[24:-6]) # print the checkpoint's level number
        flag=True

    browser.execute_script("window.scrollBy(0,5000)")
    time.sleep(2)

    # browser.clickAndHold()
    commit =browser.find_element_by_id("subBtn")
    commit.click()
    time.sleep(0.5)
    answser_page=browser.page_source

    with open("./pages/exam_page"+str(i)+".html","w",encoding="utf-8") as f:
        f.write(exam_page)
    with open("./pages/answer_page"+str(i)+".html","w",encoding="utf-8") as f:
        f.write(answser_page)
    print("Get the No."+str(i+1)+"time test answer successful!")

# logout
logout_url=host+"/OnLStuExmPt/rj/rjac!login_Out"
browser.get(logout_url)
time.sleep(0.5)
# exit the browser
browser.close()
browser.quit()


total_exam={} # the 10 list of question:[question,options]
z=0
for z in range(10):
    # test pages
    q_exam=[] # save the questions' page
    with open("./pages/exam_page"+str(z)+".html","r",encoding="utf-8") as f:
        exam_page=f.read()
    q_pattern=re.compile(r'(?<=</strong>)(.*?)(?=    <span)',re.S)
    q_exam=[x.replace("\n","").replace(" ","").strip() for x in re.findall(q_pattern,exam_page)]

    soup = BeautifulSoup(exam_page, 'html.parser')
    content_ = soup.select('.xtcontentclass')

    con=[] # to save the options
    i=0
    for i in range(30):
        A_pattern=re.compile(r'(?<=value="A"/>)(.*?)(?=</li>)',re.S)
        A_=re.findall(A_pattern,str(content_[i]))
        B_pattern=re.compile(r'(?<=value="B"/>)(.*?)(?=</li>)',re.S)
        B_=re.findall(B_pattern,str(content_[i]))
        C_pattern=re.compile(r'(?<=value="C"/>)(.*?)(?=</li>)',re.S)
        C_=re.findall(C_pattern,str(content_[i]))
        D_pattern=re.compile(r'(?<=value="D"/>)(.*?)(?=</li>)',re.S)
        D_=re.findall(D_pattern,str(content_[i]))
        con.append(A_+B_+C_+D_)


    exam_={} # {question: [questions, options]}
    i=0
    for i in range(30):
        exam_[q_exam[i]]=con[i]


    # answers' page
    q_=[] # save the questions
    a_=[] # save the answers
    with open("./pages/answer_page"+str(z)+".html","r",encoding="utf-8") as f:
        answer_page=f.read()
    a_pattern = '<label class="dx_button_xz">.+</label>'
    soup = BeautifulSoup(answer_page, 'html.parser')
    match_q = soup.select('.xttitleclass')
    match_a = re.findall(a_pattern,answer_page)

    for i in match_a:
        a_.append(i[28:-8])
    for i in match_q:
        ii=str(i).split()
        ii=''.join(ii)
        q_.append(ii.replace('<divclass="xttitleclass"><strong>题目：</strong>','').replace('<br/>',"").replace('</div>',"")[:-1])
    answ_={}
    for i in range(30):
        answ_[q_[i]]=a_[i]


    # print(exam_)
    # print(answ_)

    i=0
    try:
        for i in range(30):
            exam_[q_exam[i]].insert(0, answ_[q_exam[i]])
    except KeyError as e:
        continue
    # print(exam_) # question: [questions, options]
    total_exam.update(exam_)
    print("Writing No."+str(z+1)+" of the answer' page...")




# write to xls
file = xlwt.Workbook()
table = file.add_sheet('sy_list')
table.write(0,0,'index')
table.write(0,1,'answer')
table.write(0,2,'question')
table.write(0,3,'options')

i=1
for j in total_exam.items():
    table.write(i+1,0,i)
    table.write(i+1,2,j[0])
    table.write(i+1,1,j[1][0])
    table.write(i+1,3,"".join(list(j[1][1:])))
    i+=1
file.save('qa_('+c_[29:-6]+').xls')
print('qa_('+c_[29:-6]+').xls'+" written!")
print("Using the total time: "+str(round(time.clock()-a,2))+"seconds!")

