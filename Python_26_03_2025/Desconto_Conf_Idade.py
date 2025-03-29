# Desconto conforme a idade.

print("Olá! O programa irá calcular o desconto conforme sua idade.\n")

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print(f"Com {idade} anos você TEM direito ao desconto!")
elif idade >= 13 and idade <= 59:
    print(f"Com {idade} anos você NÃO tem direito ao desconto!")
else: 
    print(f"Com {idade} anos você TEM direito ao desconto!")