# -*- coding: utf-8 -*-
##############################
# 程序文件： DapLogger.py
# 功能：DapLogger类/输出日志
# 作者：林上满
# 创作时间：2019-08-21
##############################
import datetime, os, sys, time

def LoggerDebug(msg):
    __log("D", msg)

def LoggerInfo(msg):
    __log("I", msg)

def LoggerError(msg):
    __log("E", msg)

def __log(lever, msg):
    """
    输出日志
    """
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    s = "[%s][%s][%s]" % (time, lever, msg)
    today = now.strftime("%Y%m%d")
    # logFileName = "/home/Dap/exam/log/%s.log" % today
    logFileName = "D:\\CodeArea\\examsys\\log\\%s.log" % today
    try:
        __logFp = open(logFileName, "a")
        # __logFp.write("ABC")
        __logFp.write(s + "\n")
        __logFp.flush()
    except Exception as e:
        print("log Exception: ", e)


class DapLogger():
    """日志类"""
    def __init__(self):
        pass
    def debug(self, o, *args):
        self._log(LoggerDebug, o,_LOGPREFIX="  ", *args)
    def info(self, o, *args):
        self._log(LoggerInfo, o,_LOGPREFIX="  ", *args)
    def error(self, o, *args):
        self._log(LoggerError, o,_LOGPREFIX="  ", *args)
    def getNow(self):
        now = "%f" % time.time()
        now = now[5:10] + now[11:14]
        return now
    def _log(self, func, o, *args, **kwargs):
        """
        调用输出日志方法
        """
        entertime = self.getNow()
        prefix = kwargs.pop("_LOGPREFIX","")
        # o = "%s:%s%s" % (entertime, prefix, o)
        o = "<%s>:%s" % ("SysInfomation",o)
        # print(o)
        try:
            func(str(o))
        except Exception as e:
            print("func(str(o)) Exception: ", e)


if __name__ == '__main__':
    LoggerDebug("测试DapLogger")
