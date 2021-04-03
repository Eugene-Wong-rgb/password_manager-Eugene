  while True:

    new_user = input("Enter a username to create a user for a new account: ")
    x = len(new_user)
    print(x)
    if x >= 5:
      print("Amount of letters in username qualify")
      user_list.append(new_user)
      break
    else:
      print("Username is too short must contain 5 or more letters")

def password():
    while True:
        new_password = input("Please enter a password (must be 8 or higher): ")
        y = len(new_password)
        print(y, "is the amount of letters in your pass")
        if y >= 8:
            print("password length qualify")
            password_list.append(new_password)
            break
        else:
            print("Password is too short try again.")   




#Main routine - Run main program in a loop

pirnt("Welcome to password manager!")
print("If you are 13 or older, You can store access details to web or mobile apps")

username = input("enter username to login.")
password =  int(input("enter password to login."))


