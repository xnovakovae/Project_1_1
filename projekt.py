"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Eva Novakova
email: xnovakovae@seznam.cz
"""
#users = ["bob", "ann", "mike", "liz"]
#passwords = ["123", "pass123", "password123", "pass123"]

users_passwords = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}


user = input("Username:")
password = input("Password:")
if user in users_passwords: 
    if password == users_passwords [user]:
        print("Welcome to the app,", user +".\nWe have 3 texts to be analyzed")
    else:
        print("Incorrect password, terminating the program.")                
else:
    print("Unregistered user, terminating the program.")

TEXT_1 = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''']
TEXT_2 = ['''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''']
TEXT_3 = ['''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

text_numbers = [1,2,3]   

if password == users_passwords [user]:

    text_number = (input("Enter a number 1 or 2 or 3 to select the text:"))
    if text_number in ("1","2","3"):
        print ("Please see text details below:")
    else:
        print ("Invalid entry. Terminating the program.")

text1 = str("""Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.""")

if text_number is "1":
    words = text1.split()
    number_of_words = len(words)
    print ("There are", number_of_words, "words in the selected text.")

    words = text1.split()
    titlecases = 0
    for titlecase in words:
        if titlecase[0].isupper():
            titlecases += 1
    print ("There are", titlecases, "titlecase words.")

    words = text1.split()
    upper = 0
    for upper_case in words:
        if(upper_case.isupper()):
            if not upper_case.isalpha():
                upper += 1

    print("The number of uppercase words is:",upper)  


    lower = 0
    for lower_case in words:
        if(lower_case[0].islower()):
            lower+=1
    print("The number of lowercase words is:",lower)

    # Počítání numerických řetězců
    numeric = 0
    sum_of_numbers = 0  # Nová proměnná pro součet čísel
    for numeric_str in words:
        if numeric_str.isnumeric():  # Pokud je řetězec číslo
            numeric += 1
            sum_of_numbers += int(numeric_str)  # Převod na celé číslo a sečítání

    print ("There are", numeric, "numeric strings.")
    print(f"The sum of all the numbers is {sum_of_numbers}.")
  

     

    # Text
    text1 = """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley."""

    # Rozdělíme text na slova
    words = text1.split()

    # Získáme délky slov
    lengths = [len(word.strip(",.!?")) for word in words]  # Odstraníme interpunkci, pokud je přítomná

    # Spočítáme výskyt každé délky slova
    length_counts = Counter(lengths)

    # Výpis výsledků
    print(f"{'LEN':<5}{'OCCURENCES':<15}{'NR.'}")
    print("-" * 30)
    for length in sorted(length_counts.keys()):
        print(f"{length:<5}{'*' * length_counts[length]:<15}{length_counts[length]}")

text2 = str("""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""")

if text_number is "2":
    
    words2 = text2.split()
    number_of_words = len(words2)
    print ("There are", number_of_words, "words in the selected text.")

    words2 = text2.split()
    titlecases = 0
    for titlecase in words2:
        if titlecase[0].isupper():
            titlecases += 1
    print ("There are", titlecases, "titlecase words.")

    words2 = text2.split()
    upper = 0
    for upper_case in words2:
        if(upper_case.isupper()):
            if not upper_case.isalpha():
                upper += 1

    print("The number of uppercase words is:",upper)  

    lower = 0
    for lower_case in words2:
        if(lower_case[0].islower()):
            lower+=1
    print("The number of lowercase words is:",lower)

    numeric2 = 0
    sum_of_numbers2 = 0
    for number2 in words2:
        if number2.isnumeric():
            numeric2 += 1
            sum_of_numbers2 += int(number2)
    print (numeric2)
    print (sum_of_numbers2)
