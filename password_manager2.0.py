#Welcome to password manager. Asks user to make an account for password manager 
#sub routine
name = input("Hello, what is your name?")
while True:
    try:
        age = float(input("What is your age?"))
        if age < 13:
            print("you do not qualify to make an account")
            print(" Thank you {} for using pasword manager".format(name))
        elif age <= 100:
          print("age meets requirements")
          break
        else:
            print("please enter a valid age")
    except ValueError:
        print("please input valid age")
print("Welcome to Password Manager. Thank you for using Password Manager! ")
