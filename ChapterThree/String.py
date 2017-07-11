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

print 'Price of eggs: $%d' %42 #带符号的十进制整数
print 'Hexadecimal price of eggs:%x' %42 #不带符号的十六进制 小写
from math import pi
print 'Pi: %f...' %pi   #十进制浮点数
print 'Pi: %.10f' %pi   #十进制浮点数
print 'Very inexact estimate of pi: %i' %pi  #带符号的十进制整数
print 'Using str : %s' %42L  #字符串 使用str转换任意Python对象
print 'Using repr: %r' %42L  #字符串 使用repr转换任意Python对象

#字段宽度和精度
#这两个参数都是整数，通过点号隔开
print '%10f' %pi #字段宽10
print '%10.2f' %pi #字段宽10 精度2
print '%.2f' %pi #精度2 如果只给出精度，必须包含点号
print '%.5s' %'Guido van Rossum'
print '%.*s' %(5,'Guido van Rossum') #可使用*号最为字段宽度或精度（或者两者都使用*），此时数值从元组参数中读出
print '%*.*s' %(10,5,'Guido van Rossum')

#符号、对齐和0填充
#在字段宽度和精度值之前还可以放置一个“标表”，该标表可以是零、加号、减号或空格。
#零表示0填充
print '%010.2f' %pi

#减号（-）用来左对齐数值
print '%-10.2f' %pi

#空白‘标表’表示在正数前加上空格
print ('% 5d' %10)+'\n'+('% 5d' %-10)

#加号（+），它表示不管是正数还是负数都标示出符号
print ('%+5d' %10)+'\n'+('%+5d' %-10)

#字符串方法
#find方法
#find方法可以在一个较长的字符串中查找子字符串。返回子字符串在字符串中的最左端索引，没有找到返回-1,这个方法还可以接收可选的起始点和结束点的参数
subject='$$$ Get rich now !!! $$$'
print subject.find('$$$')
print subject.find('$$$',1) #只提供起始点
print subject.find('!!!')
print subject.find('!!!',0,16) #提供起始点和结束点 包含第一个索引，但不包含第二个索引


#join方法
#用来在队列中添加元素，需要添加队列的元素必须是字符串，是split方法的逆方法
seq=[1,2,3,4,5]
sep='+'
# print sep.join(seq)
seq=['1','2','3','4','5']
print sep.join(seq)

dirs='','usr','bin','env'
print '/'.join(dirs)
print 'C:'+'\\'.join(dirs)

#lower方法 返回字符串的小写字母版
print 'Trondheim Hammer Dance'.lower()

#title方法 将字符串转换成标题 也就是所有单词的首字母大写，其他字母小写
print "that's all folks".title()

#strip方法 返回去除两侧（不包括内部）空格的字符串
print '    internal whitespace is kept    '.strip()

#strip方法 也可以指定需要去除的字符，将它们列为参数即可
print '****SPAM * for * everyone!!!***'.strip(' *!')

#translate方法
#translate方法和replace方法一样，可以替换字符串中的某些部分，但是只处理单个字符。

#在使用translate转换之前，需要先完成一张转换表，转换表中是以某字符替换某字符的对应关系，一般使用string模块中的maketrans函数

#maketrans函数接收两个参数：两个等长的字符串，表示第一个字符串中的每个字符都用第二个字符串中相同位置的字符替换

from string import maketrans
table=maketrans('cs','kz')
print len(table) #这个表有多达256个项目，事实上是字符串

#创建这个表后，可以将它用作translate方法的参数，进行字符串转换
print 'this is an incredible test'.translate(table)

#translate的第二个参数是可选的，该参数用来删除指定的字符。
print 'this is an incredible test'.translate(table,' ')