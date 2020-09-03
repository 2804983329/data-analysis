# -*- coding: utf-8 -*-

import pyexcel as pe

e1 = pe.get_book_dict(file_name = "1.xlsx") #读取表1为字典e1
e2 = pe.get_book_dict(file_name = "2.xlsx") #读取表2为字典e2

e1.update(e2) #合并两个表的内容

v=[] #初始化列表

#两个表的内容转换为列表

for key in e1: #我想把这两行改为一个列表推导式，但是不成功：v = [e1[key] for key in e1]，还请帮忙，多谢
    v += e1[key]

#保存文件
pe.save_as(array = v, dest_file_name = "3.xlsx") 
