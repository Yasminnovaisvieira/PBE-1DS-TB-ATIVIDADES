# Se o número é maior que 10.

print("Olá! O programa irá verificar se o número é maior que 10.\n")

numero = int(input("Digite o número:"))

if numero > 10:
    print(f"{numero} é MAIOR que 10!")
elif numero == 10:
    print(f"{numero} é 10!")
else:
    print(f"{numero} é MENOR que 10!")