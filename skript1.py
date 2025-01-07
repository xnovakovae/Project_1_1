"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Eva Novakova
email: xnovakovae@seznam.cz
"""

users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

users_passwords = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

for Access in users_passwords:
    user = input("Username:")
    password = input("Password:")
 
    if user in users and password:
        print("Welcome to the app", user,
        "We have 3 texts to be analyzed")
        break
    else:
        print("Unregistered user, terminating the program.")

print(input("Enter a number btw. 1 and 3 to select:"))
    




    
  

