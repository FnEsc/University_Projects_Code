#-*-coding:utf-8-*-
import requests
import re
from bs4 import BeautifulSoup

url = 'http://selukwe.cn/da/?p='
total = 0

for index in range(1, 1301):
	r = requests.get(url+str(index))
	if (r.status_code != 200) :
		print (str(index)+'->'+'失败')
	else :
		print (index)
		total += 1
print (total)