__metaclass__ = type # Make sure we get new style classes
class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello, world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
 # Hello, world! I'm Luke Skywalker.
bar.greet()
 # Hello, world! I'm Anakin Skywalker.


class Secretive:
    def __inaccessible(self):
        print "Bet you can't see me..."
    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()

# s=Secretive
s=Secretive()
s.accessible()

s._Secretive__inaccessible()

class C:
    print "Class C is defined..."

class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked=['SPAM']

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])

print SPAMFilter.__bases__
print Filter.__bases__
print isinstance(s,Filter)
print isinstance(s,SPAMFilter)
print s.__class__


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print 'Hi, my value is', self.value

class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
# Hi, my value is 7

print hasattr(tc, 'talk')
# True
print hasattr(tc, 'fnord')
# False

print callable(getattr(tc, 'talk', None))