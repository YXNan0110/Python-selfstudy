# 通过交互式输入个人信息打印完整的ID卡

name = input('name:')
age = input('age:')
hometown = input('hometown:')
hobby = input('hobby:')

information = f'''
---------info of {name}---------
Name : {name}
Age : {age}
Hometown : {hometown}
Hobby : {hobby}
--------------end---------------
'''

print(information)


# 笔记：三个引号表示可换行字符串
# f表示该字符串中包裹着外面的变量，且变量在字符串中要用大括号表示

