# coding=utf-8
#元组与列表一样，也是一种序列。元组不能修改。
#创建元组，用逗号分隔了一些值，就自动创建了元组
print 1,2,3

print (1,2,3)  #大部分时候元组是用括号括起来的

print ()	   #空元组的表示方法

print 44,      #实现一个值的元组也需要加逗号

#注意下面两个表达式的区别
print 3*(40+2)
print 3*(40+2,)

#tuple函数 （tuple并不是真正的函数而，是一种类型）
#tuple函数的功能与list函数基本上一样，以一个序列作为参数并把它转换为元组。
#如果参数是元组，那么该参数就会被原样返回
print tuple([1,2,3]) #参数是序列
print tuple('abc')   #参数是序列
print tuple((1,2,3)) #参数是元组

#基本元组操作 创建和访问
x=(1,2,3)
print x[1]
print x[0:2]  #元组的分片还是元组 列表的分片还是列表

#元组的意义
#元组可以在映射中当作键值使用
#元组作为很多内建函数和方法的返回值存在，必须对元组进行处理

