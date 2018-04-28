import Q2_Part1
import Q2_Part2

data = Q2_Part1.get_result()


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


result = []
result.append([0, 0, 0, 0, 0, 0, 0])
num = 1
for each_list in data:
    result.append([0, 0, 0, 0, 0, 0, 0])
    for each_user in each_list:
        result[num][0] += each_user.a
        result[num][1] += each_user.b
        result[num][2] += each_user.c
        result[num][3] += each_user.d
        result[num][4] += each_user.e
        result[num][5] += each_user.f
        result[num][6] += each_user.g
    maxx = max(result[num][0], result[num][1], result[num][2], result[num][3], result[num][4], result[num][5],
               result[num][6])
    if maxx == result[num][0]:
        print('第' + str(num-1) + '组用户更偏爱' + '综艺娱乐' + '类型的节目')
    elif maxx == result[num][1]:
        print('第' + str(num-1) + '组用户更偏爱' + '新闻时事' + '类型的节目')
    elif maxx == result[num][2]:
        print('第' + str(num-1) + '组用户更偏爱' + '体育竞技' + '类型的节目')
    elif maxx == result[num][3]:
        print('第' + str(num-1) + '组用户更偏爱' + '生活服务' + '类型的节目')
    elif maxx == result[num][4]:
        print('第' + str(num-1) + '组用户更偏爱' + '科学教育' + '类型的节目')
    elif maxx == result[num][5]:
        print('第' + str(num-1) + '组用户更偏爱' + '家庭影院' + '类型的节目')
    elif maxx == result[num][6]:
        print('第' + str(num-1) + '组用户更偏爱' + '电视剧场' + '类型的节目')
    print(result[num])
    num += 1

