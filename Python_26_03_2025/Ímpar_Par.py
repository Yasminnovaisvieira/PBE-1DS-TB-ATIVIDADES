# Ímpar ou par.

print("Olá! O programa irá verificar se o número é ÍMPAR ou PAR.\n")

numero = int(input("Digite o número:"))

if numero % 2 == 0:
    print(f"{numero} é PAR!")
else:
    print(f"{numero} é ÍMPAR!")