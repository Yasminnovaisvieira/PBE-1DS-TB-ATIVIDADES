# Se o número é positivo, negativo ou zero.

print("Olá! O programa irá verificar se o número é positivo, negativo ou zero.\n")

numero = int(input("Digite um número:"))

if numero > 0:
    print(f"{numero} é POSITIVO!")
elif numero < 0:
    print(f"{numero} é NEGATIVO!")
else:
    print(f"{numero} é ZERO!")