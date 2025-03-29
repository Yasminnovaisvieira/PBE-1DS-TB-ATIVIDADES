# Solicitando data e mudando a ordem.

print(f"Olá! O programa irá trocar a ordem da data informada.\n")

data = str(input("Digite a data (dia/mês/ano):"))

dia = data [:2]
mes = data [3:5]
ano = data [6:]

data = f"{ano}/{mes}/{dia}"

print(f"Data (ano/mês/dia): {data}")