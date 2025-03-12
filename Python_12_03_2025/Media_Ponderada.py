# 15 - Média Poderada com notas fornecidas pelo usuário.

nota1 = int(input("Digite o primeiro número: "))
nota2 = int(input("Digite o segundo número: "))
nnota3 = int(input("Digite o terceiro número: "))

peso1 = 2
peso2 = 3
peso3 = 5

media_ponderada = (n1*peso1 + n2*peso2 + n3*peso3) / (peso1+peso2+peso3)

print(f"O resultado da média ponderada é: {media_ponderada}")