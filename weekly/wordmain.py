#!usr/bin/env python
# -*-coding:utf-8 -*-
# Author:wangzb87

import os
import sys
print(sys.path)  
from list.list_weekly import *
from read.read_text import *
from analysis.prepare.prepare_text import *
from analysis.prepare.word_cut import *
from analysis.model.word_frequency import *
from analysis.view.word_cloud import *
from analysis.view.word_show import *

def wordmain():
    dir_aim = input("请输入周报文件夹路径：")
    # save_path= dir_aim+'/set/'
    text_group_path = list_weekly(dir_aim,False)
    f_all = read_text(text_group_path)
    f_prepare = prepare_text(f_all)
    object_list=word_cut(f_prepare)
    word_counts_top=word_frequency(object_list)
    wc=word_cloud(word_counts_top)
    word_show(wc)
    

if __name__ == '__main__':
    wordmain()
