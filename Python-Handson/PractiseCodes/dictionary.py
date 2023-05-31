d = {}
d = {'a' : 10}
print(d)

# Dictionary comprehension
new_d = {k:v for k,v in d.items()}
print(new_d)

# Dictionary comprehension with range
new_d = {k:v for k,v in enumerate(range(10,21))}
print(new_d)


d = dict() # empty dict
d = dict(key='value') # explicit keyword arguments
d = dict([('key', 'value')]) # passing in a list of key/value pairs


d['new_list'] = [1,2,3,4,5]
d['new_dict'] = {'nested_dic': 1}
print(d)

# Avoiding KeyError 
#print(d['not found']) # KeyError
print(d.get('new_list', 'not found'))

print(d.get('new_dict'))

print(d.get('not found')) # returns None
print(d.get('not found', 'No Value')) # returns 'No Value' as default value

# Iterating over a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])

# Iterating over a dictionary using items()
for key, value in d.items():
    print(key, value)

# Iterating over a dictionary using enumerate()
for index, key in enumerate(d):
    print(index, key, d[key])

# Iterating over a dictionary using zip()
for key, value in zip(d.keys(), d.values()):
    print(key, value)

# Dictionary with default values
from collections import defaultdict
d = defaultdict(int)
print(d['key']) # returns 0
d['key'] = 10
print(d['key']) # returns 10

# Merging dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {**d1, **d2}
print(d3)

# Creating a dictionary from two lists
mydict = {'a' : [1,2,3], 'b': ['one', 'two', 'three']}
print(mydict)

mydict['a'].append(4)
print(mydict)

mydict['b'].append('four')
print(mydict)

# Creating a dictionary from tuples
iterable = [('a', 1), ('b', 2), ('c', 3)]
mydict = dict(iterable)
print(mydict)

# Swapping keys and values
my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(my_dict)
swapped = {value: key for key, value in my_dict.items()}
print(swapped)

swapped = dict(zip(my_dict.values(), my_dict.keys()))
print(swapped)

swapped = dict(map(reversed, my_dict.items()))
print(swapped)