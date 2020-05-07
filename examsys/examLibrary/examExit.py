from . import examContext

def examExit(errorCode, ErrorMsg):
    examContext.errorCode, examContext.ErrorMsg = errorCode, ErrorMsg
    return False if errorCode!="0000" else True

