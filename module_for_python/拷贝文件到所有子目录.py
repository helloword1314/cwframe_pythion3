# -*- coding: UTF-8 -*-
import os,shutil



def ensure_unicode(v):
    if isinstance(v, str):
        v = v.decode('utf8')
    return unicode(v)  # convert anything not a string to unicode too


file_path=ensure_unicode(r"F:\\zhao\\a\\wm3.jpg")
folder_path=ensure_unicode(r"F:\\zhao\\UpdateMax")




def copy_file_to_subfolder(file_path,folder_path):
    for f1 in os.listdir(folder_path):
        file_path2 = os.path.join(folder_path,f1)
        if os.path.isdir(file_path2):
            file_path2=file_path2+"\\wm3.jpg"
            shutil.copyfile(file_path,file_path2)
            
copy_file_to_subfolder(file_path,folder_path)                




                
                        



# 从文件夹B到文件夹A，相同子文件夹删除
def trans_BFolder_to_AFolder_deleteASubFolder(apath,bpath):
    for bf1 in os.listdir(bpath):
        b_file_path = os.path.join(bpath,bf1)
        if os.path.isdir(b_file_path):
            print b_file_path
            for af1 in os.listdir(apath):
                a_file_path = os.path.join(apath,af1)
                if os.path.isdir(a_file_path):
                    if af1==bf1:
                        shutil.rmtree(a_file_path)
                        shutil.move(b_file_path,apath)
            
                        
                        
            #for kind_filter in kind_filters:
                
                #if file_path.endswith(kind_filter):
                    #os.remove(file_path)



        #elif os.path.isdir(file_path):
            #deleteKindFileAndDown(file_path)

            
#copy_file_to_subfolder(apath,bpath)











































