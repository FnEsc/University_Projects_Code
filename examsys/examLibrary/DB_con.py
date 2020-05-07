import MySQLdb, sys
from examLibrary import examContext
from . import DapLoggerFunc


DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'examsys'
DB_CHARSET = 'utf8'


def examExit(errorCode, ErrorMsg):
    examContext.errorCode, examContext.errorMsg = errorCode, ErrorMsg
    return False if errorCode!="0000" else True


class DB_con(object):
    """docstring for DB_con"""

    def __init__(self):
        self.con = MySQLdb.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            charset=DB_CHARSET
        )
        self.cursor = self.con.cursor()

    def __del__(self):
        self.cursor.close()
        self.con.close()

    def DB_Userinfo_Select(self, username, password):
        """Just only to verify username & password"""
        sql = 'SELECT uid,username,nickname,ismaster FROM userinfo WHERE username="%s" AND password="%s"' % (username, password)
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            DapLoggerFunc.examError(str(e))
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            # print("SysInfomation: DB_Userinfo_Select-> Verify Succeed! uid=%s,username=%s,nickname=%s,ismaster=%s" % rs[0])
            DapLoggerFunc.examInfo("SysInfomation: DB_Userinfo_Select-> Verify Succeed! uid=%s,username=%s,nickname=%s,ismaster=%s" % rs[0])
            (examContext.uid, examContext.username, examContext.nickname, examContext.ismaster) = rs[0]
            errorCode,errorMsg = "0000","SysInfomation: DB_Userinfo_Select-> Verify Succeed! uid=%s,username=%s,nickname=%s,ismaster=%s" % rs[0]
            return examExit(errorCode,errorMsg)

        else:
            # print("SysInfomation: DB_Userinfo_Select-> Verify Failed! username=%s,password=%s" % (username, password))
            DapLoggerFunc.examInfo("SysInfomation: DB_Userinfo_Select-> Verify Failed! username=%s,password=%s" % (username, password))
            errorCode,errorMsg = "0005","SysInfomation: DB_Userinfo_Select-> Verify Failed! username=%s,password=%s" % (username, password)
            return examExit(errorCode,errorMsg)

    def DB_Userinfo_Insert(self, username, password, nickname, ismaster):
        """Just only to add one user"""
        sql = 'INSERT INTO userinfo(username,password,nickname,ismaster) VALUES ("%s","%s","%s","%s")' % (
        username, password, nickname, ismaster)
        try:
            sql_select = 'SELECT uid FROM userinfo WHERE username="%s"' % username
            self.cursor.execute(sql_select)
            rs = self.cursor.fetchall()
            if (rs):
                # print("SysInfomation: DB_Userinfo_Insert-> Insert Failed! username=%s is exist!" % username)
                DapLoggerFunc.examDebug("SysInfomation: DB_Userinfo_Insert-> Insert Failed! username=%s is exist!" % username)
                errorCode, errorMsg = "0003","SysInfomation: DB_Userinfo_Insert-> Insert Failed! username=%s is exist!" % username
                return examExit(errorCode, errorMsg)
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                # print("SysInfomation: DB_Userinfo_Insert-> Add User Succeed! username=%s,password=%s,nickname=%s,ismaster=%s" % (username, password, nickname, ismaster))
                ErrorMsg = "SysInfomation: DB_Userinfo_Insert-> Add User Succeed! username=%s,password=%s,nickname=%s,ismaster=%s" % (
                    username, password, nickname, ismaster)
                DapLoggerFunc.examInfo(ErrorMsg)
                return examExit("0000", ErrorMsg)
        except Exception as e:
            # print(e)
            self.con.rollback()
            # print("SysInfomation: DB_Userinfo_Insert-> Add User Failed!", e)
            DapLoggerFunc.examError("SysInfomation: DB_Userinfo_Insert-> Add User Failed!" + str(e))
            errorCode = "0004"
            errorMsg = "SysInfomation: DB_Userinfo_Insert-> Add User Failed!" + str(e)
            return examExit(errorCode, errorMsg)

    def DB_Userinfo_Password_Update(self, username, newpassword):
        """Just only to repassword"""
        sql = 'UPDATE userinfo SET password="%s" WHERE username="%s"' % (newpassword, username)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            print(self.cursor.rowcount)
            if (self.cursor.rowcount):
                # print("SysInfomation: DB_Userinfo_Password_Update-> Repassword Succeed! username=%s,password=%s" % (username, password))
                errorMsg = "SysInfomation: DB_Userinfo_Password_Update-> Repassword Succeed! username=%s,password=%s" % (username, newpassword)
                DapLoggerFunc.examInfo(errorMsg)
                return examExit("0000",errorMsg)
            elif self.cursor.rowcount==0:
                errorMsg = "SysInfomation: DB_Userinfo_Password_Update-> Repassword Succeed! But has no change! username=%s,password=%s" % (username, newpassword)
                DapLoggerFunc.examInfo(errorMsg)
                return examExit("0000", errorMsg)
        except Exception as e:
            # print(e)
            self.con.rollback()
            # print("SysInfomation: DB_Userinfo_Password_Update-> Repassword Failed!", e)
            errorMsg = "SysInfomation: DB_Userinfo_Password_Update-> Repassword Failed!" + str(e)
            DapLoggerFunc(errorMsg)
            return examExit("0006",errorMsg)

    def DB_Userinfo_Nickname_Update(self, username, newnickname):
        """Just only to renickname"""
        sql = 'UPDATE userinfo SET nickname="%s" WHERE username="%s"' % (newnickname, username)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                # print("SysInfomation: DB_Userinfo_Nickname_Update-> Renickname Succeed! username=%s,nickname=%s" % (username, newnickname))
                errorMsg = "SysInfomation: DB_Userinfo_Nickname_Update-> Renickname Succeed! username=%s,nickname=%s" % (username, newnickname)
                DapLoggerFunc.examInfo(errorMsg)
                return examExit("0000",errorMsg)
        except Exception as e:
            # print(e)
            self.con.rollback()
            # print("SysInfomation: DB_Userinfo_Nickname_Update-> Renickname Failed!", e)
            errorMsg = "SysInfomation: DB_Userinfo_Nickname_Update-> Renickname Failed!" + str(e)
            DapLoggerFunc.examError(errorMsg)
            return examExit("0008",errorMsg)

    def DB_Userrely_Getslave_Select(self, masteruid):
        '''get the slave userinfo'''
        sql = 'SELECT slaveuid,userinfo.username,userinfo.nickname FROM userrely,userinfo WHERE masteruid="%s" AND userinfo.uid=userrely.slaveuid' % masteruid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print("SysInfomation: DB_Userrely_Getslave_Select-> masteruid=%s slaveuid=%s username=%s nickname=%s" % (
                            (masteruid,) + row))
        else:
            print("SysInfomation: DB_Userrely_Getslave_Select-> The masteruid has no userrely!")

    def DB_Userrely_Addslave_Insert(self, masteruid, slaveuid):
        sql = 'INSERT INTO userrely(masteruid,slaveuid) VALUES ("%s","%s")' % (masteruid, slaveuid)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Userrely_Addslave_Insert-> Add uerrely Succeed! masteruid=%s,slaveuid=%s" % (
                masteruid, slaveuid))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Userrely_Addslave_Insert-> Add User Failed!", e)

    def DB_Userrely_Delslave_Delete(self, masteruid, slaveuid):
        sql = 'DELETE FROM userrely WHERE masteruid=%s AND slaveuid=%s' % (masteruid, slaveuid)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Userrely_Delslave_Delete-> Del uerrely Succeed! masteruid=%s,slaveuid=%s" % (
                masteruid, slaveuid))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Userrely_Delslave_Delete-> Del User Failed!", e)

    def DB_Groupinfo_Getgroupinfo_Select(self, masteruid):
        '''get the groupinfo of masteruid'''
        sql = 'SELECT gid,gtitle,gdescribe FROM groupinfo WHERE gowneruid=%s' % masteruid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print("SysInfomation: DB_Groupinfo_Getgroupinfo_Select-> masteruid=%s guid=%s gtitle=%s gdescribe=%s" % (
                            (masteruid,) + row))
        else:
            print("SysInfomation: DB_Groupinfo_Getgroupinfo_Select-> The masteruid has no group!")

    def DB_Groupinfo_Addgroup_Insert(self,gowneruid, gtitle, gdescribe):
        sql = 'INSERT INTO groupinfo(gowneruid,gtitle,gdescribe) VALUES ("%s","%s","%s")' % (gowneruid, gtitle, gdescribe)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print(
                    "SysInfomation: DB_Groupinfo_Addgroup_Insert-> Add group Succeed! gowneruid=%s gtitle=%s gdescribe=%s" % (
                        gowneruid, gtitle, gdescribe))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Groupinfo_Addgroup_Insert-> Add group Failed!", e)

    def DB_Groupinfo_Delete(self, gid):
        sql = 'DELETE FROM groupinfo WHERE gid=%s' % gid
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Groupinfo_Delete-> Del group Succeed! gid=%s" % gid)
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Groupinfo_Delete-> Del group Failed!", e)

    def DB_Groupinfo_Update(self, gid, newgtitle, newgdescribe):
        sql = 'UPDATE groupinfo SET gtitle="%s", gdescribe="%s" WHERE gid="%s"' % (newgtitle, newgdescribe, gid)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print(
                    "SysInfomation: DB_Groupinfo_Update-> Regroupinfo Succeed! gid=%s newgtitle=%s newgdescribe=%s" % (
                    gid, newgtitle, newgdescribe))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Groupinfo_Update-> Regroupinfo Failed!", e)

    def DB_Gusers_Getgusers_Select(self, gid='0', gowneruid='0'):
        if gid != 0:
            sql = 'SELECT gowneruid,guseruid FROM gusers WHERE gid=%s' % gid
            try:
                self.cursor.execute(sql)
                self.con.commit()
            except Exception as e:
                # print(e)
                self.con.rollback()
            rs = self.cursor.fetchall()
            if (rs):
                for row in rs:
                    print("SysInfomation: DB_Gusers_Getgusers_Select-> gid=%s gowneruid=%s guseruid=%s" % ((gid,) + row))
            else:
                print("SysInfomation: DB_Gusers_Getgusers_Select-> The gid has no gusers!")
        else:
            sql = 'SELECT gowneruid,gid,guseruid FROM gusers WHERE gowneruid=%s' % gowneruid
            try:
                self.cursor.execute(sql)
                self.con.commit()
            except Exception as e:
                # print(e)
                self.con.rollback()
            rs = self.cursor.fetchall()
            if (rs):
                for row in rs:
                    print("SysInfomation: DB_Gusers_Getgusers_Select-> gowneruid=%s guid=%s guseruid=%s" % (row))
            else:
                print("SysInfomation: DB_Gusers_Getgusers_Select-> The gowneruid has no gusers!")

    def DB_Gusers_Insert(self,gowneruid, guseruid):
        sql = 'INSERT INTO gusers(gowneruid, guseruid) VALUES ("%s","%s")' % (gowneruid, guseruid)
        try:
            sql_select = 'SELECT COUNT(1) FROM gusers WHERE gowneruid="%s" and guseruid="%s" ' % (gowneruid, guseruid)
            self.cursor.execute(sql_select)
            rs = self.cursor.fetchall()
            if (rs[0][0]) >= 1:
                print("SysInfomation: DB_Gusers_Insert-> The recovery has exist!")
                return
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print(
                    "SysInfomation: DB_Gusers_Insert-> Add gusers Succeed! gowneruid=%s guseruid=%s" % (
                        gowneruid, guseruid))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Gusers_Insert-> Add group Failed!", e)

    def DB_Gusers_Guseruid_Delete(self, gowneruid, guseruid):
        sql = 'DELETE FROM gusers WHERE gowneruid="%s" and guseruid="%s" ' % (gowneruid, guseruid)
        try:
            sql_select = 'SELECT COUNT(1) FROM gusers WHERE gowneruid="%s" and guseruid="%s" ' % (gowneruid, guseruid)
            self.cursor.execute(sql_select)
            rs = self.cursor.fetchall()
            if (rs[0][0])!=1:
                print("SysInfomation: DB_Gusers_Guseruid_Delete-> The recovery has some errors!")
                raise Exception("DB_Gusers_Guseruid_Delete", "The recovery has some errors!")
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Groupinfo_Delete-> Del group Succeed! gowneruid=%s guseruid=%s" % (gowneruid, guseruid))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Groupinfo_Delete-> Del group Failed!", e)

    def DB_Questions_Getquestion_Select(self, qid):
        sql = 'SELECT qid, qtype, q, a, op1, op2, op3, op4 FROM questions WHERE qid=%s' % qid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            print("SysInfomation: DB_Questions_Getquestion_Select-> qid=%s qtype=%s q=%s a=%s op1=%s op2=%s op3=%s op4=%s" % (
            rs[0]))
        else:
            print("SysInfomation: DB_Questions_Getquestion_Select-> The qid Error!")

    def DB_Questions_Getallquestions_Select(self, qowneruid, qtype=0):
        if qtype == 0:
            sql = 'SELECT qid, qtype, q, a, op1, op2, op3, op4 FROM questions WHERE qowneruid=%s' % qowneruid
            try:
                self.cursor.execute(sql)
                self.con.commit()
                rs = self.cursor.fetchall()
                if (rs):
                    for row in rs:
                        print("SysInfomation: DB_Questions_Getallquestions_Select-> qowneruid=%s qid=%s qtype=%s q=%s a=%s op1=%s op2=%s op3=%s op4=%s" % ((qowneruid,)+row))
                else:
                    print("SysInfomation: DB_Questions_Getallquestions_Select-> The qowneruid has no questions!")
            except Exception as e:
                # print(e)
                self.con.rollback()
        else:
            sql = 'SELECT qid, qtype, q, a, op1, op2, op3, op4 FROM questions WHERE qowneruid=%s AND qtype=%s' % (
            qowneruid, qtype)
            try:
                self.cursor.execute(sql)
                self.con.commit()
                rs = self.cursor.fetchall()
                if (rs):
                    for row in rs:
                        print(
                            "SysInfomation: DB_Questions_Getallquestions_Select-> qowneruid=%s qid=%s qtype=%s q=%s a=%s op1=%s op2=%s op3=%s op4=%s" % (
                                row))
                else:
                    print("SysInfomation: DB_Questions_Getallquestions_Select-> The qowneruid has no questions of qtype!")
            except Exception as e:
                # print(e)
                self.con.rollback()

    def DB_Questions_Addquestion_Insert(self, qtype, q, a, op1, op2, op3, op4, qowneruid, mid=0):
        if mid == 0:
            sql = 'INSERT INTO questions(qtype, q, a, op1, op2, op3, op4, qowneruid) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")' % (
            qtype, q, a, op1, op2, op3, op4, qowneruid)
            try:
                self.cursor.execute(sql)
                self.con.commit()
                if (self.cursor.rowcount):
                    print(
                        "SysInfomation: DB_Questions_Addquestion_Insert-> Add question Succeed! qowneruid=%s qtype=%s q=%s a=%s op1=%s op2=%s op3=%s op4=%s" % (
                        qowneruid, qtype, q, a, op1, op2, op3, op4))
            except Exception as e:
                # print(e)
                self.con.rollback()
                print("SysInfomation: DB_Questions_Addquestion_Insert-> Add question Failed!", e)
        else:
            sql = 'INSERT INTO questions(qtype, q, a, op1, op2, op3, op4, qowneruid) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s");SELECT LAST_INSERT_ID();' % (
            qtype, q, a, op1, op2, op3, op4, qowneruid)
            try:
                self.cursor.execute(sql)
                self.con.commit()
                rs = self.cursor.fetchall()
                if (rs[0] != 0):
                    self.DB_Qtom_Addqtom_Insert(mid, rs[0])
                    print(
                        "SysInfomation: DB_Questions_Addquestion_Insert-> Add question Succeed!Also to mid=%s! qowneruid=%s qid=%s qtype=%s q=%s a=%s op1=%s op2=%s op3=%s op4=%s" % (
                        mid, qowneruid, rs[0], qtype, q, a, op1, op2, op3, op4))
            except Exception as e:
                # print(e)
                self.con.rollback()
                print("SysInfomation: DB_Questions_Addquestion_Insert-> Add question Failed!", e)

    def DB_Questions_Delquestion_Delete(self, qid):
        sql = 'DELETE FROM questions WHERE qid=%s' % qid
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Questions_Delquestion_Delete-> Del question Succeed! qid=%s" % qid)
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Questions_Delquestion_Delete-> Del question Failed!", e)

    def DB_Questions_Requestion_Update(self, qid, qtype, q, a, op1, op2, op3, op4, qowneruid):
        sql = 'UPDATE questions SET qtype="%s",q="%s",a="%s",op1="%s",op2="%s",op3="%s",op4="%s" WHERE qid="%s" and qowneruid="%s" ' % (
        qtype, q, a, op1, op2, op3, op4, qid, qowneruid)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print(
                    "SysInfomation: DB_Questions_Requestion_Update-> Requestion Succeed! qid=%s qtype=%s,q=%s,a=%s,op1=%s,op2=%s,op3=%s,op4=%s" % (
                    qid, qtype, q, a, op1, op2, op3, op4))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Questions_Requestion_Update-> Requestion Failed!", e)

    def DB_Adqm_Getadqms_Select(self, qmowneruid):
        sql = 'SELECT qmowneruid,mid,qmtitle,qmdescribe FROM adqm WHERE qmowneruid=%s' % qmowneruid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print("SysInfomation: DB_Adqm_Getadqms_Select-> qmowneruid=%s mid=%s qmtitle=%s qmdescribe=%s" % row)
        else:
            print("SysInfomation: DB_Adqm_Getadqms_Select-> The qmowneruid has no adqms!")

    def DB_Adqm_Addadqm_Insert(self, qmowneruid, qmtitle, qmdescribe):
        sql = 'INSERT INTO adqm(qmowneruid,qmtitle,qmdescribe) VALUES ("%s","%s","%s")' % (qmowneruid, qmtitle, qmdescribe)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Adqm_Addadqm_Insert-> Add adqm Succeed! qmowneruid=%s mtitle=%s qmdescribe=%s" % (
                    qmowneruid, qmtitle, qmdescribe))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Adqm_Addadqm_Insert-> Add adqm Failed!", e)

    def DB_Adqm_Deladqm_Delete(self, mid):
        sql = 'DELETE FROM adqm WHERE mid=%s' % mid
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Adqm_Deladqm_Delete-> Del adqm Succeed! mid=%s" % mid)
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Adqm_Deladqm_Delete-> Del adqm Failed!", e)

    def DB_Adqm_Readqm_Update(self, mid, newqmtitle, newqmdescribe):
        sql = 'UPDATE adqm SET qmtitle="%s", qmdescribe="%s" WHERE mid="%s"' % (newqmtitle, newqmdescribe, mid)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Adqm_Readqm_Update-> Readqm Succeed! mid=%s newqmtitle=%s newqmdescribe=%s" % (
                mid, newqmtitle, newqmdescribe))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Adqm_Readqm_Update-> Readqm Failed!", e)

    def DB_Qtom_Getqtomqids_Select(self, mid):
        sql = 'SELECT mid,qid FROM qtom WHERE mid="%s"' % mid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print("SysInfomation: DB_Qtom_Getqtomqids_Select-> mid=%s qid=%s" % row)
        else:
            print("SysInfomation: DB_Qtom_Getqtomqids_Select-> The mid has no userrely!")

    def DB_Qtom_Addqtom_Insert(self, mid, qid):
        sql = 'INSERT INTO qtom(mid,qid) VALUES ("%s","%s")' % (mid, qid)
        try:
            sql_select = 'SELECT COUNT(1) FROM qtom WHERE mid="%s" and qid="%s" ' % (mid, qid)
            self.cursor.execute(sql_select)
            rs = self.cursor.fetchall()
            if (rs[0][0]) >= 1:
                print("SysInfomation: DB_Qtom_Addqtom_Insert-> The recovery has exist!")
                raise Exception("DB_Qtom_Addqtom_Insert", "The recovery has exist!")
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Qtom_Addqtom_Insert-> Add qtom Succeed! mid=%s,qid=%s" % (mid, qid))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Qtom_Addqtom_Insert-> Add qtom Failed!", e)

    def DB_Qtom_Delqtom_Delete(self, mid, qid):
        sql = 'DELETE FROM qtom WHERE mid=%s AND qid=%s' % (mid, qid)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Qtom_Delqtom_Delete-> Del qtom Succeed! mid=%s,qid=%s" % (mid, qid))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Qtom_Delqtom_Delete-> Del qtom Failed!", e)

    def DB_Examinfo_Select(self, creater='0', exid='0'):
        sql = 'SELECT exid,creater,createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7 FROM examinfo '
        if creater!='0':
            sql += 'WHERE creater = "%s"' % creater
        else:
            sql += 'WHERE exid = "%s"' % exid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print("SysInfomation: DB_Examinfo_Select-> exid=%s,creater=%s,createtime=%s,mid=%s,extitle=%s,exdescribe=%s,op1=%s,op2=%s,op3=%s,op4=%s,op5=%s,op6=%s,op7=%s" % row)
        else:
            print("SysInfomation: DB_Examinfo_Select-> Examinfo Select Failed")

    def DB_Examinfo_Insert(self, creater,createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7):
        sql = 'INSERT INTO examinfo(creater,createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (creater,createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Examinfo_Insert-> Add examinfo Succeed! creater=%s,createtime=%s,mid=%s,extitle=%s,exdescribe=%s,op1=%s,op2=%s,op3=%s,op4=%s,op5=%s,op6=%s,op7=%s" % (creater,createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Examinfo_Insert-> Add examinfo Failed!", e)

    def DB_Examinfo_Update(self, exid,createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7):
        sql = 'UPDATE examinfo SET createtime="%s",mid="%s",extitle="%s",exdescribe="%s",op1="%s",op2="%s",op3="%s",op4="%s",op5="%s",op6="%s",op7="%s" WHERE exid="%s"' % (createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7,exid)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Examinfo_Update-> Update examinfo Succeed! exid=%s,createtime=%s,mid=%s,extitle=%s,exdescribe=%s,op1=%s,op2=%s,op3=%s,op4=%s,op5=%s,op6=%s,op7=%s" % (exid,createtime,mid,extitle,exdescribe,op1,op2,op3,op4,op5,op6,op7))
            else:
                print("SysInfomation: DB_Examinfo_Update-> Update examinfo Succeed but has no change!")
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Examinfo_Update-> Update examinfo Failed!", e)

    def DB_Examinfo_Delete(self, exid):
        sql = 'DELETE FROM examinfo WHERE exid="%s" ' % exid
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print("SysInfomation: DB_Examinfo_Delete-> Del examinfo Succeed! exid=%s" % exid)
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Examinfo_Delete-> Del examinfo Failed!", e)

    def DB_Examrecord_Select(self,erid='0',creater='0',exid='0'):
        sql = 'SELECT erid,creater,exid,auid,answertime FROM examrecord '
        if erid != '0':
            sql += 'WHERE erid = "%s"' % erid
        elif creater !='0':
            if exid !='0':
                sql += 'WHERE creater = "%s" AND exid="%s" ' % (creater,exid)
        else:
            sql += 'WHERE exid="%s"' % exid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print(
                    "SysInfomation: DB_Examrecord_Select-> erid=%s,creater=%s,exid=%s,auid=%s,answertime=%s" % row)
        else:
            print("SysInfomation: DB_Examrecord_Select-> Examrecord Select Failed")

    def DB_Examrecord_Insert(self,creater,exid,auid,answertime):
        sql = 'INSERT INTO examrecord(creater,exid,auid,answertime) VALUES ("%s","%s","%s","%s")' % (creater, exid, auid, answertime)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print(
                    "SysInfomation: DB_Examrecord_Insert-> Add Examinfo Succeed! creater=%s,exid=%s,auid=%s,answertime=%s" % (
                        creater, exid, auid, answertime))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Examrecord_Insert-> Add Examrecord Failed!", e)

    def DB_History_Select(self,hid='0', erid='0'):
        sql = 'SELECT hid,erid,qid,a,selected,answerbool FROM history '
        if hid != '0':
            sql += 'WHERE hid = "%s"' % hid
        else:
            sql += 'WHERE erid="%s"' % erid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print(
                    "SysInfomation: DB_History_Select-> hid=%s,erid=%s,qid=%s,a=%s,selected=%s,answerbool=%s" % row)
        else:
            print("SysInfomation: DB_History_Select-> History Select Failed")

    def DB_History_Insert(self,erid,qid,a,selected):
        sql = 'INSERT INTO history(erid,qid,a,selected) VALUES ("%s","%s","%s","%s")' % (erid, qid, a, selected)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print(
                    "SysInfomation: DB_History_Insert-> Add History Succeed! erid=%s,qid=%s,a=%s,selected=%s" % (
                        erid, qid, a, selected))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_History_Insert-> Add History Failed!", e)

    def DB_Suggestions_Select(self,sugid='0', exid='0'):
        sql = 'SELECT sugid,suguid,exid,sugdescribe FROM suggestions '
        if sugid != '0':
            sql += 'WHERE sugid = "%s"' % sugid
        else:
            sql += 'WHERE exid="%s"' % exid
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            # print(e)
            self.con.rollback()
        rs = self.cursor.fetchall()
        if (rs):
            for row in rs:
                print(
                    "SysInfomation: DB_Suggestions_Select-> Sugguestions Select Succeed! sugid=%s,suguid=%s,exid=%s,sugdescribe=%s" % row)
        else:
            print("SysInfomation: DB_Suggestions_Select-> Sugguestions Select Failed")

    def DB_Suggestions_Insert(self,suguid,exid,sugdescribe):
        sql = 'INSERT INTO suggestions(suguid,exid,sugdescribe) VALUES ("%s","%s","%s")' % (suguid,exid,sugdescribe)
        try:
            self.cursor.execute(sql)
            self.con.commit()
            if (self.cursor.rowcount):
                print(
                    "SysInfomation: DB_Suggestions_Insert-> Add Suggestion Succeed! suguid=%s,exid=%s,sugdescribe=%s" % (
                        suguid, exid, sugdescribe))
        except Exception as e:
            # print(e)
            self.con.rollback()
            print("SysInfomation: DB_Suggestions_Insert-> Add Suggestion Failed!", e)


def main():
    dev_Test_DB_Con = DB_con()

    # For Table "userinfo" --ok
    print("For Table \"userinfo\"")
    dev_Test_DB_Con.DB_Userinfo_Select("99@qq.com", "1")
    dev_Test_DB_Con.DB_Userinfo_Select("99@qq.com", "2")
    dev_Test_DB_Con.DB_Userinfo_Insert("99@qq.com","99","99",1)
    dev_Test_DB_Con.DB_Userinfo_Password_Update("99@qq.com","1","2")
    dev_Test_DB_Con.DB_Userinfo_Nickname_Update("99@qq.com","testnickname")
    print("For Table \"userinfo\" --ok")
    print("\n")

    # For Table "userrely" --ok
    print("For Table \"userrely\"")
    dev_Test_DB_Con.DB_Userrely_Getslave_Select("1")
    dev_Test_DB_Con.DB_Userrely_Addslave_Insert(1,8)
    dev_Test_DB_Con.DB_Userrely_Delslave_Delete(1,8)
    print("For Table \"userrely\" --ok")
    print("\n")

    # For Table "groupinfo"
    print("For Table \"groupinfo\"")
    dev_Test_DB_Con.DB_Groupinfo_Getgroupinfo_Select("1")
    dev_Test_DB_Con.DB_Groupinfo_Addgroup_Insert("1","test_","test_")
    dev_Test_DB_Con.DB_Groupinfo_Update("4","test_g","test_d")
    dev_Test_DB_Con.DB_Groupinfo_Delete("15")
    print("For Table \"groupinfo\" --ok")
    print("\n")

    # For Table "gusers"
    print("For Table \"gusers\"")
    dev_Test_DB_Con.DB_Gusers_Getgusers_Select("1","1")
    dev_Test_DB_Con.DB_Gusers_Guseruid_Delete("1", "45")
    dev_Test_DB_Con.DB_Gusers_Insert("1","45")
    print("For Table \"gusers\" --ok")
    print("\n")

    # For Table "questions"
    print("For Table \"questions\"")
    dev_Test_DB_Con.DB_Questions_Getallquestions_Select("1")
    dev_Test_DB_Con.DB_Questions_Getallquestions_Select("1","2")
    dev_Test_DB_Con.DB_Questions_Addquestion_Insert("1","test_q","1","A","B","C","D","1")
    dev_Test_DB_Con.DB_Questions_Getquestion_Select("13")
    dev_Test_DB_Con.DB_Questions_Delquestion_Delete("13")
    dev_Test_DB_Con.DB_Questions_Requestion_Update("14","2","test_q","1234","a","b","c","d","1")
    print("For Table \"questions\" --ok")
    print("\n")

    # For Table "table"
    print("For Table \"adqm\"")
    dev_Test_DB_Con.DB_Adqm_Getadqms_Select("1")
    dev_Test_DB_Con.DB_Adqm_Addadqm_Insert("1","test_qmtitle","test_qmdescribe")
    dev_Test_DB_Con.DB_Adqm_Readqm_Update("4","test_newqmt","test_newqmd")
    dev_Test_DB_Con.DB_Adqm_Deladqm_Delete("4")
    print("For Table \"adqm\" --ok")
    print("\n")

    # For Table "qtom"
    print("For Table \"qtom\"")
    dev_Test_DB_Con.DB_Qtom_Getqtomqids_Select("1")
    dev_Test_DB_Con.DB_Qtom_Addqtom_Insert("1","5")
    dev_Test_DB_Con.DB_Qtom_Delqtom_Delete("1","5")
    print("For Table \"qtom\" --ok")
    print("\n")

    # For Table "examinfo"
    print("For Table \"examinfo\"")
    dev_Test_DB_Con.DB_Examinfo_Select(exid="3")
    dev_Test_DB_Con.DB_Examinfo_Select(creater="1")
    dev_Test_DB_Con.DB_Examinfo_Insert("1","2019-09-02 19:57:31","1","test_Insert","test_d","0","0","0","0","0","2019-09-03 19:57:31","2019-12-30 19:57:31")
    dev_Test_DB_Con.DB_Examinfo_Update("5","2019-09-02 19:57:31","1","test_update","test_d","0","0","0","0","0","2019-09-03 19:57:31","2019-12-30 19:57:31")
    dev_Test_DB_Con.DB_Examinfo_Delete("6")
    print("For Table \"examinfo\" --ok")
    print("\n")


    # For Table "examrecord"
    print("For Table \"examrecord\"")
    dev_Test_DB_Con.DB_Examrecord_Select(exid="1")
    dev_Test_DB_Con.DB_Examrecord_Select(creater="1")
    dev_Test_DB_Con.DB_Examrecord_Select(creater="1",exid="2")
    dev_Test_DB_Con.DB_Examrecord_Insert("1","1","3","2019-09-02 20:45:03")
    print("For Table \"examrecord\" --ok")
    print("\n")

    # For Table "history"
    print("For Table \"history\"")
    dev_Test_DB_Con.DB_History_Select(hid="1")
    dev_Test_DB_Con.DB_History_Select(erid="1")
    dev_Test_DB_Con.DB_History_Insert("1","1","2","1")
    print("For Table \"history\" --ok")
    print("\n")

    # For Table "Suggestions"
    print("For Table \"Suggestions\"")
    dev_Test_DB_Con.DB_Suggestions_Select(sugid="1")
    dev_Test_DB_Con.DB_Suggestions_Select(exid="1")
    dev_Test_DB_Con.DB_Suggestions_Insert("1","1","test_sug_ins")
    print("For Table \"Suggestions\" --ok")
    print("\n")

if __name__ == '__main__':
    main()


