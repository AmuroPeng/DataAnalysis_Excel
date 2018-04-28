#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

def daoru(xlsx):
    data = xlrd.open_workbook(xlsx)  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    for i in range(nrows):  # 循环逐行打印
        if i == 10:
            break
        # print(table.row_values(i)[:3])  # 取前十三列
    return table
