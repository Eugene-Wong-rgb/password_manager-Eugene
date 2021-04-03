#password_manager.py
print("Hi, welcome to Eugene's password programme. You must be 10 or over to qualify. ")

password_list = []
user_list = []



#Functions 

def age():
  age = int(float(input("What is your age: ")))
  if age < 13:
    print("You do not qualify")
  elif age >= 13:
      print("You qualify and may proceed.")
age() 
def new_user():
