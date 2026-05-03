# variable

# name = "Bilal"
# language = "JavaScript"
# print("\nMy name is", name)
# print(name,"is learning", language,"programming language")
# print(name,"want to become a", language,"developer")

# challenege

# name = "datawithbaara.com"
# arate='@'
# print("info" +arate + name)
# print("support" + arate + name)
# print('www.' + name)

# name = "datawithbaraa.com"
# arate = "@"

# print("info", arate, name)
# print("support", arate, name)
# print("www.", name)


# ! Data Types

# a = "Bilal" # string
# b = 25 # integer
# c = 5.9 # float
# d = True # boolean
# e = 'bilal' # string
# f = None # NoneType
# g = "" # empty string
# i = " " # string with space
# h = "222" # string that looks like a number

# a = "bilal"
# print(a.upper()) # converts to uppercase
# print(a.lower()) # converts to lowercase
# b= 10
# print(len(a)) # returns the length of the string
# print(b.bit_length()) # returns the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros.


# age = int(input("Enter your age: "))
# height = float(input("Enter your height in cm: "))
# name = str(input("Enter your name: "))
# student = bool(input("Are you a student? (True/False): "))

# nothing_val = None
# print("You are", age, "years old and", height,
#       "cm tall.", name + " is a student:", student)
# print("Nothing value:", nothing_val)


# ! type str
# a = "bilal"
# print(type(a))


# age = 20

# print(type(age))
# print("My age is: " +  str(age))

# age += 5
# print("My age after 5 years will be: " + str(age))
# print(type(age))

# ! count the number of characters in a string
# name = """
# Bilal
# """
# print("Number of characters in the string:", len(name))

# # count
# repeat_count = """
# i love Pakistan. Pakistan is a very beautiful country. I want to visit Pakistan again and again.
# """
# print("Number of times 'Pakistan' appears in the string:", repeat_count.count("Pakistan"))


# ! Transformations

# price = "11,00,000"
# print("Original price:", price.replace(",", "."))


# phone = "0300-1234567"
# print("phone",phone.replace("-",""))

# dollor_price = "$1,2229.000"
# print("dollor_price:", dollor_price.replace("$", "").replace(",",""))


# phone_num = "+49 (147) 123-4567"
# cleaned_phon_num = phone_num.replace("+","00").replace("(","").replace(")","").replace("-","").replace(" ","")
# print("Cleaned phone number:", cleaned_phon_num)

# ! concatenation
# first_name = "Bilal"
# last_name = "Khan"
# full_name = first_name + " " + last_name
# print("Full name:", full_name)


# ! f-string
# name = "bilal"
# age = 25
# is_student = True

# print("my name is " + name + " and I am " + str(age) + " year old. Am I am Student? " + str(is_student)+".")
# print(f"My name is {name} and I am {age} year old. Am I a student? {is_student}.")


# print(f"2 + 2 = {2 + 2}")


# ! split

# stamp = "2024-06-01 12:30:45"
# print("Original timestamp:", stamp)
# print(stamp.split("-"))


# print("="*20)

# slicing


# date = "2024-06-01"
# print("Original date:", date)

# print(date[0:4])
# print(date[:4])

# print(date[5:7])
# print(date[8:10])

# print(date[-2:])
# print(date[-5:-3])
# print(date[-10:-6])

# cleaning data
# lstripe
# text = "   Hello,       World!   "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())


# hel = "####### BVSS #######"
# print(hel.lstrip("#"))
# print(hel.rstrip("#"))
# print(hel.strip("#"))


# text = "  Engineering"
# print(len(text))
# print(len(text.strip()))
# print(len(text)-len(text.strip()))
# print(len(text)==len(text.strip()))


# print(text.upper())
# print(text.lower())
# print(text.title())


# messy_string = "968-Maria, ( D@t@ Engineer ) ;; 27y "
# print("Original messy string:", messy_string)

# parts = messy_string.split(",")
# print(parts)
# print("Parts:", len(parts))

# name_part = parts[0].split("-")[1].strip()
# print("Name part:", name_part)

# role_part = parts[1].split(";")[0].replace("(","").replace(")","").replace("@","a").strip().lower()
# print("Role part:", role_part)

# age_part = messy_string.split(";;")[1].replace("y","").strip()
# print("Age part:", age_part)

# print("Length of role part:", len(role_part))

# name_part = parts[0].split("-")[1].strip()
# print("Name part:", name_part)

# role_part = parts[1].split(";")[0]
# print("Role part:", role_part)

# role = role_part.replace("(","").replace(")","").replace("@","a").strip().lower()
# print("Cleaned role:", role)

# age_part = messy_string.split(";;")[1]
# print("Age part:", age_part)
# # print("Age part:", age_part)
# age = age_part.replace("y","").strip()
# print("Cleaned age:", age)


# final_summary = f"Name: {name_part}, Role: {role}, Age: {age}"
# print("Final summary:", final_summary)


# order = "ORDER#88291-SUCCESS"

# parts = order.split("-")
# print(parts)
# num = parts[0].split("#")
# print(num)
# str_ord = num[0]
# print(str_ord)
# num_ord = num[1]
# print(num_ord)

# text = parts[1]
# print(text)

# print(f"Order number: {num_ord}, Status: {text}")


# url = "www.mysite.com/products/electronics/laptop"


# folder = url.split("/")
# print(folder)

# eletr = folder[2]
# print(f"electronics folder: {eletr}")


# ! search

# phone = "+92-300-1234567"
# print("Original phone number:", phone)
# print("+92 start",phone.startswith("+92"))
# print("1234567 end",phone.endswith("12345d67"))

# print("300" in phone)

# line = "Banda-Banda-Banda"
# print(line.find("-")) # returns the index of the first occurrence of the specified substring. If the substring is not found, it returns -1.

# RN = "2024-BSSE-001"
# post = RN.find("-")
# print("Position of first hyphen:", post)
# print("Substring after first hyphen:", RN[post+1:])

# fruit = "BA-NA-NA"
# print(fruit.find("-"))
# print(fruit[fruit.find("-")+1:])


# ! valid variable names
# country = "Pakistan"
# print(country.isalpha()) # checks if all characters in the string are alphabetic
# print(country.isalnum()) # checks if all characters in the string are alphanumeric (letters and numbers)
# print(country.isdigit()) # checks if all characters in the string are digits
# print(country.isnumeric())
