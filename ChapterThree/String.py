#coding=utf-8
#字符串基本操作
#所有标准序列操作（索引、分片、乘法、判断成员资格、求长度、取最小值和最大值）对字符串同样适用
#由于字符串是不可变的，因此，类似以下的分片赋值是不合法的
website='http://www.python.org'
#website[-3:]='com'

#字符串格式化
#使用字符串操作符%来实现  %也可用用作模运算 求余操作符

#格式化为字符串示例
format='Hello, %s. %s enough for ya' #%s称为转换说明符，它们标记了需要插入转换值的位置 s表示值会被格式化为字符串
values=('world','Hot')  #如果使用类别或者其他序列代替元组，那么序列就会被解释为一个值。只有元组和字典可以格式化一个以上的值
print format % values

#格式化实数
#使用f作为转换说明符类型 同时提供所需要的精度：一个点加上希望保留的小数位数
format='Pi with three decimals:%.3f'
from math import pi
print format % pi


#string模块提供另外一种格式化值的方法 模板字符串
#substitute这个模板方法会用传递进来的关键字参数foo替换字符串中的$foo
from string import Template
s=Template('$x. glorious $x!')
y=s.substitute(x='slurm')
print s
print y

#string模块提供另外一种格式化值的方法 模板字符串
#substitute这个模板方法会用传递进来的关键字参数foo替换字符串中的$foo
from string import Template
s=Template('$x. glorious $x!')
s.substitute(x='slurm')
print s

#替换字段是单词的一部分，参数名须用括号括起来
s=Template("It's ${x}tastic")
print s.substitute(x='slurm')

#使用$$插入美元符号
s=Template('Make $$ selling $x!')
print s.substitute(x='slurm')

#除了关键字参数之外，还可以使用字典变量提供值/名称对
s=Template('A $thing must never $action')
d={}
d['thing']='gentleman'
d['action']='show his socks'
print s.substitute(d)

#如果右操作数是元组的话，则其中的每一个元素都会被单独格式化，每个值都需要一个对应的转换说明符。
#如果需要转换的元组作为转换表达式的一部分存在，那么必须将它用圆括号括起来。
print '%s plus %s equals %s' %(1,1,2)
#print '%s plus %s equals %s' %1,1,2  #Lacks parentheses!


