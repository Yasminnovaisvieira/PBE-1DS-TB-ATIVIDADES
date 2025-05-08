# Calculo dos fatoriais de 3, 7, 9, 25, 26.

def fatorial(numero):
    if numero < 0:
        print(f"O número é INVÁLIDO. Digite um número positivo!")

    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i

        print(f"O fatorial de {numero} é: {resultado}")

    return resultado


fatorial(3)
fatorial(7)
fatorial(9)
fatorial(25)
fatorial(26)