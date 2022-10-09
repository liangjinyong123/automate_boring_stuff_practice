# The List Data Type
print([1, 2, 3])
print(['cat', 'bat', 'rat', 'elephant'])
print(['heelo', 3.1415, True, None, 42])
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

## Getting Individual Values in a List with Indexes
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(['cat', 'bat', 'rat', 'elephant'][3])
print('Hello, ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

# spam[10000] # IndexError
# spam[1.0] # TypeError

print(spam[int(1.0)])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])

## Negative Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-3])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

## Getting a List from Another List with Slices
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])
print(spam[:])

## Getting a List's Length with the len() Function
spam = ['cat', 'dog', 'moose']
print(len(spam))

## Changing Values ina List with Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)

## List Concatenation and List Replication
print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

## Removing Values from Lists with del Statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)