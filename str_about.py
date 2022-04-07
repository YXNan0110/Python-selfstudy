a = "Life is better than your prediction."

print(a.center(50,'-'))    # output: -------Life is better than your prediction.-------
print(a.count("i",0,5))    # 0~5搜索i的个数，不加0,5则全局搜索
print(a.endswith("."))     # True，以xx结尾
print(a.startswith("L"))   # True，以xx开头

print(a.find("think"))     # return -1，如果能找到则返回索引
print(a.isdigit())         # 判断是否是整数

print(a.replace("i"," ",1))    # 后者替换前者,数字代表替换几个
# 注意，字符串不能单个字符进行改动，这里a没有发生变化，replace后必须要另附值

print(a.split())           # 在空格处将string划分为list




