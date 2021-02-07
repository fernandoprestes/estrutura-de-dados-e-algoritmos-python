from random import randint
import fila

filaNormal = fila.Fila()
filaPrioritaria = fila.Fila()
contador = 0

while contador < 10:
    idade = randint(18, 99)
    if idade > 60:
        filaPrioritaria.inserir(idade)
    else:
        filaNormal.inserir(idade)
    contador += 1

print(f'fila normal {filaNormal.data}')
print(f'fila prioritaria {filaPrioritaria.data}')

while contador > 0:
    if contador % 2 == 0 and not filaPrioritaria.isEmpty():
        filaPrioritaria.remover()
        filaPrioritaria.remover()
    else:
        filaNormal.remover()
    if filaPrioritaria.isEmpty() and filaNormal.isEmpty():
        contador = 0
    else:
        contador -= 1
