#Usuário digita um ano e retorna se ele é bissexto ou não.

print("Olá! O programa irá verificar se um ano é bissexto ou não.\n")

ano = int(input("Digite um ano:"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano informado é BISSEXTO!')
else:
    print('O ano informado NÃO é bissexto!')