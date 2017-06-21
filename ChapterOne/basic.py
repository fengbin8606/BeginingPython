# coding=utf-8

#print "hello world"

#print 10000L

#print repr("hello world")

#print repr(10000L)

print str("hello world")

print str(10000L)

temp=25

#错误的写法
#print "The temperature is "+temp

print "The temperature is "+`temp`

#str,repr和反引号是将Python值转换为字符串的3种方法。