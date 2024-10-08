krotka = (1, 42, 12, -4)

# dictionary - słownik KLUCZ - WARTOŚĆ

pokoje = {49: 'Arkadiusz Włodarczyk', 69: 'Wiletta Włodareczyk'}

"""
     czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
listy          NIE           TAK             TAK                   TAK
krotki         NIE           TAK             NIE                   NIE
słowniki       TAK           NIE             TAK                   TAK
zbiory         TAK           NIE  ```           NIE                   TAK

        ZBIORY: BONUS w postaci | & - ^ 
"""

A = {1, 4, 20, -4, 20}

B = {1, 4}

print(A.issubset(B))

# TYPY ZAGNIEŻDZONE

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"


osoba1 = ('Arkadiusz', 29, 'mężczyzna')
osoba2 = ('Wioletta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mężczyzna')

listaGosci = {
    ('Arkadiusz', 28, 'mężczyzna'),
    ('Wioletta', 22, 'kobieta'),
    ('Kuba', 32, 'mężczyzna')
}
listaGosci2 = {
    ('Arkadiusz', 28, 'mężczyzna'),
    ('W', 22, 'kobieta'),
    ('K', 32, 'mężczyzna')
}

listaGosci3 = listaGosci & listaGosci2

for imie, wiek, plec in listaGosci:
    print("Imię: ", imie)
    print("Wiek: ", wiek)
    print("Płeć; ", plec)
    print("\n")


people = {
    "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
    "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
    "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
    "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
    "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
    "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
    "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
    "4WW4F4HiUTP5dBdHatPw": {'name': 'Marie', 'age': 2, 'sex': 'Female'},
    "yuHhrXS1xsSql7kIEnUH": {'name': 'Leila', 'age': 24, 'sex': 'Female'},
    "76XBNSkJn1BIRoX3hB0s": {'name': 'Eric', 'age': 27, 'sex': 'Male'},
    "dMii4kQO1XW4WoiVI7S4": {'name': 'Tobey', 'age': 22, 'sex': 'Female'},
    "DU3Zi0aNj2LLAfujLUWB": {'name': 'Missy', 'age': 25, 'sex': 'Female'}
}

people2 = [
    {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
    {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
    {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
]

oceny = {
    "Arkadiusz": (2, 1, 2, 3, 2, 3),
    "Wiola": (4, 2, 1, 3, 4)
}


"""

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]
for name, age, sex in ppllist2:
    print(name)

"""

for id, dictionary in people.items():
    print("ID", id)
    for key in dictionary:
        print(key, ":", dictionary[key])


people2 = [
    {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
    {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
    {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
]

people3 = ["Arkadiusz",
           "Wiola",
           "Kuba"
           ]

ratings1 = {
    "Arkadiusz": (2, 1, 2, 3, 2, 3),
    "Agness": (4, 2, 1, 3, 4)
}
ratings2 = [
    {'name': "Arkadiusz", 'ratings': (2, 1, 2, 3, 2, 3), 'behaviour': 4},
    {'name': "Agness", 'ratings': (4, 2, 1, 3, 4), 'behaviour': 2}
]

ratings3 = {
    "Arkadiusz": {'ratings': (2, 1, 2, 3, 2, 3), 'behaviour': 4},
    "Agness:": {'ratings': (4, 2, 1, 3, 4), 'behaviour': 2}
}
"""
print(people["IcFDG2bO9AYDF651DoyH"])

for key in people:
    print("ID:", key)
    for secondaryKey in people[key]:
        print(secondaryKey, people[key][secondaryKey])


for key in ratings1:
    print(key, "oceny", ratings1[key])


for dictionary in people2:
    for key in dictionary:
        print(key, ":", dictionary[key])
        
 """
