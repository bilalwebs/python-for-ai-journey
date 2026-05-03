
#! logic and operator

# * condiional statement
# if else elif


# * loops
# types --> for, while
# control --> break, pass, continue


# print(True)
# print(False)
# print(type(False))
# print(bool(555))
# print(bool("555"))
# print(bool(""))
# print(bool( ))
# print(bool(0))
# print(bool(None))


# email = "bilal@gmail.com"
# phone = "1234-666366363"
# username ="barar"

# email = "bilal@gmail.com"
# phone = ""
# username ="barar"

# email = ""
# phone = "1234-666366363"
# username =""


# any() Python ka built-in function hai jo check karta hai:

# 👉 list me koi bhi value True (ya non-empty) hai ya nahi

# Agar ek bhi value True ho → result True
# Agar sab False ho → result False

# print(any["email",'phone','username'])
# print(any([email,phone,username])) # true
# print(any([email,phone,username]))


# print(isinstance(123, int))
# print(isinstance(1.23, float))


# print("Hello".startswith("o"))
# print("Hello".endswith("e"))

# ! comparison operator

# print(10 == 10)  # T
# print(10 != 10)  # f
# print(3 > 10)   # f
# print(3 < 10)  # t
# print(3 <= 10)  # t
# print(3 >= 10)  # f


# print("a" == "A")
# print("a" = "A") # single equal assign value
# print("a" != "A")

# print(1 < 4 < 6) # left to right

# age = 12
# print(18 <= age <= 30)


#! logical operator

# print(3 > 1 and 5 < 1)
# print(3 > 1 and 5 > 1)

# print(3 > 1 or 5 < 1)
# print(3 > 1 or 5 > 1)


# cpu_usage = 70
# memory_usage = 75
#         # T          and   T
# res = cpu_usage > 90 and memory_usage > 90
# print(res)


# x = 15
# y = 8

# print(x > 10 and y > 10) # f  and f


# a = 5
# b = 20

# print(a > 10 or b > 10) # f or t

# age = 17
# has_ticket = True

# print(age >= 18 and has_ticket) # f


# a = 10
# b = 20
# c = 30

# print(a > 5 and b > 10 and c > 25) # f and T  and t

# a = 2
# b = 3
# c = 50

# print(a > 10 or b > 10 or c > 10) # f or f or t

# a = 12
# b = 6
# c = 20

# print(a > 10 and b < 5 or c > 15) # t and f or t

# a = 10
# b = 3
# c = 20

# print((a > 5 and b > 5) or c > 15) # t and f = f or t

# x = 8
# y = 12
# z = 5

# print(x > 10 and (y > 10 or z > 10)) # f and ( t or t)

# age = 17
# has_id = True
# vip = False

# print((age >= 18 and has_id) or vip) # f and t or f


# ! challenge
# is_logged_in = True
# is_guest = False
# is_banned = False
# print(is_logged_in or is_guest and not is_banned)

# ! membership (in,not in)
# print("i" in "Bilal")
# print("s" in "Bilal")
# print("ss" not in "Bilal")
# print("apple" not in ['apple', 'banana'])
# print("apple" in ['apple', 'banana'])

# email = "test@gmail.com"

# print("@" in email)

# ! challenge
# domain_name = "@gmail.com"
# banned_domains = [
#     "@spam.com",
#     "@fake.com",
#     "@tempmail.com",
#     "@10minutemail.com",
#     "@disposable.com"
# ]

# print(domain_name in banned_domains)
# print(domain_name not in banned_domains)


# email = "test@gmail.com"
# phone = ""

# print(("@" in email) or phone) # t or f


# ! identity (is,is not)


# a = [1, 2, 3]
# b = a

# print(a is b)   # True
# print(id(a),id(b))

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a is b)   # False
# print(id(a), id(b))  # different id


# x = ['a','b','c']
# # y = ['a','b','c']
# y = x
# print(x == y)
# print(x is y)


#  challenge
# email = None
# print(email != None and email != "")
# print(email == None and email != "")
# print(email is None and email != "")
# print(email is not None and email != "")

