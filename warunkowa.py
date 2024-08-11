if (5 > 3):
    print("LALALA")

WYBOR = input("1 - MNOŻENIE, 2 - DZIELENIE, 3 - DODAWANIE, 4 - ODEJMOWANIE ")
  
A = int(input("wPISZ LICZBĘ A: "))
B = int(input("WPISZ LICZBĘ B: "))

if(WYBOR == '1'):
    print(A * B)
elif (WYBOR == '2'):
    if (B == 0):
        print("NIE DZIEL PRZEZ ZERO")
    else:
        print("A / B")
elif(WYBOR == '3'):
    print(A + B)
elif(WYBOR == '4'):
    print(A - B)
else:
    print("A JEST RÓWNE B")
