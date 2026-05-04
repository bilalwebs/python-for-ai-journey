
# ! Topic Loops

# item = (1, 2, 3, 4)
# item = [1, 2, 3, 4,"Hi Babar"]
# item = "Data Science";
# for items in item:
#     print(f"Range in {items}")


# ! range
# range(start,stop,step)
# for i in range(2,21,2):
#     print(i)


# * exercise
# scores = [80, 70, 66, 55]
# total = 0

# for score in scores:
#     total += score
#     print(f"Current Total: {total}")
# print("Final Total: ", total)


# data = [' REPORT.CSV', ' Data.xlsx ', '      AnalticsSS.TXT']

# for file in data:
#     files = file.strip().lower().replace("txt", 'csv').replace('xlsx','csv')
#     print("Data Processing :", files)


# ! challenge Table 7
# table = 7
# print("Table = ", table, "\n")
# for i in range(1, 11):
#     print(f"{table} x {i} = {table * i}")


#!  break
# name = ['bilal', 'maria', '', 'nabeel']
# for names in name:
#     if names == "":
#         print("Empty value detected!!")
#         break
#     print(f"Name: {names}")


# ! continue
# name = ['bilal', 'maria', '', 'nabeel']
# for names in name:
#     if names == "":
#         print("Empty value detected!!")
#         continue
#     print(f"Name: {names}")


# !pass
# name = ['bilal', 'maria', '', 'nabeel']
# for names in name:
#     if names == "":
#         # pass  # todo : Handle Empty Value
#         names = names.replace("", "unknowm")
#     print(f"Name: {names}")

# if 5 > 2:
#     pass  # Ab error nahi ayega, Python samajh jayega ke abhi yahan kuch nahi karna.

# numbers = [1, 2, 3, 4, 5]

# for n in numbers:
#     if n == 3:
#         pass # Jab 3 aaye toh kuch mat karo
#     else:
#         print(f"Number is: {n}")


# ! TASK

# * Loop through a list of days and print only the working days, skipping the weekends

# List of days
# days = ["Monday", "Tuesday", "Wednesday",
#         "Thursday", "Friday", "Saturday", "Sunday"]

# print("--- Working Days List ---")
# for day in days:
#     # print(day)
#     if day == "Saturday" or day == "Sunday":
#         continue
#     print("Working Day: ", day)


# for day in days:
#     if day in ['Saturday', 'Sunday']:
#         continue
#     print("Working Day: ", day)


# * "Scan emails to block unsafe data from entering your system"

# emails = [
#     'data@gmail.com',
#     'baraa@outlook.de',
#     "DROP TBLE USER;",
#     "maria@gmail.com"
# ]

# for email in emails:
#     if ";" in email:
#         print("SQL Injection: Hacker Attack")
#         break
#     print(f"Processing Email in {email}")


# ! Emails ki list
# emails = [
#     "Hello, how are you?",
#     "Win a free iPhone now!",
#     "Warning: This file contains a virus",
#     "Meeting scheduled for tomorrow",
#     "Download this malware.exe file"
# ]

# print("--- Email Scanning Started ---")

# for mail in emails:
#     # Safai ke liye text ko lower case mein convert kar rahe hain
#     check_mail = mail.lower()

#     # Check karein agar unsafe words hain
#     if "virus" in check_mail or "malware" in check_mail:
#         print("ALERT: Unsafe email blocked!")
#         continue  # Is email ko skip kar dou aur aglay par jao

#     # Agar email safe hai toh ye line chalegi
#     print(f"Processing Email: {mail}")

# print("--- Scanning Finished ---")


# for i in range(1,10):
#     print(f"Range: {i}")
# else:
#     print("Loops is complete")


# *1. even number check

# items = [1, 3, 5, 7, 9]
# for i in items:
#     if i % 2 == 0:
#         print(f"Even number found: {i}")
#         break
#     else:
#         print(f"All number are Odd")

# * 2.
# names = ['Kamara', 'Bilal', None, 'Nabeel']

# for name in names:
#     if name is None:
#         print(f"Foun is missing name.")
#         break
# else:
#     print(F"All name avalibale")

# * 3.
# files = ['data1.csv',
#          'report.pdf   ',
#          'reporst.pdf   ',
#          'dataset.csv '
#          ]

# all_file = True
# for file in files:
#     file = file.strip()
#     if not file.endswith('.csv'):
#         print(f"{file} is not csv")
#         all_file = False
# else:
#     print(f"All File are csv")


# *
# files = ['data1.csv',
#          'report.pdf   ',
#          'reporst.pdf   ',
#          'dataset.csv '
#          ]

# for file in files:
#     file = file.strip()
#     if not file.endswith(".csv"):
#         print(f"{file} is not csv")
#         # continue
#         break
# else:
#     print(f"All file are csv")


# *
# files = ['data1.csv',
#          'report.pdf   ',
#          'reporst.pdf   ',
#          'dataset.csv '
#          ]

# for file in files:
#     file = file.strip()
#     if not file.endswith(".csv"):
#         print(f"{file} is not csv")

# ! challanege

# file_list = [
#     'report.csv',
#     'data.xlsx',
#     'data.csv',
#     'summary.docs',
#     'report.csv',
#     'data.csv',
# ]
# file_data = []
# for file in file_list:
#     if file not in file_data:
#         file_data.append(file)

# print(f"All Unique file", file_data)


# ! outer and inner loop

# * method 1
# for x in [1, 2, 3]:
#     for y in [1, 2]:
#         print(x, y)


# * method 2
# for x in range(3): #outer loop
#     for y in range(2): #inner loop
#         print(x,y)

# for x in range(3): #outer loop
#     for y in range(2): #inner loop
#         for z in range(2):
#             print(f"({x},{y},{z})")

# *
# colors = ['red', 'green', 'blue']
# sizes = ["S", "M", "L"]

# for color in colors:
#     for size in sizes:
#         print(f"{color} - Size {size}")


# *
# years = [2026, 2027]
# months = ['Jan', 'Feb']
# days = range(1, 29)

# for y in years:
#     for m in months:
#         for d in days:
#             print(f"report_{y}_{m}_{d}.csv")


# *
# SELECT count(*) FROM customers where id IS NULL;
tables = ['customer', 'order', 'product', 'price']
columns = ['id', 'created_date']

for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {c} where {c} IS NULL;")
