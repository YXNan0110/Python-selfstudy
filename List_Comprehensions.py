# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [value.lower() for value in L1 if isinstance(value, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')





