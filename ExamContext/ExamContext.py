# -*- coding: utf-8 -*-
##############################
# 程序文件： ExamContext.py
# 功能：问卷数据存放的模块
# 作者：林上满
# 创作时间：2019-08-21
##############################

def existVariable(varName):
    vars = globals()
    return varName in vars

def getNames():
    vars = globals()
    return vars

