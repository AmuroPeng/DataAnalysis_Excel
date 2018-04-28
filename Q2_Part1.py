#!/usr/bin/env python
# -*- coding: utf-8 -*-

import daoru
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
        self.tab = 0

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
        elif menu == 10:
            self.f += time


table = daoru.daoru('1.xlsx')
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
        # print(int(table.row_values(i)[0]), int(table.row_values(i)[1]),
        #             int(table.row_values(i)[2]))
        list.append(temp)  # 不同的话就增加list用户


# print(len(list))

def match(x, y):
    for i in range(len(list)):
        xxx = [x.a, x.b, x.c, x.d, x.e, x.f, x.g]
        yyy = [y.a, y.b, y.c, y.d, y.e, y.f, y.g]
        return corrcoef(xxx, yyy)
num = 1
result = []
result.append([user('xff', 11, 0)])
for i in list:
    if i.tab != 0:
        continue
    i.tab = num
    tempp = []
    tempp.append(i)
    for j in list:
        if i == j or j.tab != 0:
            continue
        if abs(match(i, j)) > 0.8:
            j.tab = num
            tempp.append(j)
    num += 1
    result.append(tempp)


# show.show(list)

# for each_list in result:
#     print(int(result.index(each_list)))
#     for each_user in each_list:
#         print(int(each_user.name))
#     print('###################################')
def join_strings(each_list):
    results = ""
    for each_user in each_list:
        results += str(each_user.name)
        results += ' '
    return results


num = 0
for each_list in result:
    print('#####' + str(num) + '#####')
    print(join_strings(each_list))
    num += 1

def get_result():
    return result