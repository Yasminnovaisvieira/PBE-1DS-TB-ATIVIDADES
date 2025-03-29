# Verifica se 3 números estão em ordem crescente, decrescente ou se são iguais.

print(f"Olá! O programa irá verificar se os números estão em ordem crescente, decrescente ou se são iguais.\n")

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 == num2 == num3:
    print(f"Todos os números são IGUAIS! ({num1},{num2},{num3})")
elif num1 < num2 < num3:
    print(f"Os números estão em ordem CRESCENTE! ({num1},{num2},{num3})")
elif num1 > num2 > num3:
    print(f"Os números estão em ordem DECRESCENTE! ({num1},{num2},{num3})")
elif num1 == num2 and num2 < num3:
    print(f"O 1º e o 2º número são IGUAIS, e estão em ordem CRESCENTE! ({num1},{num2},{num3})")
elif num1 == num2 and num2 > num3:
    print(f"O 1º e o 2º número são IGUAIS, e estão em ordem DECRESCENTE! ({num1},{num2},{num3})")
elif num2 == num3 and num1 < num2:
    print(f"O 2º e o 3º número são IGUAIS, e estão em ordem CRESCENTE! ({num1},{num2},{num3})")
elif num2 == num3 and num1 > num2:
    print(f"O 2º e o 3º número são IGUAIS, e estão em ordem DECRESCENTE! ({num1},{num2},{num3})")
else:
    print("Os números NÃO estão em ordem crescente nem decrescente!")