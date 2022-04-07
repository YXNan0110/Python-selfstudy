names = ["cow","rabbit"]

names.append("hen")          # 末端插入
print(names)

names.insert(2,"horse")      # 指定位置插入
print(names)

citys = ["BJ","QD","SH"]
names.extend(citys)          # 将另一list合并进来
print(names)

names.pop(-1)                # pop删除指定key
print(names)

names.remove("QD")           # pop删除指定value
print(names)

print(names.index("horse"))  # 查某一元素索引
# 在不知道某一元素位置的情况下修改元素可以如下
index_ = names.index("horse")
names[index_] = "dog"
print(names)

