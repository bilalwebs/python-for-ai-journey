
#  !numeric


# x = 5
# y=4.5
# z =3+ 3j

# print(type(x))
# print(type(y))
# print(type(z))


# h = '23'
# print(type(h))
# print(h * 4)

# h = int(h)
# print(type(h))
# print(h * 3)


# x = 3.14
# print(int(x))

# x = 3
# print(float(x))

# x = "3"
# print(float(x))

# x = 3
# y = 6
# print(complex(x,y))


# print(3+2)
# print(3-2)
# print(3*2)
# print(3/2)
# print(3//2)
# print(3**2)
# print(3%2)

# x = 2
# # x = x + 3
# x += 3
# print(x)

# x -= 3
# print(x)

# x *= 3
# print(x)

# x /= 3
# print(x)


#! measure distance

# print(2 - 10)
# print(abs(2 - 10))

# ! rounding
# import math
# price = 35.7474747
# print(round(price))
# print(round(price,2))
# print(round(price,1))
# print(math.floor(price))
# print(math.ceil(price))
# print(math.trunc(price))


#! random
# import random
# print(random.random())
# print(random.randint(1,6))


# !validation

# x = 7.7
# print(x.is_integer())

# x = 7.0
# print(x.is_integer())

# x = 77
# x = 77.77
# print(isinstance(x,int))
# print(isinstance(x,float))


import random
res = random.randint(1, 100)
if (res % 2 == 0):
    print("even", res)

else:
    print("Odd", res)
