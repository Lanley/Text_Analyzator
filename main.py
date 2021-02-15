'''
author = Pavel Baranek
'''
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

separator = 60 * "-"

registrated_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

print(separator)
username = input("Please enter the Username: ")
password = input("Please enter the Password: ")

print(separator)

if registrated_users.get(username) == password:
    print("login successful")
    print(f"Welcome to the app, {username} ")

else:
    print("Wrong input. Please use valid username and password. ")
    exit()

print(separator)

print("""
In next step, chose one of the following texts to be analyzed: 

text no. 1:
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.

text no. 2:
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.

text no. 3:
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.

""")

print(separator)

choice = int(input("Write your choice: "))
chosen_text = TEXTS[choice - 1]

print(separator)

separated_words = chosen_text.split()
clean_words = []

for a in separated_words:
    a = a.strip(",.-_!:\/|*")
    clean_words.append(a)

titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
sum_of_text = 0

for b in clean_words:
    if b.istitle():
        titlecase += 1

    elif b.isupper():
        uppercase += 1

    elif b.islower():
        lowercase += 1

    elif b.isnumeric():
        numeric += 1

for c in clean_words:
    if c.isnumeric():
        sum_of_text = int(sum_of_text) + int(c)

print("There are", len(clean_words), "words", "in total in selected text no.", choice)
print(f"The sum of all the numbers in selected text is {sum_of_text} ")

print(separator)

print(f"There is/are {titlecase} titlecase word/s. ")
print(f"There is/are {uppercase} uppercase word/s.")
print(f"There is/are {lowercase} lowercase word/s.")
print(f"There is/are {numeric} numeric string/s.")

print(separator)

print("LEN | OCCURANCES | NUMBER")

number_of_chars = []
dic_of_chars = {}

for d in clean_words:
    len_word = len(d)
    number_of_chars.append(len_word)

for e in number_of_chars:
    dic_of_chars[e] = number_of_chars.count(e)

sorted_dic = sorted(dic_of_chars.items())

for key, value in sorted_dic:
    print(key, "|", "*" * value, "|", value)

print(separator)

print("Thank you for using our system, you have been logged out.")
print(separator)
print(separator)
exit()