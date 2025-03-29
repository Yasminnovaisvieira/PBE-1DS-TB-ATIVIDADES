#Validando e convertendo data em formato diferente do inserido.

print("Olá! O programa irá verificar se a data é válida e mudar seu formato.\n")

data = input("Digite uma data (dia/mês/ano):")

parte_data = data.split('/') #O método separa a str em partes, usando a / como separador.

if len(parte_data) != 3:
    print("Formato inválido. A data deve estar no formato (dia/mês/ano)! Tente novamente.")
else:
    dia = int(parte_data[0])
    mes = int(parte_data[1])
    ano = int(parte_data[2])

    if mes < 1 or mes > 12:
        print("Mês inválido. O mês deve ser entre 1 e 12! Tente novamente.")
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            dias_mes = 31
            
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias_mes = 30
            
        else:
            dias_mes = 28

        if dia < 1 or dia > dias_mes:
            print(f"Dia inválido. O mês {mes} tem entre 1 e {dias_mes} dias.")
        else:
            print(f"{ano}/{mes:02d}/{dia:02d}")