

# ! lect_01_list
# ['a','a','c']
# ordered collection items
# changeable
# allow duplicate


# !* create list
# empty = []
# letters = ['a', 'b', 'c']
# numbers = [1, 2, 3, 4]
# mixed = [1, 2, 'a', 'b', True, None]


# print(empty)
# print(type(empty))

# print(letters)
# print(type(letters))

# print(numbers)
# print(type(numbers))

# print(mixed)
# print(type(mixed))


# *--------------------

# empty = list()
# print(empty)

# letters = 'Python'
# print(letters)

# letters_word = list("Python")
# print(letters_word)


# numbers = list(range(0, 5))
# print(numbers)


# * ----------------------- nested List (Matrix) -------------------


# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f']
# ]

# print(matrix)
# print(type(matrix))

# * ----------------------- (Access & Read) -------------------

# lst = ['a', 'b', 'c', 'd']
# print(lst)
# print(lst[0])
# print(lst[-1])
# print(lst[2])


# todo matrix nested list
# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i'],
# ]
# print(matrix)
# print(matrix[2][2])
# print(matrix[-1][-1])
# print(matrix[1][1])

# todo slicing
import copy
lst = ['a', 'b', 'c', 'd']

# print(lst[:2])
# print(lst[2:])
# print(lst[:])

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
]

# print(matrix[:2])
# print(matrix[1:])
# print(matrix[2][:2])
# print(matrix[1][1:])
# print(matrix[::][1:2])


# ? Packing vs Unpacking

# * Packing --> means storing multiple items inside a container.

# * Unpacking --> means taking items out of a container into separate variables.

# Packing
data = 1, 2, 3
# print(data)   # (1, 2, 3)

# Unpacking
a, b, c = data
# print(a)
# print(b)
# print(c)


person = ["Maria", 33, 'Data Science', 'Pakistan']  # --> order of values
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

name, age, role, country = person  # --> order of variable

# print(name)
# print(country)

# * asterisk (*) unpacking

# todo Example 1: Middle values collect
name, *detail, country = person
# print(name)
# print(detail)
# print(country)


# todo Example 2: last values collect
name, *rest = person
# print(name)
# print(rest)

# todo Example 3: first values collect
*detail, country = person
# print(detail)
# print(country)

# todo Example 4: One value + rest ignore style --> _ means ignore middle values
name, *_, country = person
# print(name)
# print(country)

# todo Example 5: Strings unpacking
word = ["P", "y", "t", "h", "o", "n"]

# first, *middle, last = word

# print(first)   # P
# print(middle)   # ['y', 't', 'h', 'o']
# print(last)     # n

# * ---------pratice-------------
# a = 10
# b = 20

# a, b = b, a

# print(a)
# print(b)

x, y, z = 10, "Ali", 99.5

x, y, z = z, x, y

# print(x)
# print(y)
# print(z)


# ! Unpacking rule
# number = [1, 2, 3, 4]

# todo : Rule 1: Same number of variables required
# first, second, last = number
# print(first)


# todo : Rule 2: Order matters
data = ['Bilal', 21, 'Data Engineering']
name, age, field = data
# print(name)
# print(field)


# todo :Rule 3: * (asterisk) extra values handle karta hai

a, *b, c = [1, 2, 3, 4, 5]
# print(a)
# print(b)
# print(c)

# todo : Rule 4: Only one * allowed

# a, *b, *c = [1, 2, 3] # error

# todo : Rule 5: _ is used to ignore values

a, _, c = [10, 20, 30]
# print(a)
# print(c)


# ! explore & analyze list

numbers = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
# print("Max: ", max(numbers))
# print("Min: ", min(numbers))
# print("Sum: ", sum(numbers))
# print("Length: ", len(numbers))

# * all() -> Returns True only if ALL values are True
# print("All: ", all(numbers))  # all number true

# print("All: ", all([1, 0, 2]))  # 0,'',False,None -->False
# print("All: ", all(['a', '', 'c']))  # 0,'',False,None -->False


# * any() -> Returns True if AT LEAST ONE value is True
# print("Any", any(numbers))
# print("Any", any([1, 0, 2]))
# print("Any", any(['a', '', 'c']))
# print("Any", any([0, 0, 0]))


# print("Count: ", numbers.count(2))

# *index()-> Index means position of an item in a list (or string).
# print("Index: ",numbers.index(2))


# ! Analysis & check

list1 = [1, 2, 2, 4, 5]

list2 = [1, 2, 2, 4, 5]

# print(1 in list1)
# print(14 not in list1)

# print(list1 == list2)
# print(list1 < list2) #first eement compare
# print(list1 is list2)


# todo: append() --> add value at the end
list_1 = ['a', 'b', 'c']
list_1.append('x')
list_1.append('y')
# print(list_1)


# todo: insert() --> insert value at a specific position

list_1.insert(1, 'd')
list_1.insert(2, 'men')
# print(list_1)


# ? adding
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix[1].append('x')
matrix[0].insert(2, 'x')
matrix.append(['x', 'y', 'z'])
matrix.append('x')
matrix.insert(1, ['a', 'a', 'a'])
# print(matrix)

# todo: remove() --> remove first matching value (number, string, etc.)
# print(list_1)
list_1.remove('men')
list_1.append(2)
list_1.append(2)
list_1.remove(2)
list_1.remove(2)
# print(list_1)

# todo: clear() --> remove all items from list
list_1.clear()
# print(list_1)

# todo: pop() --> remove and return value from a specific position


list_1 = ['a', 'b', 'c', 'd']

list_1.pop()  # removes last element
# print(list_1)


removed = list_1.pop()
# print("Removed: ", removed)


# list_1.pop(1)  # remove element at index
removed = list_1.pop(1)
# print("Removed: ", removed)
# print(list_1)


# ? matrix
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
# matrix.remove(['a','b','c'])
# matrix.pop()

# matrix[1].remove('e')
matrix[-1].pop(0)
matrix[1].pop()
# print(matrix)

# todo: update() --> update or add key-value pairs in dictionary
letters = ['a', 'b', 'c', 'd']

letters[0] = "x"
letters[2] = "y"
letters = 'z'
# print(letters)
# print(type(letters))


matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix[-1] = ['x', 'y', 'x']
matrix[0][0] = '-'
matrix[1][1] = '-'
matrix[-1][-1] = '-'
# print(matrix)


# todo: sort() --> arrange list in ascending or descending order

letters = ['c', 'a', 'b']

# letters.sort(reverse=True)  # descending order
# letters.sort()  # ascending order (default)
# print(letters)


# todo: sorted() --> returns a new sorted list (original list remains same)
new_list = sorted(letters)

# print("Original List:", letters)
# print("Sorted List:", new_list)


# * reverse sorting example with sorted()
desc_list = sorted(letters, reverse=True)
# print("Descending Sorted List:", desc_list)

# todo: sorting in 2D list (matrix)

matrix = [
    ['g', 'i', 'h'],
    ['a', 'a', 'f'],
    ['a', 'b', 'c']
]

# todo: sort() on matrix --> sorts rows based on first element of each row
matrix.sort()
# print("Sorted Matrix (rows):", matrix)


# sorting inside a row (list inside list)
matrix[0].sort()
# print("After sorting first row:", matrix)


# letters.reverse()


# reverse() --> list method
# it reverses the list in-place (original list is changed permanently)
# it does NOT return a new list
# letters.reverse()


# todo: reversed() --> built-in function
# it does NOT change the original list
# it returns an iterator (not a list), so we must convert it using list()

letters = ['c', 'a', 'b']
new_reverse = list(reversed(letters))
# print("Origional List: ", letters)
# print("Reversed List: ", new_reverse)


# todo: copy -> # reference assignment using =
# letters = ['c', 'a', 'b']
# letters.append('z')
# letters.sort()
# letters.pop(-1)
# letters.pop()
# letters_copy = letters
# print("Origional List: ", letters)
# print("Copy List: ", letters_copy)


# todo: copy() creates a shallow copy of the list.
# todo: The outer list becomes separate in memory,
# todo: but nested objects are still shared between both lists.


letters = ['c', 'a', 'b']
# letters.append('z')
# letters.sort()
# letters.pop(-1)
# letters.pop()
letters_copy = letters.copy()
letters_copy.append('z')
letters_copy.sort()
letters_copy.pop(-1)
# print("Origional List: ", letters)
# print("Copy List: ", letters_copy)


# matrix

# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
# ]

# matrix_cpy = matrix.copy()
# matrix.pop()
# matrix_cpy[0].append('z')
# print("Origional List: ", matrix)
# print("Copy List: ", matrix_cpy)


# ! import copy
# * copy.deepcopy() create a true,indepent copy for all levels
# * copy.copy() create a SHALLOW copy like just the method copy(),is more general than list.copy() ,not limited lists
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
]

# matrix_cpy = copy.deepcopy(matrix)
matrix_cpy = copy.copy(matrix)
matrix.pop()
matrix_cpy[0].append('z')
# print("Origional List: ", matrix)
# print("Copy List: ", matrix_cpy)


# ! Assignment

origional = [
    ['a', 'b'],
    ['c', 'd'],
]


copy1 = origional
# print("Same object?", origional is copy1, "\n")


# shallow copy
copy2 = origional.copy()
# print("Same object?", origional is copy2)
# print("Shared List?", origional[0] is copy2[0], "\n")


# deep copy
copy3 = copy.deepcopy(origional)
# print("Same object?", origional is copy3)
# print("Shared List?", origional[0] is copy3[0], "\n")


# ! combining

letter = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]

# comb = letter + numbers
# print("Combined", letter + numbers)


# ? extend()-> doesnot create a new list; it expand the origional one
numbers.extend(letter)
# print(numbers)


# ? zip()

# comb = list(zip(numbers, letter))
comb = list(zip(numbers, letter, "Hi"))
# print(comb)


# todo: Iterable
# * An object that can be looped through one by one using a for loop.
# * Examples: list, tuple, string, set, dictionary

l = ['apple', 'bananana', 'grapes']
# for fruit in l:
# print(fruit.upper())

# todo: Iterator:
# * An object that keeps track of the current position during iteration
# * and returns the next value using next().


l = ['apple', 'bananana', 'grapes']

# * 1. enumerate()
# print(list(enumerate(l)))
# for index, value in enumerate(l):
# print(index, value)

# * 2. reversed()
# print(reversed(l))
# print(list(reversed(l)))


# for reverse in reversed(l):
#     print(reverse)


# * 3. zip()
# number = [1, 2, 3]
# print(zip(l, number))
# print(list(zip(l, number)))

# for l, n in zip(number, l):
#     print(l, n)


# * 4. map
# print(list(map(str.upper,l)))

number = [1, 2, 3, 4]
# print(list(map(int,number)))

name = [' bilal', ' nabeel', '  akmal  ']
# print(list(map(str.strip,name)))

# * 5. filter

letterss = ['a', '', 'b', None, 'c', None]
print(filter(None, letterss))
print(list(filter(None, letterss)))
