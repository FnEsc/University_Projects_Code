# -*- coding: utf-8 -*-
##############################
# 程序文件： Test.py
# 功能：测试模块
# 作者：林上满
# 创作时间：2019-08-21
##############################
import ExamContext
import DapLoggerFunc

def SubModuleDoFst():
    DapLoggerFunc.examInfo(">>>>>>进入Test.py<<<<<<")
    if not ExamContext.existVariable("errorMsg"):
        print("not exist errorMsg")
    else:
        print("exist errorMsg")
    if not ExamContext.existVariable("Novar"):
        print("not exist Novar")
        DapLoggerFunc.examDebug("examDebug不存在Novar变量")
    else:
        print("exist Novar")
    DapLoggerFunc.examInfo(">>>>>>退出Test.py<<<<<<")