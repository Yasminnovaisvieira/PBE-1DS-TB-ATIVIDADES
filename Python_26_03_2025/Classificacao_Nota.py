# Classificação conforme nota.

print("Olá! O programa irá verificar qual categoria a nota se enquadra.\n")

nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida. Digite uma nota de 0 a 10!")
elif nota >= 9:
    print("Categoria: A")
elif nota >= 7:
    print("Categoria: B")
elif nota >= 5:
    print("Categoria: C")
elif nota >= 3:
    print("Categoria: D")
else:
    print("Categoria: E")