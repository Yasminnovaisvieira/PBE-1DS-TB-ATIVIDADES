# Se o usuário é menor ou maior de idade.

print("Olá! O programa irá verificar se o usuário é maior de idade.\n")

idade = int(input("Digite a sua idade:"))

if idade >= 18:
    print(f"Com {idade} anos é considerado MAIOR de idade!")
else:
    print(f"Com {idade} anos é considerado MENOR de idade!")