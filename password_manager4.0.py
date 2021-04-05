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

#Ask user to create/login to account in Password Manager
#sub routine
while True:
    try:
        print("1) Log in to account")
        print("2) Create an account")
        mode_1 = float(input("Enter numbers 1 or 2 to chose a mode \n>"))
    #create account
        if mode_1 == 2:
            account = input("New account name \n>")
            account_password = check_password()
        #write to file
            with open("Account_file.txt", 'a') as file:
                file.write("{} {}".format(account, account_password ))
                file.write("\n")
                break

    #log in to account
        elif mode_1 == 1:
            while True:
                account = input("What is your account username \n>")
                account_password = input("What is your password \n>")
                
    #main routine
        while True:
            print("< Menu >")
            print("1) Save Usernames, Passwords and Apps/Website")
            print("2) Veiw Usernames, Passwords and App/Website")
            print("3) Exit")
        try:
            option = float(input("Enter 1 2 or 3:"))
            if option == 1:
                username = input("Username:")
                password = input("Password:")
                website = input("Website:")               
