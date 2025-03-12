# 14 - Novos valores para a variável, sem utilizar uma terceira variável.

a = int(input("Digite o 1º número (A): "))
b = int(input("Digite o 2º número (B): "))

a, b = b, a

print (f"Valores invertidos:\n(A) = {a}\n(B) = {b}")