import MySQLdb


class Con(object):
    def __init__(self):
        try:
            self.con = MySQLdb.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='',
                db='baitan_python',
                charset='utf8'
            )
            self.cursor = self.con.cursor()
        except Exception as e:
            print("出错：", str(e))

