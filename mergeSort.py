import timeit
from random import randint
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10**6)


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def generateList(size):
    list = []
    while size:
        list.append(size)
        size -= 1
    return list


def mergeSort(lista): 
    if len(lista) >1: 
        mid = len(lista)//2 
        L = lista[:mid]  
        R = lista[mid:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                lista[k] = L[i] 
                i+=1
            else: 
                lista[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            lista[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            lista[k] = R[j] 
            j+=1
            k+=1


size = [100000, 200000, 400000, 5000000, 1000000, 2000000]
time = []

for s in size:
    lista = generateList(s)
    time.append(timeit.timeit("mergeSoft({})".format(lista),
                              setup="from __main__ import mergeSoft", number=1))
    print(s)

desenhaGrafico(size, time, "Size", "Time",
               "MergeSoft.png")
