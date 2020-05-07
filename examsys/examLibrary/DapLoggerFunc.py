# -*- coding: utf-8 -*-
##############################
# 程序文件： DapLoggerFunc.py
# 功能：日志维护方法
# 作者：林上满
# 创作时间：2019-08-21
##############################

import time, os, sys
from . import DapLoggerHandler

ExamLogger = DapLoggerHandler.getLogger()

def examDebug(msg, *args):
    '''
    打印调试级问卷日志
    '''
    ExamLogger.debug(msg, *args)

def examInfo(msg, *args):
    '''
    打印信息级问卷日志
    '''
    ExamLogger.info(msg, *args)

def examError(msg, *args):
    '''
    打印错误级问卷日志
    '''
    ExamLogger.error(msg, *args)