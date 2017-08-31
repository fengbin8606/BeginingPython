#coding=utf-8


fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print fibs

def hello(name):
    return 'Hello,'+name+'!'

print hello('Kimi')

def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

def square(x):
    'Calculates the square of the number x.'
    return x*x

print square.__doc__

# Functions that don’t return anything simply don’t
# have a return statement. Or, if they do have return statements, there is no value after the word
# return:
def test():
    print 'This is printed'
    return
    print 'This is not'

x=test()

# That’s a familiar value: None. So all functions do return something; it’s just that they return
# None when you don’t tell them what to return. I guess I was a bit unfair when I said that some
# functions aren’t really functions
print x

def change(n):
    n[0] = 'Mr. Gumby'

names = ['Mrs. Entity', 'Mrs. Thing']
print names[:]
change(names[:])
print names

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage={}
init(storage)
print storage

me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]

def lookup(data, label, name):
    return data[label].get(name)

print lookup(storage, 'middle', 'Lie')

# Consider the following two functions:
def hello_1(greeting, name):
    print '%s, %s!' % (greeting, name)
def hello_2(name, greeting):
    print '%s, %s!' % (name, greeting)

# They both do exactly the same thing, only with their parameter names reversed:
hello_1('Hello', 'world')
# Hello, world!
hello_2('Hello', 'world')
# Hello, world!

# Sometimes (especially if you have many parameters) the order may be hard to remember.
# To make things easier, you can supply the name of your parameter:
hello_1(greeting='Hello', name='world')
# Hello, world!
# The order here doesn’t matter at all:
hello_1(name='world', greeting='Hello')
# Hello, world!
# The names do, however (as you may have gathered):
hello_2(greeting='Hello', name='world')
# world, Hello!

# The parameters that are supplied with a name like this are called keyword parameters. On
# their own, the key strength of keyword parameters is that they can help clarify the role of each
# parameter. Instead of needing to use some odd and mysterious call like this:
#    store('Mr. Brainsample', 10, 20, 13, 5)
# you could use this:
#    store(patient='Mr. Brainsample', hour=10, minute=20, day=13, month=5)

# Even though it takes a bit more typing, it is absolutely clear what each parameter does.
# Also, if you get the order mixed up, it doesn’t matter.
# What really makes keyword arguments rock, however, is that you can give the parameters
# in the function default values:
def hello_3(greeting='Hello', name='world'):
    print '%s, %s!' % (greeting, name)

# When a parameter has a default value like this, you don’t need to supply it when you call
# the function! You can supply none, some, or all, as the situation might dictate:
hello_3()
# Hello, world!
hello_3('Greetings')
# Greetings, world!
hello_3('Greetings', 'universe')
# Greetings, universe!

# You can combine positional and keyword parameters.
# The only requirement is that all the positional parameters come first. If they don’t,
# the interpreter won’t know which ones they are (that is, which position they are supposed to have).

# For example, our hello function might require a name, but allow us to (optionally) specify
# the greeting and the punctuation:

def hello_4(name, greeting='Hello', punctuation='!'):
    print '%s, %s%s' % (greeting, name, punctuation)

# This function can be called in many ways. Here are some of them:
hello_4('Mars')
# Hello, Mars!
hello_4('Mars', 'Howdy')
# Howdy, Mars!
hello_4('Mars', 'Howdy', '...')
# Howdy, Mars...
hello_4('Mars', punctuation='.')
# Hello, Mars.
hello_4('Mars', greeting='Top of the morning to ya')
# Top of the morning to ya, Mars!
# hello_4()
# Traceback (most recent call last):
# File "<pyshell#64>", line 1, in ?
# hello_4()
# TypeError: hello_4() takes at least 1 argument (0 given)


def print_params(*params):
    print params

print_params('Testing')
# ('Testing',)

# You can see that what is printed out is a tuple because it has a comma in it.

print_params(1, 2, 3)
# (1, 2, 3)


def print_params_4(x, y, z=3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar

print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
print_params_4(1, 2)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None: # If the stop is not supplied...
        start, stop = 0, start # shuffle the parameters
    print stop
    result = []
    i = start  # We start counting at the start index
    while i < stop:  # Until the index reaches the stop index...
        result.append(i)  # ...append the index to the result...
        i += step  # ...increment the index with the step (> 0)
    return result

print interval(10)

a,b=0,3
print a
print b

def combine(parameter):
    print parameter + globals()['parameter']

parameter = 'berry'
combine('Shrub')
# Shrubberry

# def recursion():
#     return recursion()
# recursion()

import sys
print sys.argv
