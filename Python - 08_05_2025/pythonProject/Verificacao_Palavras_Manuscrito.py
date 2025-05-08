# Verificar se “Ana Ana”, “1DSTB-SENAI”, “Subi no Onibus” são palíndromos (para título de capítulos) dentro de um manuscrito.

def palindromo(palavra):
    palavra_minuscula = palavra.lower()
    if palavra_minuscula == palavra_minuscula[::-1]:
        print(f"A palavra '{palavra}' é um PALÍNDROMO!")

    else:
        print(f"A palavra '{palavra}' NÃO é um palíndromo!")


palindromo("Ana Ana")
palindromo("1DSTB-SENAI")
palindromo("Subi no Onibus")