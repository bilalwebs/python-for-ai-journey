
# ! Python Challenges
# * Check if a user's name is not empty and the age is greater than or equal to 18

name = "Bilal"
age = 18

is_res = name != "" and age >= 18
print("Result: ", is_res)

# * Check if the password is at least 8 characters long and does not contain spaces

password = "mySecurePassword123"
is_secure = len(password) >= 8 and " " not in password
print(is_secure)

# * Check if a user's email is not empty, contains '@', and ends with '.com'

user = "bilal@gmail.com"
res = user != " " and "@" in user and user.endswith(".com")
print(res)
print("@" in user)
print(user.endswith(".com"))

# * Check if a username is a string, is not None, and is longer than 5 characters


userName = "BilalCode"
res = userName is not None and len(userName) >= 5
print(res)
