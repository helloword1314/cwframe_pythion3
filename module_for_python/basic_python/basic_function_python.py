# -*- coding: utf-8 -*-
import os
import sys

def Unicode_2_Str(str_input):
    '''返回上一级目录
    Args:
        给我当前目录
    '''
    return str_input.encode('gbk')

def Check_Chinese_In_String(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def Show_Python_EXE_Path():
    '''当前工作目录绝对路径
    Args:
        whatdoyouwannasay
    '''
    return sys.executable

def Show_Current_Working_Path():
    '''当前工作目录绝对路径
    Args:
        whatdoyouwannasay
    '''
    return os.getcwd()

def Change_Dir__Path(path_input):
    '''修改当前工作目录绝对路径
    Args:
        whatdoyouwannasay
    '''
    return os.chdir(path_input)

def Show_Current_File_Path():
    '''当前文本的绝对路径
    Args:
        whatdoyouwannasay
    '''
    return os.path.realpath(__file__)

def Back_Upper_Path(strPath):
    '''返回上一级目录
    Args:
        strPath：我当前目录
    '''
    return '\\'.join(strPath.split('\\')[:-1])

def Show_All_Builtins_Funcitons_In_Python():
    '''返回python模块的内置函数
    Args:
    '''
    return dir("__builtins__")

def Show_All_Builtins_Funcitons_In_Sys():
    '''返回Sys模块的内置函数
    Args:
       
    '''
    return dir(sys.modules['__builtin__'])  

def Show_Properties_Of_Object(obj):
    '''返回对象的所有属性方法
    Args: 
    '''
    return dir(obj)

def Check_Object_Belongs_Class(obj_input,class_input):
    '''对象是否是这个类的实例
    Args:
       
    '''
    return isinstance(obj_input,class_input)

def Say_Something():
    print("曹维，人生真是无聊啊！")
	
	
if __name__=="__main__":
    Say_Something()
