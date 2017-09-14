#coding=utf-8

# import sys
# sys.path.append('D:/python')

# import hello

# import hello

# hello=reload(hello)

__name__

import sys,pprint
pprint.pprint(sys.path)

import ChapterSix
print ChapterSix.PI

name='feng'
import ChapterSix.Abstraction
print ChapterSix.Abstraction.hello(name)

from ChapterSix import Abstraction
print Abstraction.hello(name)

import copy
print dir(copy)

print [n for n in dir(copy) if not n.startswith('_')]

print copy.copy.__doc__

print copy.__file__

print sys.argv

print sys.modules

print sys.platform

import os
print os.environ['PYTHONPATH']

# print os.system()

# os.system(r'c:\"Program Files (x86)"\"Notepad++"\notepad++.exe')

# os.startfile(r'c:\"Program Files (x86)"\"Notepad++"\notepad++.exe')

import webbrowser
# webbrowser.open('http://www.python.org')

print set(range(10))

a = set([1, 2, 3])
b = set([2, 3, 4])
print a.union(b)
print a | b
c=a&b
print c.issubset(a)
print a.difference(b)


print a.add(frozenset(b))
print a

from heapq import *
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print heap
# [0, 1, 3, 6, 2, 8, 4, 7, 9, 5]
heappush(heap, 0.5)
print heap
# [0, 0.5, 3, 6, 1, 8, 4, 7, 9, 5, 2]
print heapreplace(heap,10)

# for n in range(10):
#     print heappop(heap)

list=[6,1,2,4,3,7,9]
heapify(list)
print "list: "
print list

print nlargest(1,list)
print nlargest(2,heap)
print nsmallest(2,heap)

from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print q
# deque([6, 0, 1, 2, 3, 4, 5])
print q.pop()
# 5
print q.popleft()
# 6
q.rotate(3)
print q
# deque([2, 3, 4, 0, 1])
q.rotate(-1)
print q
# deque([3, 4, 0, 1, 2])

import time
print time.asctime()
time.sleep(1)
print time.localtime()
print time.strptime(time.asctime())
print time.time()

from random import *
print random()

