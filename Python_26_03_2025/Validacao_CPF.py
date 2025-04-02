# Verificando se um CPF é válido.

import re

print("Olá! O programa vai verificar se um CPF é válido com base nos dois dígitos verificadores.\n")

cpf = input("Digite o número do CPF (XXX.XXX.XXX-XX): ")
padrao = r"\d{3}\.\d{3}\.\d{3}\-\d{2}"
valido = re.match(padrao, cpf)

if valido:
    penul_digito = ((int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)) % 11
    ult_digito = ((int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (int(cpf[6]) * 6) + (int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)) % 11

    if penul_digito >= 2:
        digito1 = 11 - penul_digito
    else:
        digito1 = 0
    
    if ult_digito >= 2:
        digito2 = 11 - ult_digito
    else:
        digito2 = 0

    if int(cpf[12]) == digito1 and int(cpf[13]) == digito2:
        print(f"O CPF {cpf} é válido!")
    else:
        print(f"O CPF {cpf} é inválido!")
else:
    print(f"O CPF não foi digitado corretamente! Tente novamente.")
