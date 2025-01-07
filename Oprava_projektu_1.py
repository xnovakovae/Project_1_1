"""
projekt_1.py: Opravena verze - první projekt do Engeto Online Python Akademie

author: Eva Novakova
email: xnovakovae@seznam.cz
"""

from collections import Counter

# Funkce pro načítání textů uživatelem
def load_texts():
    # Předdefinované texty
    texts = [
        """Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley.""",
        """At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick.""",
        """The monument contains 8198 acres and protects
        a portion of the largest deposit of freshwater fish
        fossils in the world. The richest fossil fish deposits
        are found in multiple limestone layers, which lie some
        100 feet below the top of the butte. The fossils
        represent several varieties of perch, as well as
        other freshwater genera and herring similar to those
        in modern oceans. Other fish such as paddlefish,
        garpike and stingray are also present."""
    ]
    # Tady můžeš přidat i možnost pro uživatele zadat nové texty
    # Pokud chceš, můžeš tu přidat nějaký vstup, nebo ponechat texty jako pevně definované
    return texts

# Načítání textů
texts = load_texts()

# Uživatelé a jejich hesla
users_passwords = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Přihlášení uživatele
user = input("Username: ")
password = input("Password: ")

print("-" * 45)

if user in users_passwords and password == users_passwords[user]:
    print(f"Welcome to the app, {user}")
    print(f"We have {len(texts)} texts to be analyzed.")
else:
    print("Invalid credentials, terminating the program.")
    exit()

print("-" * 45)

# Výběr textu
try:
    text_number = int(input(f"Enter a number between 1 and {len(texts)} to select: "))
    if text_number <= 0 or text_number > len(texts):
        raise ValueError("Number out of range.")
except ValueError:
    print("Invalid entry. Terminating the program.")
    exit()

print("-" * 45)
selected_text = texts[text_number - 1]

# Analýza textu
words = selected_text.split()
number_of_words = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = 0
sum_of_numbers = 0
word_lengths = []

for word in words:
    clean_word = word.strip(",.!?")
    number_of_words += 1
    word_lengths.append(len(clean_word))

    if clean_word.istitle():
        titlecase_words += 1
    elif clean_word.isupper():
        uppercase_words += 1
    elif clean_word.islower():
        lowercase_words += 1
    elif clean_word.isnumeric():
        numeric_strings += 1
        sum_of_numbers += int(clean_word)

# Výstup analýzy textu
print(f"There are {number_of_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_strings} numeric strings.")
print(f"The sum of all the numbers is {sum_of_numbers}.")
print("-" * 35)

# Tabulka rozložení délek slov
length_counts = Counter(word_lengths)

print(f"{'LEN':<3}|{'OCCURENCES':^13}|{'NR.':>3}")
print("-" * 35)
for length, count in sorted(length_counts.items()):
    bar = '*' * count
    print(f"{length:<3}|{bar:<13}|{count:>3}")
