from random import randint
import pilha

binario = pilha.Pilha()
decimal = randint(10, 100)
print(f'({decimal})d = ', end="")

#empilhando
while decimal > 0:
  resto = decimal % 2
  decimal //= 2
  binario.push(resto)

#desempilhando
while not binario.isEmpty():
  print(binario.pull(), end="")