#coding=utf-8

# raise Exception

# raise Exception('hyperdrive overload')

import exceptions
print dir(exceptions)

# raise ArithmeticError

class SomeCustomException(Exception): pass

# x = input('Enter the first number: ')
# y = input('Enter the second number: ')
# print x/y
#
# try:
#     x = input('Enter the first number: ')
#     y = input('Enter the second number: ')
#     print x/y
# except ZeroDivisionError:
#     print "The second number can't be zero!"

class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise

calculator = MuffledCalculator()
print calculator.calc('10/3')
# print calculator.calc('10/0')
calculator.muffled=True
# print calculator.calc('10/0')

# try:
#     x = input('Enter the first number: ')
#     y = input('Enter the second number: ')
#     print x/y
# except (ZeroDivisionError, TypeError, NameError):
#     print 'Your numbers were bogus...'

# try:
#     x = input('Enter the first number: ')
#     y = input('Enter the second number: ')
#     print x/y
# except (ZeroDivisionError, TypeError, NameError),e:
#     print e

# try:
#     x = input('Enter the first number: ')
#     y = input('Enter the second number: ')
#     print x/y
# except Exception,e:
#     print e

# while True:
#     try:
#         x = input('Enter the first number: ')
#         y = input('Enter the second number: ')
#         value = x/y
#         print 'x/y is', value
#     except:
#         print 'Invalid input. Please try again.'
#     else:
#         break

# while True:
#     try:
#         x = input('Enter the first number: ')
#         y = input('Enter the second number: ')
#         value = x/y
#         print 'x/y is', value
#     except Exception, e:
#         print 'Invalid input:', e
#         print 'Please try again'
#     else:
#         break


# try:
#     1/0
# except :
#     print "Unknown variable"
# else:
#     print "That went well!"
# finally:
#     print "Cleaning up."


def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print 'Exception Handle'

# handle_exception()
ignore_exception()