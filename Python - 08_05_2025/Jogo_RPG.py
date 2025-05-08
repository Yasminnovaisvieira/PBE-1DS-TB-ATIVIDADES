# Classificação em um jogo de RPG ("Pequeno", "Médio" ou "Grande") para definir a dificuldade de um desafio (3, 9 e 12).

def tamanho_numero(numero):
    if numero <= 5:
        print(f"O número {numero} é PEQUENO!")

    elif numero <= 10:
        print(f"O número {numero} é MÉDIO!")

    else:
        print(f"O número {numero} é GRANDE!")


tamanho_numero(3)
tamanho_numero(9)
tamanho_numero(12)