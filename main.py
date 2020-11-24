def firstMethod(lista, liczba):
    print("Pierwszy algorytm: ")
    if liczba in lista:
        print("Znaleziono")
    else:
        print("Nie znaleziono")
def secondMethod(lista, liczba):
    print("Pierwszy algorytm: ")
    l = 0
    r = len(lista)
    while l<=r:
        mid = l+int((r-l)/2)
        if lista[mid] == liczba:
            print("Znaleziono")
        elif lista[mid] < liczba:
            l=mid+1
        else:
            r=mid-1
    print("Nie znaleziono")
import time
from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]
start_firstMethod=time.time()
firstMethod(long_list, -1)
stop_firstMethod=time.time()
fisrt_result = stop_firstMethod - start_firstMethod
print(f'Czas wyszukiwania pierwszym sposobem: {fisrt_result}')
start_secondMethod=time.time()
secondMethod(long_list, -1)
stop_secondMethod=time.time()
second_result = stop_secondMethod - start_secondMethod
print(f'Czas wyszukiwania pierwszym sposobem: {fisrt_result}')