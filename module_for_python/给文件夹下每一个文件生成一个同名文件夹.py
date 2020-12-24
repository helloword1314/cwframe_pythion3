# -*- coding: UTF-8 -*-
import os,shutil
#apath="F:\\20200525\\test\\"
apath="F:\\zhao\\UpdateMax\\"


def ensure_unicode(v):
    if isinstance(v, str):
        v = v.decode('utf8')
    return unicode(v)  # convert anything not a string to unicode too


          


# 给文件一个文件夹
def give_file_a_folder(apath):
    for af1 in os.listdir(ensure_unicode(apath)):
        file_path = ensure_unicode(os.path.join(apath,af1))
        if os.path.isfile(file_path):
            f_name,f_type=os.path.splitext(af1)
            f_path,f_message=os.path.splitext(file_path)
            newfilepath = f_path + "\\"
            
            print file_path
            print newfilepath
            os.mkdir(f_name)
            shutil.move(file_path,newfilepath)
                       


 
give_file_a_folder(apath)











































