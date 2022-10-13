# The Dictionary Data Type
# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# print(myCat['size'])

# spam = {12345: 'Luggage Combination', 42: 'The Answer'}

## Dictionaries vs. Lists
# spam = ['cat', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cat']
# print(spam == bacon)

# eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
# ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
# print(eggs == ham)

# spam = {'name': 'Zophie', 'age': 7}
# print(spam['color']) # KeyError

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit) ')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

## The keys(), values(), and items() Methods
# spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#     print(v)

# for k in spam.keys():
#     print(k)

# for i in spam.items():
#     print(i)

# spam = {'color': 'red', 'age': 42}
# print(spam.keys())
# print(list(spam.keys()))

# for k, v in spam.items():
#     print('Key: ' + k + ' Value: ' + str(v))

## Checking Whether a Key or Vlue Exists in a Dictionary
# spam = {'name': 'Zophie', 'age': 7}
# print('name' in spam.keys())
# print('Zophie' in spam.values())
# print('color' in spam.keys())
# print('color' not in spam.keys())
# print('color' in spam) # Same as 'color' in spam.keys()

## The get() Method
# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# print('I am bringing ' + str(picnicItems['eggs']) + ' eggs.') # KeyError

## The setdefault() Method
# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'

# print(spam)

# spam = {'name': 'Pooka', 'age': 5}
# spam.setdefault('color', 'black')
# print(spam)
# spam.setdefault('color', 'white')
# print(spam)

# Count the number of occurrences of each letter in a string.
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# print(count)

# Pretty Printing
# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# pprint.pprint(count)
# print(pprint.pformat(count))