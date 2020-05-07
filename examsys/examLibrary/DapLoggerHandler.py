# -*- coding: utf-8 -*-
##############################
# 程序文件： DapLoggerHandler.py
# 功能：Django平台日志控件
# 作者：林上满
# 创作时间：2019-08-21
##############################

from . import DapLogger

_DapLOGGER_ = None

def getLogger():
    global _DapLOGGER_
    if _DapLOGGER_ ==None:
        _DapLOGGER_ = DapLogger.DapLogger()
        return _DapLOGGER_
    else:
        return _DapLOGGER_
