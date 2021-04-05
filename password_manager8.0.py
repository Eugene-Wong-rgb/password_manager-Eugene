#Eugene Wong

#Password Manager 

#Searches for errors in users input
import re
#Tells user how many tries they are allowed, when logging in.
tries = 3
#Checks if the password is complex enough (meet requirements)
def check_password():
    while True:
        password = input("Enter a password \n> ")
        if len(password) < 8:
            print("Make sure your password is at least 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
        elif re.search('[!, @, #, $, %, &, *, ~, `, (, ), +, , , -, ., /, :, ;, ", <, >, ?, \, _, |, {, }, ^]',password): 
            print("Make sure your password doesn't have special characters in it")            
        else:
            print("Your password is acceptable")
            break
    return(password)


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
                file.write("Account name: {} Password: {}".format(account, account_password ))
                file.write("\n")
                break

    #log in to account
        elif mode_1 == 1:
            while True:
                account = input("What is your account username \n>")
                account_password = input("What is your password \n>")
                d = {}
                #read file and make it a list
                with open('Account_file.txt') as f:
                    d = dict(x.rstrip().split(None, 1) for x in f)
                if d.get(account) == account_password:
                    print("pasword and username match")
                    break
                else:
                    if tries == 1:
                        print("You have reached maximum tries, Program will shut down")
                        raise SystemExit
                    else:
                        tries = tries - 1
                        print("incorrect pasword or account username {} tries left".format(tries))
            break
        else:
            print("please enter a valid niumber (1 or 2)")
    except ValueError:
        print("please enter a valid number(1 or 2)")

#main routine
while True:
    print("< Menu >")
    print("1) Save Usernames, Passwords and Apps/Website")
    print("2) Veiw Usernames, Passwords and App/Website")
    print("3) Exit")
    try:
        option = int(float(input("Enter 1 2 or 3:")))
        if option == 1:
            username = input("Username:")
            password = input("Password:")
            website = input("Website:")
            with open("{}.txt".format(account), 'a') as file:
                file.write("Username: {} \n".format(username))
                file.write("Password: {} \n".format(password))
                file.write("Website:  {} \n".format(website))
            
                
        elif option == 2:
            with open("{}.txt".format(account), 'r') as file:
                for line in file:
                    print(line)                        
        elif option == 3:
            print("Thank you for using password manager")
            print("Goodbye")
            break
        else:
            print("Enter 1,2 or 3")
    except ValueError:
        print("please enter a valid number 1,2 or 3")
