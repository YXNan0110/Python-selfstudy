# 将班级中的同学按照成绩不同进行分类，10分为一档，最后一档为59-0
# 班级列表如下：classmates = [['李林甫', 95], ['杜牧', 84], ['薛涛', 79], ['杨国忠', 89], ['李商隐', 34], ['高适', 100],['历真', 70]]

classmates = [['李林甫', 95], ['杜牧', 84], ['薛涛', 79], ['杨国忠', 89], ['李商隐', 34], ['高适', 100],['历真', 70]]

class_1 = []
class_2 = []
class_3 = []
class_4 = []
class_5 = []

for i in classmates:
    if i[1] >= 90:
        class_1.append(i)
    elif i[1] >= 80 and i[1] < 90:
        class_2 .append(i)
    elif i[1] >= 70 and i[1] < 80:
        class_3.append(i)
    elif i[1] >= 60 and i[1] < 70:
        class_4.append(i)
    else:
        class_5.append(i)

print(class_1)
print(class_2)
print(class_3)
print(class_4)
print(class_5)





