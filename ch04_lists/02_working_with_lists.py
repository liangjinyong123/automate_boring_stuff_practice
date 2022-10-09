# Working with Lists
# catName1 = 'Zophie'
# catName2 = 'Pooka'
# catName3 = 'Simon'
# catName4 = 'Lady Macbeth'
# catName5 = 'Fat-tail'
# catName6 = 'Miss Cleo'

# print('Enter the name of cat 1: ')
# catName1 = input()
# print('Enter the name of cat 2: ')
# catName2 = input()
# print('Enter the name of cat 3: ')
# catName3 = input()
# print('Enter the name of cat 4: ')
# catName4 = input()
# print('Enter the name of cat 5: ')
# catName5 = input()
# print('Enter the name of cat 6: ')
# catName6 = input()
# print('The cat names are:')
# print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + catName5 + ' ' + catName6)

# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) \
#         + ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] # list concatenation

# print('The cat names are:')
# for name in catNames:
#     print('    ' + name)

## Using for Loops with Lists
# for i in range(4):
#     print(i)

# for i in [0, 1, 2, 3]:
#     print(i)

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

## The in and not in Operator
# print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
# spam = ['hello', 'hi', 'howdy', 'heyas']
# print('cat' in spam)
# print('howdy' not in spam)
# print('cat' not in spam)

# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')

## The Multiple Assignment Trick
# cat = ['fat', 'gray', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# size, color, disposition = cat
# size, color, disposition, name = cat # ValueError
# print(size, color, disposition)

## Using the enumerate() Function with Lists
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print('Index ' + str(index) + ' in supplies is: ' + item)

## Using the random.choice() and random.shuffle() Functions with Lists
# import random
# pets = ['Dog', 'Cat', 'Moose']
# print(random.choice(pets))
# print(random.choice(pets))
# print(random.choice(pets))

# people = ['Alice', 'Bob', 'Carol', 'David']
# random.shuffle(people)
# print(people)

#####################
# Augmented Assignment Operators
# spam = 42
# spam = spam + 1
# print(spam)

# spam = 42
# spam += 1
# print(spam)

# spam = 'Hello'
# spam += ' world!'
# print(spam)
# bacon = ['Zophie']
# bacon *= 3
# print(bacon)

#####################
# Methods
## Finding a Value in a List with the index() Method
# spam = ['hello', 'hi', 'howdy', 'heyas']
# print(spam.index('hello'))
# print(spam.index('heyas'))
# print(spam.index('howdy howdy howdy')) # ValueError

# spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
# Return the index of first appearance when there are duplicates
# print(spam.index('Pooka')) 

## Adding Values to Lists with the append() and insert() Methods
# spam = ['cat', 'dog', 'bat']
# spam.append('moose')
# print(spam)

# spam = ['cat', 'dog', 'bat']
# spam.insert(1, 'chicken')
# print(spam)

# eggs = 'hello'
# eggs.append('world') # AttributeError
# bacon = 42
# bacon.insert(1, 'world') # AttributeError

## Removing Values from Lists with the remove() Method
# spam = ['cat', 'dog', 'bat', 'elephant']
# spam.remove('bat')
# print(spam)

# spam = ['cat', 'dog', 'bat', 'elephant'] 
# spam.remove('chicken') # ValueError

# spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] 
# spam.remove('cat')
# print(spam)

## Sorting the Values in a List with the sort() Method
# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)

# spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
# spam.sort()
# print(spam)

# spam.sort(reverse=True)
# print(spam)

# spam = [1, 3, 2, 4, 'Alice', 'Bob']
# spam.sort() # TypeError

# spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
# spam.sort()
# print(spam)

# spam = ['a', 'z', 'A', 'Z']
# spam.sort(key=str.lower)
# print(spam)

## Reversing the Values in a List with the reverse() Method
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)