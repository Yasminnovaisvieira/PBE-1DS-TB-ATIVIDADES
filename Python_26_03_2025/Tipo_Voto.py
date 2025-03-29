# Se o usuário tem voto obrigatório, opcional ou não tem.

print("Olá! O programa irá verificar se o usuário tem voto obrigatório, opcional ou não tem.\n")

idade = int(input("Digite a sua idade:"))

if idade >= 18:
    print(f"Com {idade} anos o voto é OBRIGATÓRIO!")
elif idade >= 16:
    print(f"Com {idade} anos o voto é OPCIONAL!")
else:
    print(f"Com {idade} anos NÃO há voto!")