

# counter = 1  # intialization

# while counter < 6:  # condition
#     print(counter)
#     counter += 1  # update


# answer = " "
# while answer != "yes":
#     answer = input("Do you agree(yes/no): ")
# print("thnk you")


# while True:
#     answer = input("Do you agree(yes/no): ")
#     if answer == "yes":
#         break
# print("thanks")


# ! challenge

# * 1. Challenge Instructions:

# Allow up to 3 attempts

# If the user types "yes", print "Glad we are on the same page"

# Otherwise, print "3 Strikes, You are Out!"


# attempt = 0

# while attempt < 3:
#     answer = input("Do you agree? (yes/no): ")
#     if answer == "yes":
#         print("Glad we are on the same page")
#         break
#     attempt += 1

# if attempt == 3:
#     print("3 Strikes, You are Out!")


# *2. Challenge: The Password Protector (Basic)
# password = " "
# while password != "python123":
#     password = input("Enter your Password: ")
#     if password != "python123":
#         print("Wrong Passwor: Try again")

# print("Congratulation")


# *3. Challenge: Number Guess
# secret_num = 7
# attempts = 0

# while attempts < 5:
#     user_gucess = int(input("Guess the number: "))

#     # 1. Compare with secret_num, NOT attempts
#     if user_gucess == secret_num:
#         print("Winner! You guessed it.")
#         break
#     else:
#         attempts += 1
#         print("Wrong guess! Try again.")

# # 2. Check if the loop finished because attempts ran out
# if attempts == 5:
#     print("Game Over! You've used all 5 attempts.")


# * 4

num = 1

while num < 11:
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd numver")

    num += 1
