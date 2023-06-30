"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Janovec
email: p.janovec@seznam.cz
discord: djolefola
"""
import re 

texts = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
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


users = [("bob", "123"), ("ann", "123"), ("mike", "password123"), ("liz", "pass123")]
del_char = "-" 
del_len = 40
delimiter = del_char * del_len 

login = input("username: ")
pwd = input("password: ")

if (login, pwd) not in users:
    print("Unregistered user, terminating the program..")
    quit()

print(delimiter)
print(f"Welcome to the app, {login}!\nWe have 3 texts to be analyzed.")
print(delimiter)
select =  input("Enter a number between 1 and 3 to select:")
print(delimiter)

if not re.match("^[1-3]$", select.strip(" ")):
    print("Invalid value, terminating the program..")
    quit()

my_text = "".join(char for char in texts[int(select)-1] if char not in ".;,/|")
words = my_text.split()

words_len = {}
title = 0
upcase = 0
lowcase = 0
num = 0
numsum = 0

for word in words:
    length = len(word)
    if length in words_len:
        words_len[length] += 1
    else:
        words_len[length] = 1
    if word.istitle():
        title += 1
    if word.isupper() and word[0].isalpha():
        upcase += 1
    if word.islower():
        lowcase += 1
    if word.isnumeric():
        num +=1
        numsum += int(word)

sort_len = sorted(words_len.items())

print(f"There are {len(words)} words in the selected text.")
print(f"There are {title} titlecase words.")
print(f"There are {upcase} uppercase words.")
print(f"There are {lowcase} lowercase words.")
print(f"There are {num} numeric strings.")
print(f"The sum of all numbers {numsum}")
print(delimiter) 

header = ("LEN|"+"OCCURENCES".center(int(del_len/2))+"|NR".center(int(del_len/5)
))
pos_1 = header.find("|")
pos_2 = header.find("|", pos_1 + 1 )
print(header)
print(delimiter)
for key, value in sort_len:
    print(str(key).rjust(pos_1) + "|" + value * "*"  + ("|" + str(value)).rjust(pos_2 - pos_1 - (value - len(str(value))))) #sorry for this..

