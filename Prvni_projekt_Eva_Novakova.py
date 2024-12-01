"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Eva Novakova
email: xnovakovae@seznam.cz
"""

# Uživatelé a jejich hesla
users_passwords = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Přihlášení uživatele
user = input("Username: ")
password = input("Password: ")

print("-" * 45)

if user in users_passwords and password == users_passwords[user]:
    print(f"Welcome to the app, {user}")
    print("We have 3 texts to be analyzed.")
else:
    print("Invalid credentials, terminating the program.")
    exit ()

print("-" * 45)

# Texty
TEXT_1 = """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""

TEXT_2 = """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick."""

TEXT_3 = """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""

texts = [TEXT_1, TEXT_2, TEXT_3]

# Výběr textu
text_number = input("Enter a number 1 and 3 to select: ")
print("-" * 45)

if text_number not in {"1", "2", "3"}:
    print("Invalid entry. Terminating the program.")
    print("-" * 45)

selected_text = texts[int(text_number) - 1]

# Analýza textu
words = selected_text.split()
number_of_words = len(words)
titlecase_words = sum(1 for word in words if word.istitle())
uppercase_words = sum(1 for word in words if word.isupper())
lowercase_words = sum(1 for word in words if word.islower())
numeric_strings = sum(1 for word in words if word.isnumeric())
sum_of_numbers = sum(int(word) for word in words if word.isnumeric())

# Výstup analýzy textu
print(f"There are {number_of_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_strings} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers}")
print("-" * 35)

# Délky slov
from collections import Counter

word_lengths = [len(word.strip(",.!?")) for word in words]
length_counts = Counter(word_lengths)

# Tabulka rozložení délek slov
print(f"{'LEN':<3}|{'OCCURENCES':^13}|{'NR.':>3}")
print("-" * 35)
for length, count in sorted(length_counts.items()):
    print(f"{length:<3}|{'*' * count:<13}|{count:>3}")