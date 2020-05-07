# -*- coding: utf-8 -*-
##############################
# 程序文件： Main.py
# 功能：主函数测试
# 作者：林上满
# 创作时间：2019-08-21
##############################
import ExamContext
import Test
import DapLoggerFunc

if __name__ == '__main__':
    DapLoggerFunc.examInfo(">>>>>>开始Main<<<<<<")
    ExamContext.errorCode, ExamContext.errorMsg = "0000", "答题完成"
    print(ExamContext.errorCode)
    if not ExamContext.existVariable("errorMsg"):
        print("not exist errorMsg")
    else:
        print("exist errorMsg")
    print("Finish!")
    Test.SubModuleDoFst()
    print("Go!")
    DapLoggerFunc.examError(">>>>>>结束Main<<<<<<")




