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





def Delete_ALL_In_Folder(folder_input):
    '''删除所有文件
    Args:  
    '''
    for f in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def Delete_Startswith_Str_In_Folder(folder_input,startswith_str):
    '''删除以某某开头的文件
    Args:
        startswith_str是某某开头
    '''
    for f1 in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f1)
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            if file_name.find(startswith_str)>-1:
                os.remove(file_path)
        elif os.path.isdir(file_path):
            Delete_Startswith_Str_In_Folder(file_path,startswith_str)

def Delete_Except_Startswith_Str_In_Folder(folder_input,startswith_str):
    '''删除以某某开头的文件之外的文件
    Args:
        startswith_str是某某开头
    '''
    for f1 in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f1)
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            if file_name.find(startswith_str)==-1:
                os.remove(file_path)
        elif os.path.isdir(file_path):
            Delete_Except_Startswith_Str_In_Folder(file_path,startswith_str)

def Delete_Kind_Array_In_Folder(folder_input,kind_array):
    '''删除多种特定类型文件
    Args:
        kind_array是[".txt",".abc"]
    '''
    for f1 in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f1)
        if os.path.isfile(file_path):
            for kind_filter in kind_array:
                if file_path.endswith(kind_filter):
                    os.remove(file_path)
        elif os.path.isdir(file_path):
            Delete_Kind_Array_In_Folder(file_path,kind_array)

def Copy_Folder_To_Another_Folder(folder_input,folder_output):
    '''复制
    Args:
        folder_output可以不存在
    '''
    shutil.copytree(folder_input,folder_output)
    
def Say_Something():
    '''修改
    Args:
        
    '''
    print("曹维，人生真是无聊啊！")
	
	
if __name__=="__main__":
    print("1-删除所有的文件")
    print("2-删除特定类型的文件")
    print("3-删除某某开头的文件")
    print("4-删除某某开之外的文件")
    while True :
        method_file= input("what do you want:")
        if method_file== 1:
            path_input = raw_input("input folder:")
            Delete_ALL_In_Folder(path_input)
            print("-------------------all deleted------------------")
        elif method_file== 2:
            path_input = raw_input("input folder:")
            kind_type = raw_input("input kind,such as '.USX' :")
            kind_filters=[kind_type]
            deleteKindFileAndDown(path_input,kind_filters)
            print("-------------------all deleted------------------")
        elif method_file== 3:
            path_input = raw_input("input folder:")
            capital = raw_input("input capital,such as 'tttt' :")
            Delete_Startswith_Str_In_Folder(path_input,capital)
            print("-------------------all deleted------------------")
        elif method_file== 4:
            path_input = raw_input("input folder:")
            capital = raw_input("input capital,such as 'tttt' :")
            Delete_Except_Startswith_Str_In_Folder(path_input,capital)
            print("-------------------all deleted------------------")
        elif method_file== 5:
            path_input = raw_input("input folder:")
            path_output = raw_input("output folder:")
            Move_Folder_To_Another_Folder(path_input,path_output)
            print("-------------------all done------------------")
         
