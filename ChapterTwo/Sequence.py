# coding=utf-8
# Python包含6种内建序列：列表、元组、字符串、Unicode字符串、buffer对象、xrange对象

# 列表与元组的主要区别：列表可以修改、元组不能

# 序列举例
edward =['Edward Gumby',42]
john=['John Smith',55]
database=[edward,john]

print database

# 通用序列操作
# 索引
greeting='Hello'
print greeting[0]

# 使用负数作为索引时，从序列都最后一个元素开始计数，最后1个元素的位置编号是-1
print greeting[-1]

# 字符串字面值能够直接使用索引，而不需要一个变量引用它们
print 'Hello'[0]

# 如果一个函数返回一个序列，那么可以直接对返回结果进行索引操作。
# fourth = raw_input('Year: ')[3]
# print fourth

# months=['January','February','March','April','May','June','July','August','September','October','November','December']
# endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
# year=raw_input('Year: ')
# month=raw_input('Month(1-12): ')
# day=raw_input('Day(1-31): ')
#
# month_number=int(month)
# day_number=int(day)
#
# month_name=months[month_number-1]
# ordinal=day+endings[day_number-1]
#
# print month_name+' '+ordinal+'. '+year



#  分片 访问序列一定范围内的元素
numbers=[1,2,3,4,5,6,7,8,9,10]

#  第一个元素包含在分片内，第二个不包含在分片内
print numbers[3:6]

#  为了让分片部分能够包含列表的最后一个元素，必须提供最后一个元素的下一个元素所对应的索引作为边界
print numbers[7:10]

#  需要从列表的尾部开始计数呢
print numbers[-3:-1]   #得到的结果的是[8,9], 并不能以这种方式访问最后的元素。

print numbers[-3:0] # 得到的结果是[]。这并不是期望的结果。只要分片中最左边的索引比它右边的索引晚出现在序列中，结果就是一个空序列。

print numbers[-3:] # 包括序列结尾的元素正确写法

print numbers[:3] # 上述同样适用于序列的开始元素

print numbers[:] # 得到整个序列

# 步长(step length)
print numbers[0:10:1] # 步长是1

print numbers[0:10:2] # 步长是2

print numbers[3:6:3]  # 得到的是每三个元素的第一个元素

print numbers[::4] # 将每4个元素中的第1个提取出来

# 步长不能为0（那样不会向下执行） 但是步长可以为负数，即从右到左提取元素

print numbers[8:3:-1]

print numbers[10:0:-2]

print numbers[0:10:-2] # 返回为空[] 使用负数作为步长，需让开始索引大于结束索引

print numbers[::-2]

print numbers[5::-2]

print numbers[:5:-2]

# 序列相加

print [1,2,3]+[4,5,6]

print 'Hello, '+'world'

# print  [1,2,3]+'world' # 会报错， 列表和字符串是无法链接在一起的


# 序列乘法

# 用数字x乘以一个序列会生成一个新的序列，原来的序列将重复x次

print 'python'*5

print [42]*10

print [None]*10


# 成员资格

permissions = 'rw'

print 'w' in permissions
print  'x' in permissions

# users = ['mlh','foo','bar']
# print raw_input('Enter your name: ') in users

# 检查用户名和PIN码

# database = [['albert','1234'],['dilbert','4242'],['smith','7524'],['jones','9843']]
#
# username = raw_input('User name: ')
# pin = raw_input('PIN code: ')
#
# if [username,pin] in database : print 'Access granted'


# 长度 最大值 最小值
numbers = [100,34,678]
print len(numbers)

print max(numbers)

print min(numbers)

print max(2,3)

print min(9,3,2,5)


# 列表

# list函数

print list('Hello')

# 改变列表 元素赋值 不能为一个位置不存在的元素进行赋值
x = [1,1,1]
x[1] = 2
print x

# 删除元素

names = ['Alice','Beth','Cecil','Dee','Earl']
del names[3]
print names

# 分片赋值

name = list('Perl')
name[2:] = list('ar')

print name

# 分片赋值语句可以在不需要替换任何原有元素的情况下插入新的元素

numbers = [1,5]
numbers[1:1] = [2,3,4]
print numbers


# 通过分片赋值来删除元素

numbers = [1,2,3,4,5]
numbers[1:4] = []
print numbers

# 列表方法

# 方法是一个与某些对象有紧密联系的函数

# append 方法用于在列表末尾追加新的对象
# append方法不是简单的返回一个修改过的新列表，而是直接修改原来的列表

lst = [1,2,3]
lst.append(4)
print lst



# count方法统计某个元素在列表中出现的次数
print ['to','be','or','not','to','be'].count('be')

x = [[1,2],1,1,[2,1,[1,2]]]
print x.count(1)
print x.count([1,2])


# extend方法可以在列表的末尾一次性追加另一个序列中的多个值，即可以用新列表扩展原有的列表

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print a






