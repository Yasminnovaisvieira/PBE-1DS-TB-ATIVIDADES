# Verifica a sensação térmica (Frio, Aconchegante, Quente ou Muito Quente).

print(f"Olá! O programa irá verificar, conforme a temperatura em Celsius informada, qual a sensação térmica (Frio, Aconchegante, Quente ou Muito Quente).\n")

temperatura = float(input("Digite a temperatura em Celsius (ºC):"))

if temperatura < 10:
    print(f"A sensação térmica em {temperatura}ºC é FRIO")
elif temperatura >= 10 and temperatura < 25:
    print(f"A sensação térmica em {temperatura}ºC é ACONCHEGANTE!")
elif temperatura >= 25 and temperatura < 40:
    print(f"A sensação térmica em {temperatura}ºC é QUENTE!")
else:
    print(f"A sensação térmica em {temperatura}ºC é MUITO QUENTE!")