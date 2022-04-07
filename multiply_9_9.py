# 打印九九乘法表

i = 1

while i <= 9:

    j = 1

    while j <= i:
        print(f"{i}*{j}={i*j}",end=' ')   # print函数中end自带换行，所以需要令end=‘ ’
        if i==j:
            print()
        j += 1

    i += 1




