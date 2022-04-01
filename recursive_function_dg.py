# 汉诺塔的移动可以用递归函数非常简单地实现。
#
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法。
# 汉诺塔原理：上面n-1个挪到B上，最下面一个挪到C上，B上的n-1个挪到C上

def move(n, a, b, c):

    if n == 1:

        print(a, '-->', c)

    else:

        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

    return

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C

move(3, 'A', 'B', 'C')






