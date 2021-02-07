def buscaBinariaRecursiva(lista, item, inicio, fim):
  meio = (inicio + fim) // 2
  if fim < inicio:
    return -1
  if item == lista[meio]:
    return meio
  elif item < lista[meio]:
    return buscaBinariaRecursiva(lista, item, inicio, meio - 1)
  elif item > lista[meio]:
    return buscaBinariaRecursiva(lista, item, meio + 1, fim)

def buscaBinariaIterativa(lista, item):
  inicio, fim = 0, len(lista)-1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == item:
      return meio
    elif lista[meio] > item:
      fim = meio - 1
    else:
      inicio = meio + 1
  return -1
