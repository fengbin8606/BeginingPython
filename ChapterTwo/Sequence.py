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

months=['January','February','March','April','May','June','July','August','September','October','November','December']
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year=raw_input('Year: ')
month=raw_input('Month(1-12): ')
day=raw_input('Day(1-31): ')

month_number=int(month)
day_number=int(day)

month_name=months[month_number-1]
ordinal=day+endings[day_number-1]

print month_name+' '+ordinal+'. '+year
