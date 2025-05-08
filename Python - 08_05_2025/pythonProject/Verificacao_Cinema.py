# Verificação três clientes (15, 20 e 8 anos) podem assistir a um filme para maiores de 18 anos.

def verificacao(idade):
    if idade < 18:
        if idade == 8:
            print("Você com 8 anos não tem idade o suficiente para ver esse filme. \nClassificação: +18!\n")
        elif idade == 15:
            print("Você com 15 anos não tem idade o suficiente para ver esse filme. \nClassificação: +18!\n")
    else:
        print("Você por ser maior de 18 anos poderá assistir o filme!\n")

verificacao(15)
verificacao(20)
verificacao(8)