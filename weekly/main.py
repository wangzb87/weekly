#!usr/bin/env python
# -*-coding:utf-8 -*-
# Author:wangzb87

import os
import sys
sys.path.append("../")
print(sys.path)  
from list.list_weekly import *
from read.read_weekly import *
from process.append_weekly import *
from write.write_weekly import *

def main():
    dir_aim = input("请输入周报文件夹路径：")
    save_path= dir_aim+'/set/'
    excel_group_path = list_weekly(dir_aim,False)
    dframes = read_weekly(excel_group_path)
    df = append_weekly(dframes)
    write_weekly(save_path,'周报汇总.xls',df)
    print("已汇总完毕，周报汇总文件保存在"+save_path)

if __name__ == '__main__':
    main()
