#Cálculo de Raiz Quadrada

import math

print("Olá! O programa irá realizar a raiz quadrada do número e também verificar se ele é negativo ou muito grande.\n")

numero = float(input("Digite um número: "))

if numero < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo! Tente novamente.")
elif numero > 100:
    print("Número muito grande, reduza para um valor abaixo de 100!")
else:
    raiz = math.sqrt(numero) #SQRT = Scare Root/Raiz Quadrada.
    print(f"A raiz quadrada de {numero} é {raiz:.2f}.")
