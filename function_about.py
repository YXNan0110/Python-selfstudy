# 函数相关笔记

def calc(x,y):          # xy是形参，形参只能存活在函数定义内
    rut = x ** y
    print(rut)


a = 5
b = 4

calc(a,b)               # ab是实参

# 默认参数
def stu_register(name, age, course, country = 'CN'):       # 默认参数必须放到最后
    print("学生信息如下：")
    print("姓名：", name)
    print("age：", age)
    print("国籍：", country)
    print("课程：", course)

stu_register("Alex", 20, "python")
stu_register("Bob", 22, "linux")
stu_register("Catherine", 18, "linux", "UK")


# 命名关键字参数与关键字参数
def stu_info(name, age, *args, **kwargs):           # 命名关键字参数格式是tuple，关键字参数格式是dict
    print(name, age, args, kwargs)

stu_info("Alex", 20, "CN", "Male", addr = "SD Province")
stu_info("Bob", 22, "CN", "Male", hobby = "skating")
stu_info("Catherine", 18, "Female", Tel = "12345678")


# 练习题：函数内为自己写的
def print_info(*args, **kwargs):
    print("-----info-----")

    for key_ in kwargs:
        print(key_,":",kwargs[key_])


print_info(name = "Alex", age = 22, sex = "M")
print_info(name = "Jack", age = 26, sex = "M", hobbie = "学习")


# 函数返回值用于print_ = print_info()，等号右侧就是函数的返回值，被赋返回值的参数可以用作其他运算，只是调用函数不涉及到等号
# 且函数见到return代表函数结束



