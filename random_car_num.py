# 用随机数产生车牌号
# 首位必须是A-Z的字母，后五位是字母和数字的随机组合
import random   # 导入random模块
import string

count = 1

while count <= 3:

    first = random.choice(string.ascii_uppercase)
    car_nums = []

    for i in range(1,21):
        num = string.ascii_uppercase + string.digits
        rand_num = random.sample(num, 5)
        print(f"京{first}-{''.join(rand_num)}", end='  ')
        car_num = f"京{first}-{''.join(rand_num)}"
        car_nums.append(car_num)

        if i % 5 == 0:
            print()

    new = input("请输入你喜欢的号码：").strip()  # 可以去掉输入时不小心打上的空格
    if new in car_nums:
        print(f"恭喜您，您的车牌号为{new}")
        break
    else:
        print("抱歉，您所输入的车牌号不在可选范围中！")
        count += 1
        continue




# random用法：random.choice()从括号中random一个元素出来,可以是list也可以是字符串
# random.sample(a,n)从a中random出n个元素
# "str".join(list)表示将list中的元素用str连接起来，str也可以为空
# random.randint(x,y)表示从x到y之间random打印一个随机数
# string模块可以帮忙导入字母和数字,string.ascii_uppercase & string.ascii_lowercase & string.punctuation & string.digits
# 上述四个分别为大写字母，小写字母，特殊字符和数字



