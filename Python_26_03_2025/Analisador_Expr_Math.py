#Analisador de expressões matemáticas simples no formato de string.

print("Olá! O programa irá analisar e calcular uma expressão matemática simples.\n")

expressao = input("Digite uma expressão matemática: ")

resultado = eval(expressao)

print(f"O resultado da expressão é: {resultado}")