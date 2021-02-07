from random import randint

def bubbleSort(lista):
  for i in range(len(lista)-1):
    for j in range(len(lista)-i-1):
      if(lista[j] > lista[j+1]):
        lista[j], lista[j+1] = lista[j+1], lista[j]

def insertSort(lista):
  for i in range(1, len(lista)):
    valor = lista[i]
    posicao = i - 1
    while posicao >= 0 and lista[posicao] > valor:
      lista[posicao+1] = lista[posicao]
      posicao -= 1
    lista[posicao+1] = valor

def mergeSort(lista):
  if len(lista) > 1:
    meio = len(lista) // 2
    metadeEsq = lista[:meio]
    metadeDir = lista[meio:]
    mergeSort(metadeEsq)
    mergeSort(metadeDir)
    i = 0
    j = 0
    k = 0
    while i < len(metadeEsq) and j < len(metadeDir):
        if metadeEsq[i] < metadeDir[j]:
            lista[k] = metadeEsq[i]
            i+=1
        else:
            lista[k] = metadeDir[j]
            j+=1
        k+=1
        
    while i < len(metadeEsq):
        lista[k] = metadeEsq[i]
        i+=1
        k+=1
        
    while j < len(metadeDir):
        lista[k] = metadeDir[j]
        j+=1
        k+=1

def quickSort(lista, first, last):
    if first < last:
        splitpoint = partition(lista, first, last)
        quickSort(lista, first, splitpoint - 1)
        quickSort(lista, splitpoint+1, last)

def partition(lista, first, last):
    pivo = lista[first]
    pontoEsq = 1
    pontoDir = last
    done = False
    while not done:
        while pontoEsq <= pontoDir and lista[pontoEsq] <= pivo:
            pontoEsq += 1
        while lista[pontoDir] >= pivo and pontoDir >= pontoEsq:
            pontoDir -=1
        if pontoDir < pontoEsq:
            done = True
        else:
            lista[pontoEsq], lista[pontoDir] = lista[pontoDir], lista[pontoEsq]
    lista[first], lista[pontoDir] = lista[pontoDir], lista[first]
    return pontoDir

def heapSort(lista):
    if len(lista) < 2:
        return lista
   
    l, p, h = [], [], []

    valor = lista[randint(0, len(lista)-1)]
    for i in lista:
        if i < valor:
            l.append(i)
        elif i == valor:
            p.append(i)
        elif i > valor:
            h.append(i)
    return heapSort(l) + p + heapSort(h)
