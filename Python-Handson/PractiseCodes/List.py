a = [1,2,3,4,5]

a.append(6)
a.append(7)
a.append(7)
print(a)

# Appending a list to a list
b = [8,9,10]
a.append(b)
print(a)

# Lists are heterogenous
a.append('Hello')
print(a)

# Lists can be extended
a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)
print(a)

#Pop removes the last element
a.pop()
print(a)

a.pop(3) # removes the element at index 3
print(a)

print(a.count(7)) # returns the number of times 7 appears in the list

a.sort(reverse=True) # sorts the list in descending order
print(a)

# Sorting the dictionary by value
l = {'a': 10, 'b': 20, 'c': 5, 'd': 15}
print(l)

print(sorted(l.items(), key=lambda x: x[1]))

# Using itemgetter
people = [{'name':'chandan','age':20,'salary':2000},
{'name':'chetan','age':18,'salary':5000},
{'name':'guru','age':30,'salary':3000}]
print(people)

from operator import itemgetter
by_age = itemgetter('age')
by_salary = itemgetter('salary') 

people.sort(key=by_age) #in-place sorting by age
print(people)

people.sort(key=by_salary) #in-place sorting by salary
print(people)

a = [1,2,3,4,5]
print(a)

b = a # b is a reference to a
print(b)

a.append(6)
print(a)
print(b)

b.append(7)
print(a)
print(b)

print(id(a))
print(id(b))

# Way to really copy a list
a = [1,2,3,4,5]
b = a[:]
print(a)
print(b)
a.append(6)
b.append(7)
print(a)
print(b)
print(id(a))
print(id(b))

# Checking if a list is empty
a = []
if not a:
    print('List is empty')

# Iterating over a list
a = [1,2,3,4,5]
for i in a:
    print(i)

# Iterating over a list using enumerate()
for index, value in enumerate(a):
    print(index, value) 

alist = [1,2,3,4,5]
blist = [6,7,8,9,10]

for a, b in zip(alist, blist):
    print(a,b)

# Iterating over a list using zip() 
# It will display only till the matching index
alist = [1,2,3,4,5]
blist = [6,7,8,9]

for a, b in zip(alist, blist):
    print(a,b)

print([1, 10] > [0, 10, 100]) # returns True
print([1, 10] < [1, 10, 100]) # returns True

# List Comprehension
a = [1,2,3,4,5]
square = [x**2 for x in a]
print(square)

for x in range(6,11):
    square.append(x**2)
print(square)

# Strip off any commas from the end of strings in a list
op =  [w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
print(op)
# ['these', 'words', 'mostly', 'have,commas']

# Organize letters in words more reasonably - in an alphabetical order
sentence = "Beautiful is better than ugly"
x1 = [x.lower() for x in sentence.split()]
print(x1)


print([x.sort() for x in [[2, 1], [4, 3], [0, 1]]])
# returns None as sort() returns None

print([sorted(x) for x in [[2, 1], [4, 3], [0, 1]]])
# returns [[1, 2], [3, 4], [0, 1]]
