wynik = 0


i = 0
while i < 3:
    x = int(input("Podaj liczbę: "))
    if(x >0 and x % 2 == 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia i parzysta.")
        continue
    print("Aktualny wynik dodawania liczb to: ", wynik)
    i += 1

