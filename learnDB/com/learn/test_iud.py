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

sql_insert = "insert into user(userid,username) values (10,'name10')"
sql_update = "update user set username='name91' where userid=9"
sql_delete = "delete from user where userd<3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)  # 返回执行数据库影响了多少行
    cursor.execute(sql_update)
    print(cursor.rowcount)  # 返回执行数据库影响了多少行
    cursor.execute(sql_delete)
    print(cursor.rowcount)  # 返回执行数据库影响了多少行

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()  # 错误回滚


cursor.close()
conn.close()