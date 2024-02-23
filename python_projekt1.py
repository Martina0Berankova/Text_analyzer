"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martina Berankova
email: berankova.ma@centrum.cz
discord: Martina_b.0
"""

registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

username = input("username:")
password = input("password:")

if username in registered_users and registered_users[username] == password:
    print("-"*40)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("-"*40)

    selected_text = input("Enter a number btw. 1 and 3 to select: ")
    if selected_text.isdigit():
        selected_text = int(selected_text) - 1
        if 0 <= selected_text < len(TEXTS):
            text = TEXTS[selected_text]
            words = text.split()
            word_lengths = [len(word) for word in words]

            total_words = len(words)
            titlecase_words = sum(1 for word in words if word.istitle())
            uppercase_words = sum(1 for word in words if word.isupper())
            lowercase_words = sum(1 for word in words if word.islower())
            numeric_strings = sum(1 for word in words if word.isnumeric())
            sum_of_numbers = sum(int(word) for word in words if word.isnumeric())

            word_length_freq = {i: word_lengths.count(i) for i in set(word_lengths)}
            print("-" *40)
            print(f"There are {total_words} words in the selected text.")
            print(f"There are {titlecase_words} titlecase words.")
            print(f"There are {uppercase_words} uppercase words.")
            print(f"There are {lowercase_words} lowercase words.")
            print(f"There are {numeric_strings} numeric strings.")
            print(f"The sum of all the numbers {sum_of_numbers}")
            print("-" *40)
            print("LEN|  OCCURRENCES  |NR.")
            print("-" *40)
            for length, freq in sorted(word_length_freq.items()):
                print(f"{length:2}|{'*' * freq: <13}|{freq}")
        else:
            print("Invalid text selection. You were suppose to choose number btw 1-3. Terminating the program...")
    else:
        print("Invalid input. You were suppose to choose number btw 1-3. Terminating the program...")
else:
    print("Unregistered user, Terminating the program...")
