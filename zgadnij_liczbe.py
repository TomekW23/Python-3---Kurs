szukana_liczba = 40

zgadywana_liczba = 0

while zgadywana_liczba !=szukana_liczba:
    zgadywana_liczba = int(input("Odgadnij liczbę: "))

    if(zgadywana_liczba == szukana_liczba):
        print("BRAWO!")
    elif (zgadywana_liczba < szukana_liczba):
        print("Za mała!")
    else:
        print("Za duza!")   
