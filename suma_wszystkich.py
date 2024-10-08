"""
Mierzenie wydajności skryptu
"""

import time


def sumuj_do(liczba):
    suma = 0

    for liczba in range(1, liczba+1):
        suma = suma + liczba

    return suma


def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba+1)])


def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1, liczba+1)})


def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1, liczba+1)))


def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba


def finish_timer(start):
    end = time.perf_counter()
    return end-start


start = time.perf_counter()
print(sumuj_do(256))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do2(256))
print(finish_timer(start))


start = time.perf_counter()
print(sumuj_do3(256))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do4(256))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do5(256))
print(finish_timer(start))


def function_performance(func, arg, how_many_times=1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum


def show_message(message):
    print(message)


function_performance(show_message, "Wiadomość")

print(function_performance(sumuj_do, 500000))
print(function_performance(sumuj_do2, 500000))
print(function_performance(sumuj_do3, 500000))
print(function_performance(sumuj_do4, 500000))
print(function_performance(sumuj_do5, 500000))
