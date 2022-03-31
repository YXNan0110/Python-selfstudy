# life-in-BJ
## Python学习笔记  
### 输入和输出  

输出：print()**字符串**要用**单引号**<br>
eg:print('hello,', name)<br>

输入：name = input()<br>

### 字符串

**转义字符**例如\n表示**换行**，\t表示制表<br>
如果字符串里不需要转义，用**r''**\表示，引号中的内容不转义<br>

**布尔值**and or not

**格式化**
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
**dict**用大括号表示，格式为索引：内容<br>
如果要查找需要d[]，中括号中为索引<br>
**set**是数学意义上无序和无重复元素的集合，set()<br>









