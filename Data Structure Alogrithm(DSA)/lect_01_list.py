

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
number = [1, 2, 3, 4]

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
