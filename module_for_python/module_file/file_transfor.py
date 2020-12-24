# -*- coding: utf-8 -*-
import os
import MaxPlus
import inspect

def printsomething():
    '''修改Sddraft文件的参数。（一般就修改开启WMS、WFS功能）

    Args:
        sddraft_file_path: .sddraft文件的路径。
    '''
    print(123)

def reset():
	'''重新启动reset
    '''
	MaxPlus.FileManager.Reset(True)

def showClasses():
	classes = inspect.getmembers(MaxPlus, inspect.isclass)
	for c in classes :
		name = str(c[0])
		print(name+"\n")
		xx=str(c[1])
		print(xx+"\n")
	
	
if __name__=="__main__":
    printsomething()
