# 创建dict形式
d = {}

d["name"] = "Harry"
print(d)

d["hometown"] = "UK"
d["hobby"] = "magic"
print(d)
# d.pop("hometown")         # 删除指定key
# print(d)
del d["hometown"]           # 同pop
print(d)

# dict无切片操作
# key可查是否在dict中，不能直接查value

print(d.keys())             # 把所有key取出
print(d.values())           # 把所有value取出
print(d.items())            # 把dict变成list

for k,v in d.items():       # 同时打印key和value
    print(k, v)

for k in d:                 # 同上但效率高
    print(k, d[k])









