# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce

def str2float(s):
    new = s.split('.')
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(s):
        return DIGITS[s]

    int_1 = reduce(lambda x, y: x * 10 + y, map(char2num, new[0]))
    float_1 = reduce(lambda x, y: x * 10 + y, map(char2num, new[1])) / (10 ** len(new[1]))

    return int_1 + float_1, int_1, float_1

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



