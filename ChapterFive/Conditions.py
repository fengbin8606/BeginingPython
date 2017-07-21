#coding=utf-8

#The following values are considered by the interpreter to mean false when evaluated as a
# Boolean expression (for example, as the condition of an if statement):
#    False     None    0    ""    ()      []      {}

# In other words, the standard values False and None, numeric zero of all types (including
# float, long, and so on), empty sequences (such as empty strings, tuples, and lists), and empty
# dictionaries are all considered to be false. Everything else3 is interpreted as true, including the
# special value True.4

print True
# True
print False
# False
print True == 1
# True
print False == 0
# True
print True + False + 42
# 43

# The Boolean values True and False belong to the type bool, which can be used (just like, for
# example, list, str, and tuple) to convert other values:
print bool('I think, therefore I am')
# True
print bool(42)
# True
print bool('')
# False
print bool(0)
# False

# Although [] and "" are both false (that is, bool([])==bool("")==False), they are not equal (that
# is, []!=""). The same goes for other false objects of different types (for example, ()!=False)

# If you want to check for several conditions, you can use elif, which is short for “else if.” It is a
# combination of an if clause and an else clause—an else clause with a condition:
# num = input('Enter a number: ')
# if num > 0:
#     print 'The number is positive'
# elif num < 0:
#     print 'The number is negative'
# else:
#     print 'The number is zero'


# Nesting Blocks
# Let’s throw in a few bells and whistles. You can have if statements inside other if statement
# blocks, as follows:
# name = raw_input('What is your name? ')
# if name.endswith('Gumby'):
#     if name.startswith('Mr.'):
#         print 'Hello, Mr. Gumby'
#     elif name.startswith('Mrs.'):
#         print 'Hello, Mrs. Gumby'
#     else:
#         print 'Hello, Gumby'
# else:
#     print 'Hello, stranger'

# is: The Identity Operator
# The is operator is interesting. It seems to work just like ==, but it doesn’t:
x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
# True
print x == z
# True
print x is y
# True
print x is z
# False

# Until the last example, this looks fine, but then you get that strange result: x is not z, even
# though they are equal. Why? Because is tests for identity, rather than equality. The variables x
# and y have been bound to the same list, while z is simply bound to another list that happens to
# contain the same values in the same order. They may be equal, but they aren’t the same object.

# To summarize: use == to see if two objects are equal, and use is to see if they are identical
# (the same object).

print [2, [1, 4]] < [2, [1, 5]]
# True


# while Loops
x = 1
while x <= 100:
    print x
    x += 1

# name = ''
# while not name:
#     name = raw_input('Please enter your name: ')
# print 'Hello, %s!' % name
#
# name = ''
# while not name.strip():
#     name = raw_input('Please enter your name: ')
# print 'Hello, %s!' % name


# for Loops
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print word

d = {'x': 1, 'y': 2, 'z': 3}
for key in d.keys():
    print key, 'corresponds to', d[key]

# You may remember that
# d.items returns key-value pairs as tuples. One great thing about for loops is that you can use
# sequence unpacking in them:

for key, value in d.items():
   print key, 'corresponds to', value

# Parallel Iteration
# Sometimes you want to iterate over two sequences at the same time.
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'

# A useful tool for parallel iteration is the built-in function zip, which “zips” together the
# sequences, returning a list of tuples:
# The zip function works with as many sequences as you want. It’s important to note what
# zip does when the sequences are of different lengths: it stops when the shortest sequence is
# used up:
for name, age in zip(names, ages):
    print name, 'is', age, 'years old'

# List Comprehension—Slightly Loopy
# List comprehension is a way of making lists from other lists (similar to set comprehension, if
# you know that term from mathematics). It works in a way similar to for loops and is actually
# quite simple:

print [x*x for x in range(10)]
print [x*x for x in range(10) if x % 3 == 0]

print [(x, y) for x in range(3) for y in range(3)]
# As a comparison, the following two for loops build the same list:
result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print result

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
# ['chris+clarice', 'arnold+alice', 'bob+bernice']

# A BETTER SOLUTION
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
    print letterGirls
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]

# pass statement
# Now, why on earth would you want a statement that does nothing? It can be useful as a
# placeholder while you are writing code. For example, you may have written an if statement
# and you want to try it, but you lack the code for one of your blocks. Consider the following:
if name == 'Ralph Auldus Melish':
    print 'Welcome!'
elif name == 'Enid':
    # Not finished yet...
    pass  # This code won’t run because an empty block is illegal in Python.
elif name == 'Bill Gates':
    print 'Access Denied'

# del statement
x = 1
del x
# print x

# This may seem easy, but it can actually be a bit tricky to understand at times. For instance,
# in the following example, x and y refer to the same list:
x = ["Hello", "world"]
y = x
y[1] = "Python"
print x
# ['Hello', 'Python']
# You might assume that by deleting x, you would also delete y, but that is not the case:
del x
y
# ['Hello', 'Python']
# Why is this? x and y referred to the same list, but deleting x didn’t affect y at all. The reason
# for this is that you delete only the name, not the list itself (the value). In fact, there is no way to
# delete values in Python—and you don’t really need to, because the Python interpreter does it
# by itself whenever you don’t use the value anymore.


# You do this by adding in <scope>, where <scope> is some dictionary that will function as
# the namespace for your code string:

# from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
# print sqrt(4)
# 2.0
print scope['sqrt']
# 1
print len(scope)
print scope

# eval
# A built-in function that is similar to exec is eval (for “evaluate”). Just as exec executes a series
# of Python statements, eval evaluates a Python expression (written in a string) and returns the
# resulting value. (exec doesn’t return anything because it is a statement itself.) For example, you
# can use the following to make a Python calculator:
print eval(raw_input("Enter an arithmetic expression: "))
# Enter an arithmetic expression: 6 + 18 * 2
# 42

