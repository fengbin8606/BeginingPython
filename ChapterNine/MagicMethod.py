#coding=utf-8

# __metaclass__ =type
class FooBar:
    def __init__(self):
        self.somevar = 42

f=FooBar()
print f.somevar


class A:
    def hello(self):
        print "Hello, I'm A."
class B(A):
    pass

a = A()
b = B()
a.hello()
# Hello, I'm A.
b.hello()
# Hello, I'm A./

class B(A):
    def hello(self):
        print "Hello, I'm B."

b = B()
b.hello()
# Hello, I'm B.

__metaclass__ = type # super only works with new-style classes
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No, thanks!'

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
        
sb = SongBird()
sb.sing()
# Squawk!
sb.eat()
# Aaaah...
sb.eat()
# No, thanks!


def checkIndex(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integer. If it
    is not an integer, a TypeError is raised; if it is negative, an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key, (int, long)): raise TypeError
    if key<0: raise IndexError
class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.
        start - the first value in the sequence
        step - the difference between two adjacent values
        changed - a dictionary of values that have been modified by
        the user
        """
        self.start = start # Store the start value
        self.step = step # Store the step value
        self.changed = {} # No items have been modified
    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        """
        checkIndex(key)
        try: return self.changed[key] # Modified?
        except KeyError: # otherwise...
            return self.start + key*self.step # ...calculate the value

    def __setitem__(self, key, value):
        """
        Change an item in the arithmetic sequence.
        """

        checkIndex(key)
        self.changed[key] = value  # Store the changed value

s = ArithmeticSequence(1, 2)
print s[4]
print s[5]
# print s[-5]

# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def setSize(self, size):
#         self.width, self.height = size
#     def getSize(self):
#         return self.width, self.height
#
# r = Rectangle()
# r.width = 10
# r.height = 5
# print r.getSize()
# # (10, 5)
# r.setSize((150, 100))
# print r.width
# print r.height
# # 15\

__metaclass__ = type
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

r = Rectangle()
r.width = 10
r.height = 115
print r.size
# (10, 5)
r.size = 1150, 10000
print r.width


it = iter([1, 2, 3])
# print it.next
print it.next()
print it.next()


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs=Fibs()
for f in fibs:
    if f>100:
        print f
        break

class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
print list(ti)

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1, 2], [3, 4], [5]]
print list(flatten(nested))
for num in flatten(nested):
    print num

g = ((i+2)**2 for i in range(2,27))
print g.next()

print sum(i**2 for i in range(10))
print 2**6

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                 yield element
    except TypeError:
        yield nested

print list(flatten([[[1],2],3,4,[5,[6,7]],8]))

def flatten(nested):
    try:
        # Don't iterate over string-like objects:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

print list(flatten(['foo', ['bar', ['baz']]]))

def simple_generator():
    yield 1

print simple_generator
print simple_generator()


def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(42)
print r.next()
print r.send('Hello')
