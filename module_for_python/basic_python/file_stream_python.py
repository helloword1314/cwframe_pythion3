# -*- coding: utf-8 -*-
import os
import shutil
import sys
# 如果不行，加上之前的基础信息
try :
    basic_python
except NameError:
    sys.path.append('\\'.join(os.path.realpath(__file__).split('\\')[:-2]))
    import basic_python.basic_function_python as basic_function_python


def Is_File_Exist(file_input):
    '''删除所有文件
    Args:  
    '''
    return os.path.exists(file_input)
    
def Print_Line_In_File(file_input):
    '''读文件
    Args:  
    '''
    if Is_File_Exist(file_input):     
        data_input = open(file_input)
        print(type(data_input))
        for each_line in data_input:
            print(each_line)
        data_input.close()

def Read_Content_In_File(file_input):
    '''返回文件内容
    Args:  
    '''
    if Is_File_Exist(file_input):     
        data_input = open(file_input,"r")
        content_str=data_input.read()
        data_input.close()
        return content_str
        
def Write_Content_To_File(content,file_input):
    '''重新写文件
    Args:  
    '''
    try:
        file_using = open(file_input,'w',errors='ignore')
        file_using.write(content)
        file_using.close()
    except IOError:
        print("写入错误")

def Append_Content_To_File(content,file_input):
    '''重新写文件
    Args:  
    '''
    try:
        file_using = open(file_input,'a')
        file_using.write(content)
        file_using.close()
    except IOError:
        print("写入错误")
 
def Say_Something():
    '''修改
    Args:
        
    '''
    print("曹维，人生真是无聊啊！")
	
	
if __name__=="__main__":
    Say_Something()
