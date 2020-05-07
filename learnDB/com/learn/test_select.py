import MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    db='test_python',
    charset='utf8'
)

cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)
rs=cursor.fetchall()
for row in rs:
    print("userid=%s,username=%s" % row)


cursor.close()
conn.close()