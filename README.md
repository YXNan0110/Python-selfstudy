# Python-selfstudy
## Python学习笔记  
### 输入和输出  

输出：print()**字符串**要用**单引号**<br>
eg:print('hello,', name)<br>

输入：name = input()<br>

### 字符串

**转义字符**例如\n表示**换行**，\t表示制表<br>
如果字符串里不需要转义，用**r''** 表示，引号中的内容不转义<br>

**布尔值**and or not

**格式化**<br>
- %d 整数    
- %f 浮点数（小数）   
- %s 字符串    
- %x 十六进制整数    

例如：保留两位小数.2f<br>

### list 和 tuple
**list**用**中括号**，list索引从0开始，并且用中括号表示第几位，若倒数第几位则加负号<br>
list**追加元素**用.append，**插入元素**用.insert，删除元素用.pop(i)<br>
eg:classmate[0],classmate[2][2],classmate[-1]<br>

**tuple**用**小括号**，且tuple内元素不能改变<br>
eg:单元素t = (1,)<br>

### 循环

**if...elif...else**,注意，if、elif、else后面都要加**冒号！**<br>

**for i in L**,L应当为一个list or tuple，L后面要加**冒号！**<br>

**while循环**加**冒号！** continue、break语法同c<br>

### dict 和 set
dict和set都是一组key的集合<br>
**dict**用大括号表示，格式为索引:内容（即key:value）<br>
如果要查找需要d[]，中括号中为索引<br>
注意，dict中的索引（即key）是无序排列的<br>

**set**是数学意义上无序和无重复元素的集合，set()<br>

### 定义函数
**def** 函数名、括号、括号中返回的参数，加**冒号！**<br>
返回多个值用逗号隔开，eg:return nx,ny<br>

**调用函数**调用函数包中的函数<br>
import xxx,函数包.函数<br>

**默认参数**是指在定义参数时就给某些参数赋以一定的值，如果输入值相同可以不输入，不同时才输入<br>

**关键字参数**两个*+参数名，这个参数中是一个dict，可以添加任意参数<br>
**命名关键字参数**一个*+参数名，这个参数中是一个tuple<br>
注意定义参数时命名关键字参数在前，关键字参数在后<br>

### 递归函数
在函数中调用函数，类似递推公式，找到每一步的特性，放到函数中<br>
其实这里我也不太明白，等有空学习数据结构好好研究<br>

### 切片
取list or tuple中的元素<br>
- 第一个数 起始数   
- 第二个数 末尾数    
- 第三个数 间隔数   
**中间用冒号隔开**<br>
字符串也可以用切片<br>但必须要用中括号<br>
就算是倒数第几个数切的方式也是正数的<br>

### 迭代
**for...in**<br>
dict默认迭代key，迭代**value**要用**for value in d.values()**,同时迭代用**d.items()**<br>
判断是否可迭代，需要用**from collections.abc import Iterable**<br>
insinstance(xxx,Iterable)会输出True/False<br>
**下标循环**可以用**enumerate**，把list变成**索引-元素对**的形式<br>
eg:for i, value in enumerate(['A','B','C'])<br>

### 列表生成式
中括号中依次放入**输出结果**，**循环式**，**条件判断**<br>
eg:[k + '=' + v for k, v in d.items()]<br>
列表生成式中的if语句**不能**带else，但如果if语句**在循环式之前**，必须要加else，否则无法判断x结果输出给for循环<br>

### 生成器
只需要把列表生成式的中括号改为**小括号**即可，eg:g=(x * x for x in range(10))<br>
生成器generator也是可迭代对象，可以用for...in，也可以用**next函数**调用下一个<br>
generator函数中包含**yield**关键字，相当于普通函数中的return返回，再次执行时从上次返回的语句处执行，再通过**next函数**执行，有点像普通函数的print<br>

### 迭代器
判断是否是可迭代对象Iterable可以用**isinstance函数**，eg:insinstance((x for x in range(10)), Iterable)<br>
**迭代器Iterator**是指可以被next()调用并不断返回下一个值的对象<br>
Iterator同样也可以用**isinstance函数**判断<br>
把list、dict、str等*Iterable*变成*Iterator*可以用**iter函数**<br>
注意：Iterator的计算是**惰性**的，在需要返回下一个数据时才会计算，可以表示无限大的数据流<br>
凡是可作用于**for循环**的对象都是**Iterable类型**，凡是可作用于**next()函数**的对象都是**Iterator类型**，它们表示一个惰性计算的序列<br>

### 高阶函数
函数调用的结果可以赋给变量<br>
- 函数结果可以赋给变量   
- 函数本身可以赋值给变量 
   
**高阶函数**：一个函数可以接收另一个函数作为参数<br>   

### map函数
map函数接收两个参数，分别是**函数**和**Iterable**，把结果作为新的**Iterator**返回，由于Iterator是惰性计算序列，所以输出时要用**list函数**输出<br>

### reduce函数
同样接收两个参数，分别是**函数**和**序列**，序列每两个元素做一次函数运算，以此向后累积，eg：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)<br>
**lambda**函数可接受任意数量参数，生成一个表达式，格式为参数:表达式，eg：x = lambda a, b, c : a + b + c<br>

### filter函数
同样接收两个参数，分别是函数和序列，把传入的函数依次作用于每个元素，根据返回值0or1决定保留还是舍弃，eg：filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])<br>
注意：filter返回的是**Iterator**，需要强迫list函数输出<br>

### sorted函数
sorted函数用于排序，可以输入**一个序列**，也可以输入**序列**和**函数**，函数作用于每一个元素上。eg：sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)<br>

### 局部变量与全局变量
在函数中定义的变量称为**局部变量**，在程序一开始定义的变量称为**全局变量**<br>
局部变量*作用域*是定义该变量的**函数**<br>
变量的查找优先级是**局部变量>全局变量**<br>








