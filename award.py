# 设置公司抽奖程序，300名员工，抽3次奖，第一次抽三等，一二三等奖个数分别为3、6、30，每个员工限中奖一次
# 设置两个序列，一个a负责删除数据，a123负责抽取数据
import random

i = 1
a = list(range(300))

while i <= 3:
    if i == 1:
        a1 = a
        print("开始抽取三等奖......")
        new_1 = random.sample(a1,30)
        print(new_1)

        new_1.sort(reverse=True)

        for key in new_1:
            a.pop(key)

        i += 1
        a = list(range(300))

    if i == 2:
        a2 = a1
        print("开始抽取二等奖......")
        new_2 = random.sample(a2,6)
        print(new_2)

        new_2 = new_2 + new_1
        new_2.sort(reverse=True)

        for key in new_2:

            a.pop(key)

        i += 1
        a2 = a
        a = list(range(300))

    if i == 3:
        a3 = a2
        print("开始抽取一等奖......")
        new_3 = random.sample(a3,3)
        print(new_3)

        new_3 = new_3 + new_2
        new_3.sort(reverse=True)

        for key in new_3:
            a.pop(key)
        i += 1



