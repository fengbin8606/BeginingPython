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

print os.system()

os.system(r'c:\"Program Files (x86)"\"Notepad++"\notepad++.exe')

os.startfile(r'c:\"Program Files (x86)"\"Notepad++"\notepad++.exe')

import webbrowser
webbrowser.open('http://www.python.org')

