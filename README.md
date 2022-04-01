# Python-selfstudy
## Python学习笔记  
### 输入和输出  

输出：print()**字符串**要用**单引号**<br>
eg:print('hello,', name)<br>

输入：name = input()<br>

### 字符串

**转义字符**例如\n表示**换行**，\t表示制表<br>
如果字符串里不需要转义，用**r''**\表示，引号中的内容不转义<br>

**布尔值**and or not

**格式化**<br>
-%d 整数    
-%f 浮点数（小数）   
-%s 字符串    
-%x 十六进制整数    

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
-第一个数 起始数   
-第二个数 末尾数    
-第三个数 间隔数   
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







