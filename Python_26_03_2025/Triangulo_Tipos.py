# Verificando 3 lados e determinando se eles podem formar um triângulo. Caso sim, classificando-os como equilátero, isósceles ou escaleno.

print("Olá! O programa irá verificar se os lados informados formam um triângulo, caso sim, qual tipo.\n")

lado1 = int(input("Digite o 1º lado: "))
lado2 = int(input("Digite o 2º lado: "))
lado3 = int(input("Digite o 3º lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Os lados fornecidos formam um triângulo EQUILÁTERO!")
    elif (lado1 == lado2 != lado3) or (lado3 == lado2 != lado1) or (lado1 == lado3 != lado2):
        print("Os lados fornecidos formam um triângulo ISÓSCELES!")
    else:
        print("Os lados fornecidos formam um triângulo ESCALENO!")
else:
    print("Os lados fornecidos não podem formar um triângulo.")