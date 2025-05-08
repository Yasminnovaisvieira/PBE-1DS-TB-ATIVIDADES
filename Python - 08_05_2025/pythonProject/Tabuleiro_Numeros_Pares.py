# Tabuleiro que usa um dado de 10 faces. Verificação se os números 4, 7 e 10 são pares (jogador avança) ou ímpares (jogador recua)

def avancar_recuar(jogada):
    if jogada % 2 == 0:
        print("O valor do dado é PAR. O jogador deve avançar!")

    else:
        print("O valor do dado é ÍMPAR. O jogador deve recuar!")
    return jogada

avancar_recuar(4)
avancar_recuar(7)
avancar_recuar(10)