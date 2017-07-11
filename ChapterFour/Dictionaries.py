# coding=utf-8

# Creating and Using Dictionaries
# Dictionaries are written like this:
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# Keys are unique within a dictionary (and any other kind of mapping).

# The dict Function
# You can use the dict function1 to construct dictionaries from other mappings (for example,other dictionaries) or from sequences of (key, value) pairs:

items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print d
print d['name']
# It can also be used with keyword arguments, as follows:
d = dict(name='Gumby', age=42)
print d

# The basic behavior of a dictionary in many ways mirrors that of a sequence:
# • len(d) returns the number of items (key-value pairs) in d.
# • d[k] returns the value associated with the key k.
# • d[k] = v associates the value v with the key k.
# • del d[k] deletes the item with key k.
# • k in d checks whether there is an item in d that has the key k

# Key types: Dictionary keys don’t have to be integers (though they may be). They may be
# any immutable type, such as floating-point (real) numbers, strings, or tuples.

# Automatic addition: You can assign a value to a key, even if that key isn’t in the dictionary
# to begin with; in that case, a new item will be created.

# Membership: The expression k in d (where d is a dictionary) looks for a key, not a value.
# The expression v in l, on the other hand (where l is a list) looks for a value, not an index

# x = []
# x[42] = 'Foobar'

x = {}
x[42] = 'Foobar'
print x

# # A simple database
# # A dictionary with person names as keys. Each person is represented as
# # another dictionary with the keys 'phone' and 'addr' referring to their phone
# # number and address, respectively.
# people = {
# 'Alice': {
# 'phone': '2341',
# 'addr': 'Foo drive 23'
# },
# 'Beth': {
# 'phone': '9102',
# 'addr': 'Bar street 42'
# },
# 'Cecil': {
# 'phone': '3158',
# 'addr': 'Baz avenue 90'
# }
# }
# # Descriptive labels for the phone number and address. These will be used
# # when printing the output.
# labels = {
# 'phone': 'phone number',
# 'addr': 'address'
# }
# name = raw_input('Name: ')
# # Are we looking for a phone number or an address?
# request = raw_input('Phone number (p) or address (a)? ')
# # Use the correct key:
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
# # Only try to print information if the name is a valid key in
# # our dictionary:
# if name in people: print "%s's %s is %s." % \
#                          (name, labels[key], people[name][key])


# String Formatting with Dictionaries
print "Cecil's phone number is %(Cecil)s." % phonebook

template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print template % data

# Dictionary Methods
# clear
# The clear method removes all items from the dictionary. This is an in-place operation (like
# list.sort), so it returns nothing (or, rather, None):
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print d
returned_value = d.clear()
print d
print returned_value


# Two scenarios.
# Here’s the first one:
x = {}
y = x
x['key'] = 'value'
print y
x = {}
print y

# And here’s the second scenario:
x = {}
y = x
x['key'] = 'value'
print y
x.clear()
print y
# In both scenarios, x and y originally refer to the same dictionary. In the first scenario, I
# “blank out” x by assigning a new, empty dictionary to it. That doesn’t affect y at all, which still
# refers to the original dictionary. This may be the behavior you want, but if you really want to
# remove all the elements of the original dictionary, you must use clear. As you can see in the
# second scenario, y is then also empty afterward.

# copy
# The copy method returns a new dictionary with the same key-value pairs (a shallow copy, since
# the values themselves are the same, not copies):
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print y
print x

# As you can see, when you replace a value in the copy, the original is unaffected. However,
# if you modify a value (in place, without replacing it), the original is changed as well because the
# same value is stored there (like the 'machines' list in this example).
# One way to avoid that problem is to make a deep copy, copying the values, any values they
# contain, and so forth as well. You accomplish this using the function deepcopy from the copy
# module:
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c   # 浅复制收到append方法的影响
#{'names': ['Alfred', 'Bertrand', 'Clive']}
print dc  # 深度复制没有受append方法的影响
# {'names': ['Alfred', 'Bertrand']}

# fromkeys
# The fromkeys method creates a new dictionary with the given keys, each with a default corresponding value of None:
print {}.fromkeys(['name', 'age'])
# {'age': None, 'name': None}


# This example first constructs an empty dictionary and then calls the fromkeys method on
# that, in order to create another dictionary—a somewhat redundant strategy. Instead, you can
# call the method directly on dict, which (as mentioned before) is the type of all dictionaries.
print dict.fromkeys(['name', 'age'])
# {'age': None, 'name': None}
# If you don’t want to use None as the default value, you can supply your own default:
print dict.fromkeys(['name', 'age'], '(unknown)')
# {'age': '(unknown)', 'name': '(unknown)'}

# get
# The get method is a forgiving way of accessing dictionary items. Ordinarily, when you try to
# access an item that is not present in the dictionary, things go very wrong:
d = {}
print d['name']
print d.get('name')
# None
# As you can see, when you use get to access a nonexistent key, there is no exception.
# Instead, you get the value None. You may supply your own “default” value, which is then used
# instead of None:
print d.get('name', 'N/A')
