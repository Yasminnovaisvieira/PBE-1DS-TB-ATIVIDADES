# IMC e qual a categoria o usuário se enquadra.

print(f"Olá! O programa irá calcular o índice de Massa Corporal (IMC).\n")

peso = float(input("Insira o peso (KG): "))
altura = float(input("Insira a altura (Metros): "))

imc = peso / (altura * altura)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print(f"A sua faixa é: BAIXO PESO.")
elif imc >= 18.5 and imc <= 24.9:
    print(f"A sua faixa é: NORMAL.")
elif imc >= 25 and imc <= 29.9:
    print(f"A sua faixa é: SOBREPESO.")
elif imc >= 30:
    print(f"A sua faixa é: OBESIDADE.")