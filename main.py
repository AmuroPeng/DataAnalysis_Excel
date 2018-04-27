#!/usr/bin/env python
# -*- coding: utf-8 -*-

import daoru
import edit

from math import sqrt


def multipl(a, b):
    sumofab = 0.0
    for i in range(len(a)):
        temp = a[i] * b[i]
        sumofab += temp
    return sumofab


def corrcoef(x, y):
    n = len(x)
    # 求和
    sum1 = sum(x)
    sum2 = sum(y)
    # 求乘积之和
    sumofxy = multipl(x, y)
    # 求平方和
    sumofx2 = sum([pow(i, 2) for i in x])
    sumofy2 = sum([pow(j, 2) for j in y])
    num = sumofxy - (float(sum1) * float(sum2) / n)
    # 计算皮尔逊相关系数
    den = sqrt((sumofx2 - float(sum1 ** 2) / n) * (sumofy2 - float(sum2 ** 2) / n))
    return num / den


class user:
    def __init__(self, name, menu, time):
        self.name = 99999
        self.menu = 0
        self.time = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.g = 0

    def setter(self, name, menu, time):
        self.name = name
        self.menu = menu
        self.time = time
        if menu == 1:
            self.b += time
            self.g += time
        elif menu == 2:
            self.a += time
            self.g += time
        elif menu == 3:
            self.b += time
            self.e += time
            self.g += time
        elif menu == 4:
            self.a += time
            self.g += time
        elif menu == 5:
            self.a += time
            self.g += time
        elif menu == 6:
            self.a += time
            self.g += time
        elif menu == 7:
            self.b += time
        elif menu == 8:
            self.c += time
        elif menu == 9:
            self.b += time
            self.e += time
        elif menu == 6:
            self.f += time


table = daoru.daoru()
nrows = table.nrows  # 获取表的行数
list = []  # 记录所有用户编号
for i in range(nrows):  # 循环逐行 print(table.row_values(i)[0])
    if i != 0 and int(table.row_values(i)[0]) == int(table.row_values(i - 1)[0]):  # 用户相同，直接添加属性即可
        list[-1].setter(int(table.row_values(i)[0]), int(table.row_values(i)[1]),
                        int(table.row_values(i)[2]))
    else:
        temp = user(None, None, None)
        temp.setter(int(table.row_values(i)[0]), int(table.row_values(i)[1]),
                    int(table.row_values(i)[2]))
        list.append(temp)  # 不同的话就增加list用户
print(len(list))
for i in range(len(list)):
    x = [list[0].a,list[0].b,list[0].c,list[0].d,list[0].e,list[0].f,list[0].g]
    y = [list[i].a,list[i].b,list[i].c,list[i].d,list[i].e,list[i].f,list[i].g]
    print (corrcoef(x, y))