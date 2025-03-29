# Verificando se um CPF é válido.

print("Olá! O programa vai verificar se um CPF é válido com base nos dois dígitos verificadores.\n")

cpf = input("Digite o número do CPF (XXX.XXX.XXX-XX): ")

cpf = cpf.replace(".", "").replace("-", "")

if len(cpf) != 11:
    print("CPF inválido pois não contém 11 dígitos! Tente novamente.")
else:
    d1 = int(cpf[0])
    d2 = int(cpf[1])
    d3 = int(cpf[2])
    d4 = int(cpf[3])
    d5 = int(cpf[4])
    d6 = int(cpf[5])
    d7 = int(cpf[6])
    d8 = int(cpf[7])
    d9 = int(cpf[8])
    d10 = int(cpf[9])
    d11 = int(cpf[10])

    soma_1 = (d1 * 10) + (d2 * 9) + (d3 * 8) + (d4 * 7) + (d5 * 6) + (d6 * 5) + (d7 * 4) + (d8 * 3) + (d9 * 2)
    resto_1 = soma_1 % 11
    if resto_1 < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - resto_1
    
    soma_2 = (d1 * 11) + (d2 * 10) + (d3 * 9) + (d4 * 8) + (d5 * 7) + (d6 * 6) + (d7 * 5) + (d8 * 4) + (d9 * 3) + (d10 * 2)
    resto_2 = soma_2 % 11
    if resto_2 < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - resto_2
    
    if digito_1 == d10 and digito_2 == d11:
        print(f"O CPF {d1}{d2}{d3}.{d4}{d5}{d6}.{d7}{d8}{d9}-{d10}{d11} é VÁLIDO!")
    else:
        print(f"O CPF {d1}{d2}{d3}.{d4}{d5}{d6}.{d7}{d8}{d9}-{d10}{d11} é INVÁLIDO!")
