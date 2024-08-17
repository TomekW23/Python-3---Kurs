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
