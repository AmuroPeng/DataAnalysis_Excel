#!/usr/bin/env python
# -*- coding: utf-8 -*-

import daoru
from math import sqrt

list_a = []
list_b = []
list_c = []
list_d = []
list_e = []
list_f = []
list_g = []

table = daoru.daoru('2.xlsx')
nrows = table.nrows  # 获取表的行数
list = []  # 记录所有用户编号
for i in range(nrows):  # 循环逐行 print(table.row_values(i)[0])
    if table.row_values(i)[0] == 'a':
        if table.row_values(i)[1]=='无':
            list_a.append(table.row_values(i)[2])
        else:
            list_a.append(table.row_values(i)[1])
    if table.row_values(i)[0] == 'b':
        if table.row_values(i)[1]=='无':
            list_b.append(table.row_values(i)[2])
        else:
            list_b.append(table.row_values(i)[1])
    if table.row_values(i)[0] == 'c':
        if table.row_values(i)[1]=='无':
            list_c.append(table.row_values(i)[2])
        else:
            list_c.append(table.row_values(i)[1])
    if table.row_values(i)[0] == 'd':
        if table.row_values(i)[1]=='无':
            list_d.append(table.row_values(i)[2])
        else:
            list_d.append(table.row_values(i)[1])
    if table.row_values(i)[0] == 'e':
        if table.row_values(i)[1]=='无':
            list_e.append(table.row_values(i)[2])
        else:
            list_e.append(table.row_values(i)[1])
    if table.row_values(i)[0] == 'f':
        if table.row_values(i)[1]=='无':
            list_f.append(table.row_values(i)[2])
        else:
            list_f.append(table.row_values(i)[1])
    if table.row_values(i)[0] == 'g':
        if table.row_values(i)[1]=='无':
            list_g.append(table.row_values(i)[2])
        else:
            list_g.append(table.row_values(i)[1])
print('综艺娱乐')
print(list_a)
print('新闻时事')
print(list_b)
print('体育竞技')
print(list_c)
print('生活服务')
print(list_d)
print('科学教育')
print(list_e)
print('家庭影院')
print(list_f)
print('电视剧场')
print(list_g)
