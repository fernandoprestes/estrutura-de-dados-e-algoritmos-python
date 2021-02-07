
import ordenacao


lista1 = [50, 11, 3, 88, 79, 34, 17]
ordenacao.insertSort(lista1)
print(f"Insert Sort: {lista1}")


lista2 = [10, 9, 1, 78, 14, 54, 34, 2]
ordenacao.bubbleSort(lista2)
print(f"Bubble Sort: {lista2}")

        
lista3 = [5, 8, 69, 47, 2, 7, 89, 4, 6, 61]
ordenacao.mergeSort(lista3)
print(f"Merge Sort: {lista3}")


lista4 = [5, 212, 93, 37, 77, 31, 4, 55, 20]
ordenacao.quickSort(lista4, 0, len(lista4) - 1)
print(f"Quick Sort: {lista4}")


lista5 = [5, 13, 1, 145, 74, 32, 929, 47, 36, 9]
print(f"Heap Sort: {ordenacao.heapSort(lista5)}")