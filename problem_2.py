

# ! challenge

# !1.Validate the Quality and Correctness of Email Values
# * Must not be empty

# * Must contain '.' and '@'

# * Must contain exactly one '@' symbol

# * Must end with '.com', '.org', or '.net'

# * Must not be longer than 254 characters

# * Must start and end with a letter or digit


email = "bila!!l123@gmail.com"
# clean a string
email = email.strip()

# # * Email must not be empty
if email == "":
    print("Email cannot be empty")
# * Must contain '.' and '@'
elif not ("@" in email and "." in email):
    print("Email must be contain . and @")
# * Must contain exactly one '@' symbol
elif email.count('@') != 1:
    print("Email must be contain exactly one at least @")
# * Must end with '.com', '.org', or '.net'
elif not (email.endswith(('.com', '.org', '.net'))):
    print("Email Must be end with '.com', '.org', or '.net'")
# * Must not be longer than 254 characters
elif len(email) > 254:
    print("Email must not be longer than 254 characters")
# * Must start and end with a letter or digit
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email valid")
